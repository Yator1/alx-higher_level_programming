#!/usr/bin/node

/*
 * A class square that defines a square and inherits
 * square from 5-square.js
 */
const Psquare = require('./5-square');

class Square extends Psquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
