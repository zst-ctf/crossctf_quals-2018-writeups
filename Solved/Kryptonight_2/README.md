# Kryptonight 2
Crypto

## Challenge 
> Have I got a little story for you What you thought was your daddy Was nothin' but a

> nc ctf.pwn.sg 1503

> Creator - amon (@nn_amon)

## Solution

Again we get a sample hash

	~ $ nc ctf.pwn.sg 1503
	0100fb8e8ac805899323371bb790db19218afd8db8e3755d8b90f39b3d5506a9abce4fa912244500000000ee8146d49fa93ee724deb57d12cbc6c6f3b924d946127c7a97418f9348828f0f02 -> 87c4e570653eb4c2b42b7a0d546559452dfab573b82ec52f152b7ff98e79446f

Search on google and we find these

	https://github.com/fireice-uk/xmr-stak/issues/1227
	https://github.com/turtlecoin/turtlecoin/blob/master/tests/Hash/tests-cn-lite-v1.txt

Yet another variant of CryptoNight: Cryptonight-Lite Variant 1

---

Build the turtlecoin test hash function

	$ git clone https://github.com/turtlecoin/turtlecoin
	$ cd turtlecoin/tests

	$ cmake.
	$ make HashTests
	$ ./hash_tests 
	Wrong number of arguments

In the Turtlecoin code base, the function is called `cn_lite_slow_hash_v1` and the name `cryptonight-lite-v1`.

	# ./hash_tests cryptonight-lite-v1 ./Hash/crossctf.txt 
	terminate called after throwing an instance of 'std::ios_base::failure[abi:cxx11]'
	  what():  basic_ios::clear: iostream error
	Aborted

Weird error, fix it by commenting out this line in main.cpp

	if (input.rdstate() & ios_base::eofbit) {
      break;
    }
    // input.exceptions(ios_base::badbit | ios_base::failbit | ios_base::eofbit);
    input.clear(input.rdstate());

Now recompile and run

	./hash_tests cryptonight-lite-v1 ./Hash/crossctf.txt 
	Hash mismatch on test 3
	Input: xxx
	Expected hash: xxx
	Actual hash: 45c65cfb24267cec4d1111d1d4bd5865ccf6f24df76cb08e6e115345a57022b4

Submit the actual hash and let's go!

## Flag

	Flag: CrossCTF{d3ny_y0ur_m4ker_w3ll_b3_w4st1ng}