#!/usr/bin/node
let arr = process.argv;
arr.shift();
arr.shift();
arr = arr.map((itm) => parseInt(itm));
arr.sort().reverse();
console.log(arr[1] || 0);
