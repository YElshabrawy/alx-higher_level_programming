#!/usr/bin/node
const _Square = require('./5-square');

class Square extends _Square {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) { line += c; }
      console.log(line);
    }
  }
}

module.exports = Square;
