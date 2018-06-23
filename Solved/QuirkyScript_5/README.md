# QuirkyScript 5
Web

## Challenge 
> Get the flag.

> http://ctf.pwn.sg:8085

>Creator - quanyang (@quanyang)

> [challenge.js](challenge.js)

## Solution

	var flag=require("./flag.js");
	var express=require('express')
	var app=express()
	app.get('/flag', function(req,res){
		var re=new RegExp('^I_AM_ELEET_HAX0R$','g');
		if(re.test(req.query.fifth)){
			if(req.query.fifth===req.query.six&&!re.test(req.query.six)){
				res.send(flag.flag);
			}
		}
		res.send("Try to solve this.");
	});
	app.listen(31337)

---

Bug in the re.test

	>> var re=new RegExp('^I_AM_ELEET_HAX0R$','g');
	undefined
	>> re.test('I_AM_ELEET_HAX0R')
	true
	>> !re.test('I_AM_ELEET_HAX0R')
	true

Final URL
	
	http://ctf.pwn.sg:8085/flag?fifth=I_AM_ELEET_HAX0R&sixth=I_AM_ELEET_HAX0R

## Flag

	CrossCTF{1_am_n1k0las_ray_zhizihizhao}.