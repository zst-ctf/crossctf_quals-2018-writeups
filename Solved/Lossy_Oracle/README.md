# Lossy Oracle
Crypto

## Challenge 
> No one believes I can recover the message from this crappy ORacle.

> `nc ctf.pwn.sg 1401`

> Creator - prokarius (@prokarius)

> [lossyoracle](lossyoracle)

## Solution

From the output, reverse base64 and we find the length of the `data` is 14160.

The provided file gives us a hint on how to decode --- it has 2 functions, one to OR and the other to AND.

By my theory, if we were to take many many of the encrypted bytes, then AND them together, we will eventually end up such that the bytes will become the original again.

	Take Example: (orig | A) & (orig | B) & (orig | C) & (orig | D)

	If A & B & C & D becomes zero, then we are left with orig.


After about 20 iterations, we get the output file.

	 $ file output.file 
	 output.file: MPEG ADTS, layer III, v2,  16 kbps, 24 kHz, Monaural

Rename it to `output.mpeg` and open it and we listen to the flag!

## Flag

	The flag is CrossCTF{bitw1se0racl3}