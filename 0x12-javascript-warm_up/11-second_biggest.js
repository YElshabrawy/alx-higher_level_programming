#!/usr/bin/node
let arr = process.argv;
arr.shift();
arr.shift();
arr = arr.map((itm) => parseInt(itm)).filter((val) => !Number.isNaN(val));
arr = arr.sort((a, b) => b - a);
console.log(arr[1] || 0);
