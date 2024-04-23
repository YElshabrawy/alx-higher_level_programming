#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(res.body).results.filter((movie) => {
      return movie.characters.some((el) => el.endsWith('18/'));
    });
    console.log(results.length);
  }
});
