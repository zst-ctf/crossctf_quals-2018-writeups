# QuirkyScript 4
Web

## Challenge 
> Get the flag.

> http://ctf.pwn.sg:8084

> Creator - quanyang (@quanyang)

> [challenge.js](challenge.js)

## Solution

	var flag=require("./flag.js");
	var express=require('express')
	var app=express()
	app.get('/flag',function(req,res){
		if(req.query.fourth){
			if (req.query.fourth==1 && req.query.fourth.indexOf("1") == -1) {
				res.send(flag.flag);
				return;
			}
		}
		res.send("Try to solve this.");
	});
	app.listen(31337)

Simple array weak comparisons again

	>>> ['01'] == 1
	true
	>>> ['01'].indexOf("1")==-1
	true

Final URL

	http://ctf.pwn.sg:8084/flag?fourth[0]=01

## Flag

	CrossCTF{1m_g0ing_hungry}
