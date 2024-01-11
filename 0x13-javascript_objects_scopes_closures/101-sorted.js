#!/usr/bin/node
const dict = require('./101-data').dict;
const output = {};
Object.entries(dict).forEach(([key, val]) => {
  const idx = Object.keys(output).findIndex(k => k.toString() === val.toString());
  if (idx === -1) {
    // If val not in output, create it
    output[val] = [key];
  } else {
    // If val exists, append into its arr
    output[val] = [...output[val], key];
  }
});
console.log(output);
