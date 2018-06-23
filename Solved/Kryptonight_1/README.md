# Kryptonight 1
Crypto

## Challenge 
> I took a walk around the world to ease my troubled mind.

> `nc ctf.pwn.sg 1502`

> Creator - amon (@nn_amon)

## Solution

#### The challenge

	$ nc ctf.pwn.sg 1502

	00000000000000000000000000000000000000000000000000000000000000000000000000000000000000 -> b5a7f63abb94d07d1a6445c36c07c7e8327fe61b1647e391b4c7edae5de57a3d
	
We are given a hex string of zeros which is hashed.
We are then given another hex string and we need to find the hash.


---

#### Cipher?

At first, my team assumed it is [a cipher](https://github.com/gilsho/kryptonite/blob/master/README.md
).

	from kryptonite import Cipher
	key = Cipher.generate_key()
	cipher = Cipher(key)
	cipher_text = cipher.encrypt('my message')
	plain_text = cipher.decrypt(cipher_text)

https://stackoverflow.com/questions/31001997/how-to-get-a-key-stream-block-for-a-specific-counter-in-aes-ctr-encryption

	If you just need the key stream that was XORed with the first 16 bytes of plaintext (as the picture suggests) then you need to encrypt a block of 16 bytes set to 00 using the same AES CTR mode. A block of key stream, when XOR'ed with all zero's simply returns the same stream.


However, since the output is shorter in length than the input, we doubt it is a cipher

---

#### Hashing algorithm

Searching for hasing algorithms online, we find out that it is an [algorithm called CryptoNight](https://www.google.com.sg/search?client=opera&q="b5a7f63abb94d07d1a6445c36c07c7e8327fe61b1647e391b4c7edae5de57a3d"&sourceid=opera&ie=UTF-8&oe=UTF-8)

#### Using old CryptoNight libraries

I tried 2 different python cryptonight hash libraries but they gave a different hash.

	git clone https://github.com/sumoprojects/cryptonight-hash-lib
	cd cryptonight-hash-lib/
	cmake .
	make

	>>> import cryptonite_hash
	>>> dir (cryptonite_hash)
	['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cpu_has_aes_in_supported', 'cryptolite_hash', 'cryptolite_scanhash', 'cryptonite_hash', 'cryptonite_scanhash']

	>>> b = (b"00000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
	>>> binascii.hexlify(cryptonite_hash.cryptonite_hash(b, 1))
	b'dd05b92f7b44f57faf72e80539db202556e8df11ed677bcda96162d80dae2b38'
	
	>>> b = bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000")
	>>> binascii.hexlify(cryptonite_hash.cryptonite_hash(b, 0))
	b'bcf1903f00a993c8dca0a25d2b264ea1bdb7c8d4b188a95d1305c7b3b84d9fc6'

And another
	
	# https://github.com/maoxs2/pycryptonight
	$ git clone https://github.com/maoxs2/pycryptonight
	$ cd pycryptonight
	$ python3 setup.py install

	>>> import binascii
	>>> from pycryptonight import cpu_has_aes_in_supported, cryptolite_hash, cryptonite_hash

	>>> HAS_AES_NI = cpu_has_aes_in_supported() # return a bool
	>>> b = b'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

	>>> binascii.hexlify(cryptonite_hash(b, HAS_AES_NI))
	b'dd05b92f7b44f57faf72e80539db202556e8df11ed677bcda96162d80dae2b38'

This was when I found out that crypto-currency is so complex and fragmented, with many variants of hash algorithms.

---

#### Variant of the algorithm?

Unfortunately, it seems like these cryptonight has different variants too!

[Looking deeper at the Google Search results](https://www.google.com.sg/search?client=opera&q="b5a7f63abb94d07d1a6445c36c07c7e8327fe61b1647e391b4c7edae5de57a3d"&sourceid=opera&ie=UTF-8&oe=UTF-8
), the version is `cn_slow_hash`.

With this, I found the correct library for it

	# https://github.com/ph4r05/py-cryptonight

	>>> import binascii
	>>> from pycryptonight import *
	
	>>> binascii.hexlify(cn_slow_hash(bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000')))
	b'1638735d10436894e654a01ee580b9538a760a1ba58f23df2ecf6b841b5e1f12'
	
	>>> binascii.hexlify(cn_slow_hash(bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 1)) # variant 1
	b'b5a7f63abb94d07d1a6445c36c07c7e8327fe61b1647e391b4c7edae5de57a3d'

Now nc to the server and then hash the output using variant 1 of this cryptonight library `._.`

## Flag

	Flag: CrossCTF{h0dl_t1l_u_d1e}
