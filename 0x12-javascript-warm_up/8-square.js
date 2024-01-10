#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (!n) console.log('Missing size');
else {
  for (let i = 0; i < n; i++) {
    let line = '';
    for (let j = 0; j < n; j++) line += 'X';
    console.log(line);
  }
}
