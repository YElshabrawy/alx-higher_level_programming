#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    const promises = characters.map(character => new Promise((resolve, reject) => {
      request.get(character, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    }));
    Promise.all(promises).then(characters => {
      characters.forEach(character => console.log(character));
    }).catch(err => console.log(err));
  }
}
);
