# BabyRSA 2
Crypto - 1 points

## Challenge 
> Each time I asked for the flag, it gets encoded through RSA.... again... I'm lucky I kept all those values... AGAIN!

> Creator -- prokarius (@prokarius)

> [out.txt](out.txt)

## My workings

We are given 5 `n, e, c` but all the `n` are the same?
All the `c`s are of length 2048 hex-chars (which is 1024 bytes)


[Common Modulus Attack](https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack)?

- https://pequalsnp-team.github.io/writeups/common_modulus
- https://raw.githubusercontent.com/sourcekris/ctf-solutions/master/crypto/plaidctf-strength/strpwn.py

But it only works if gcd(e1, e2) == 1

---

### Manupulate maths?

So I tried to do some maths myself -.-

Theory Reference:
- https://crypto.stackexchange.com/questions/1614/rsa-cracking-the-same-message-is-sent-to-two-different-people-problem/1616
- https://crypto.stackexchange.com/questions/16283/how-to-use-common-modulus-attack?rq=1
- https://crypto.stackexchange.com/questions/2516/can-two-different-pairs-of-rsa-key-have-the-same-modulus?rq=1

Failed Maths working:

    m = c1^a * c2^b

    m1^(e1*a) * c2^(e2*b)

	If gcd(e1, e2) != 1

	    Let g = gcd(e1, e2)
	    Let e1//g = f1
	    Let e2//g = f2

	Then m is the common message

	m^(g*f1*a) * m^(g*f2*b)
	= m^(g*f1*a + g*f2*b)

	= m^(g*f1*a + g*f2*b)

	----

	Hence for (g*f1*a + g*f2*b) == 0,
	Let A = f2 and B = -f1

	Then (g*f1*A + g*f2*(B)) == 0

	(g*f1*A + g*f2*(B-1))
	= (g*f1*f2 + g*f2*(-f1-1))
	= g(f1*f2 + (-f1-1)*f2)
	= g(f1*f2 - f1*f2 - f2)
	= g(0 - f2)
	= -f2*g

	Let X=f2*g
	m^X = m1^(e1*A) * c2^(e2*B)

---

Failed Maths working 2:

	m =~ c1^a * c2^b 
	m =~ m^(e1*a) * m^(e2*b)
	m =~ m^(e1*a + e2*b)

	---------------------

	Let g = gcd(e1, e2)
	Let e1//g = f1
	Let e2//g = f2

	If gcd(e1, e2) != 1:
	Then c1^a * c2^b 
	=~ m^(e1*a) * m^(e2*b)
	=~ m^(f1 * g * a + f2 * g *b)
	=~ m^(g * (f1 * a + f2 * b))

	Now find a, b where (f1 * a + f2 * b) == 1
	ie. gcd(f1, f2) == 1
	and gcd(e1, e2) == g:

	So m^g <mod n> = c1^a * c2^b 
	Get m

---

	c1 = m^(e1) mod n
	c2 = m^(e2) mod n

	c1 = m^(f1*g) mod n
	c2 = m^(f2*g) mod n

	c1^a * c2^b = m^(f1*g*a) * m^(f2*g*b) mod n
	c1^a * c2^b = m^(f1*g*a+f2*g*b) mod n
	c1^a * c2^b = m^(g*[f1*a + f2*b]) mod n

---

#### GCD comparison

I tried to compare GCD

	$ ./gcd_exp.sage

	50734392291911 = 27087235607 * 1873
	50734392291911 = 21524986123 * 2357
	50734392291911 = 25379886089 * 1999
	50734392291911 = 8824907339 * 5749

	197276336925781 = 27087235607 * 7283
	197276336925781 = 83698064033 * 2357
	197276336925781 = 98687512219 * 1999
	197276336925781 = 34314895969 * 5749

	156766473933809 = 21524986123 * 7283
	156766473933809 = 83698064033 * 1873
	156766473933809 = 78422448191 * 1999
	156766473933809 = 27268476941 * 5749

	184841710386187 = 25379886089 * 7283
	184841710386187 = 98687512219 * 1873
	184841710386187 = 78422448191 * 2357
	184841710386187 = 32151976063 * 5749

	64271800149937 = 34314895969 * 1873
	64271800149937 = 8824907339 * 7283
	64271800149937 = 27268476941 * 2357
	64271800149937 = 32151976063 * 1999

