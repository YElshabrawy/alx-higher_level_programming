#!/usr/bin/node
const args = process.argv;
args.shift();
args.shift();
if (args.length === 0) console.log('No argument');
else if (args.length === 1) console.log('Argument found');
else console.log('Arguments found');
