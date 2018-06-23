# BabyRSA
Crypto

## Challenge 
> Each time I asked for the flag, it gets encoded through RSA. I'm lucky I kept all those values.

> Creator -- prokarius (@prokarius)

> [out.txt](out.txt)

## Solution

#### Broadcast attack

https://github.com/aaossa/Computer-Security-Algorithms/blob/master/11%20-%20Håstad's%20Broadcast%20Attack/hastads-broadcast-attack.py

Since message is same, with same exponent: 

	BabyRSA $ python3 solve.py 
	Read in values.
	Combine N.
	Solving.
	Flag.
	0x63726f73736374667b4861357461645f6368346c6c336e4765735f6152655f47657474316e675f623072694e675f6e30775f45687d73686974747970616464696e6773686974747970616464696e6773686974747970616464696e6773686974747970616464696e67
	crossctf{Ha5tad_ch4ll3nGes_aRe_Gett1ng_b0riNg_n0w_Eh}shittypaddingshittypaddingshittypaddingshittypadding

## Flag

	crossctf{Ha5tad_ch4ll3nGes_aRe_Gett1ng_b0riNg_n0w_Eh}