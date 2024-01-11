#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((itm, i) => (itm * i));

console.log(list);
console.log(newList);
