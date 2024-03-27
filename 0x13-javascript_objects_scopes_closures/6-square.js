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

    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
