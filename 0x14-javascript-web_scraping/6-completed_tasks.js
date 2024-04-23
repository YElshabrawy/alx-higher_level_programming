#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  const output = {};
  const data = JSON.parse(res.body);
  data.forEach(el => {
    if (!output[el.userId]) {
      output[el.userId] = 0;
    }
    if (el.completed) {
      output[el.userId]++;
    }
  });
  console.log(output);
});
