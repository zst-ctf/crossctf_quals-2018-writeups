# QuirkyScript 3
Web

## Challenge 
> Get the flag.

>http://ctf.pwn.sg:8083

>Creator - quanyang (@quanyang)

> [challenge.js](challenge.js)

## Solution

	var flag=require("./flag.js");
	var express=require('express')
	var app=express()
	app.get('/flag',function(req,res){
		if(req.query.third){
			if(Array.isArray(req.query.third)){
				third=req.query.third;
				third_sorted=req.query.third.sort();
				if (Number.parseInt(third[0]) > Number.parseInt(third[1]) && 
				    third_sorted[0] == third[0] &&
				    third_sorted[1] == third[1]){
					res.send(flag.flag);
					return;
				}
			}
		}
		res.send("Try to solve this.");
	});
	app.listen(31337)

---

Make use of `Number.parseInt()` to exploit the sorting of arrays which happens to sort negative numbers in reverse numerical order.

	http://ctf.pwn.sg:8083/flag?third[0]=-1&third[1]=-2


## Flag

	CrossCTF{th4t_r0ck3t_1s_hug3}