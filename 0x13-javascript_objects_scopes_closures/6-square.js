#!/usr/bin/node

/*
 * A class square that defines a square and inherits
 * square from 5-square.js
 */
const P_square = require('./5-square');

class Square extends P_square {
  constructor (size) {
    super(size);
  }
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
