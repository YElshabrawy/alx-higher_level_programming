#!/usr/bin/node
let c = 0;
process.argv.shift();
process.argv.shift();
process.argv.forEach((arg) => {
  console.log(arg);
  c++;
});
if (c === 0) console.log('No argument');
