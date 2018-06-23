# Even Flow
Pwn

## Challenge 
> Do you like shell command injection?

>nc ctf.pwn.sg 1601

>Creator - amon (@nn_amon)


>[evenflow.py](evenflow.py)

## Solution

From the source, we see Flag can only be `[a-zA-Z0-9_{}]` and Shell can only be 2 chars.

The shell calls echo, hence the only meaningful 2 char input will be [special parameters](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html).

In particular, [let's use `$?`](https://unix.stackexchange.com/questions/22726/how-to-conditionally-do-something-if-a-command-succeeded-or-failed) which shows us the return value of `strcmp()` which is returned in the `main()`.


I shall assume `CrossCTF{` as the flag. Hence, let's try some stuff to test out `strcmp()`

	~ $ nc ctf.pwn.sg 1601
	Flag: B
	Shell: $?
	1
	~ $ nc ctf.pwn.sg 1601
	Flag: D
	Shell: $?
	255

So we can see that the return value is unsigned 8 bits:

	+1 for B to C, and
	-1 (255) for D to C

We can make a script to take the return value and then append that value as a char.
- [`strcmp` returns the difference of the current char to the compared char](http://www.tutorialspoint.com/ansi_c/c_strcmp.htm).
- Since C has a null byte ending, the return value is the compared char - \0
- hence the return value is the char itself.

Now run my script and we get the flag!

## Flag

	CrossCTF{I_just_want_someone_to_say_to_me}
