#!/usr/bin/node

/*
 * Class Rectangle that defines a rectangle:
 * An instance method prints the rectangle using the character X
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }

    return constructor.name + {};
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
