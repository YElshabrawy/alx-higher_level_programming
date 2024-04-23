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
  data.map(todo => {
    if (todo.completed) {
      output[todo.userId] = (output[todo.userId] || 0) + 1;
      return output;
    }
  });
  console.log(output);
});