The exponennts are all related to each other (all of them are have one missing factor)

From factordb:

	e1 = 50734392291911  = 1873 · 1999 · 2357 · 5749
	e2 = 197276336925781 =        1999 · 2357 · 5749 · 7283
	e3 = 156766473933809 = 1873 · 1999 ·        5749 · 7283
	e4 = 184841710386187 = 1873 ·        2357 · 5749 · 7283
	e5 = 64271800149937  = 1873 · 1999 · 2357 ·        7283
	                 lcm = 1873 · 1999 · 2357 · 5749 · 7283


	c1^7283 = (m^(e1) mod n)^7283
	c2^1873 = (m^(e2) mod n)^1873
	c3^2357 = (m^(e3) mod n)^2357

	c1^7283 = (m^(e1) - k1*n)^7283
	c2^1873 = (m^(e2) - k2*n)^1873

---

Tried revisiting the Common Modulus Attack. 


	c1 = m^(e1) mod n
	c2 = m^(e2) mod n

	c1^x * c2^y * c3^z * c4^a = m^(e1*x + e2*y + e3*z + e4*a) <mod n>

	Let x = 7283
	Let y = 1873
	Let z = -2357
	Let a = -1999

	Hence 
	c1^x * c2^y * c3^z * c4^a = m^(lcm + lcm - lcm - lcm) <mod n>
	                          = m^(0) <mod n>

	c1^x * c2^y * c3^z * c4^(a+1) = m^1 <mod n>


	c1^a * c2^b = m^(f1*g*a+f2*g*b) mod n
	c1^a * c2^b = m^(g*[f1*a + f2*b]) mod n

---


	sage: xgcd(1873, 1999)
	(1, 587, -550)
	sage: xgcd(1873, 2357)
	(1, 823, -654)
	sage: xgcd(1873, 5749)
	(1, 1194, -389)
	sage: xgcd(1873, 7283)
	(1, -906, 233)


---

	e1: 1873 · 1999 · 2357 · 5749
	e2:        1999 · 2357 · 5749 · 7283
	e3: 1873 · 1999 ·        5749 · 7283
	e4: 1873 ·        2357 · 5749 · 7283
	e5: 1873 · 1999 · 2357 ·        7283
	lcm:1873 · 1999 · 2357 · 5749 · 7283

	1873(587) + 1999(-550) = 1
	1873(823) + 2357(-654) = 1
	1873(1194) + 5749(-389) = 1
	1873(-906) + 7283(233) = 1

	sage: xgcd(1873, 1999)
	(1, 587, -550)

	sage: xgcd(1873 * 1999, 2357)
	(1, 689, -1094486)

	sage: xgcd(1873 * 1999 * 2357, 5749)
	(1, -2015, 3093092414)

	xgcd(1873 * 1999 * 2357 * 5749, 7283)
	(1, 3239, -22563325090416)

	e4*587 + e2*-550 = 2357 · 5749 · 7283

	(e4*587 + e2*-550) * -1094486 + e3*689 = 5749 · 7283

	(e4*587 + e2*-550) * -1094486 + e3*689 = 5749 · 7283

	((e4*587 + e2*-550) * -1094486 + e3*689) * 3093092414 + e5 * -2015 = 7283

	(((e4*587 + e2*-550) * -1094486 + e3*689) * 3093092414 + e5 * -2015) * -22563325090416 + e1 * 3239 = 1

Simplify it

	e1 * 3239 +
	e5 * -2015 * -22563325090416 +
	e3*689 * 3093092414 * -22563325090416 +
	e2*-550 * -1094486 * 3093092414 * -22563325090416 +
	e4*587 * -1094486 * 3093092414 * -22563325090416

	Hence,
	x = 3239
	y = -550 * -1094486 * 3093092414 * -22563325090416
	z = 689 * 3093092414 * -22563325090416
	a = 587 * -1094486 * 3093092414 * -22563325090416
	b = -2015 * -22563325090416

	c1^x * c2^y * c3^z * c4^a * c5^b = m^(e1*x + e2*y + e3*z + e4*a + e5*b) <mod n>

The computation is too large to be done. I stopped attempting from here.


## Flag

	??