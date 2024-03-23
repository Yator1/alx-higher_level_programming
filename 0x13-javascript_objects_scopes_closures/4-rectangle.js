#!/usr/bin/node

/*
 * Class Rectangle that defines a rectangle:
 * An instance method print()
 * An instance method rotate()
 * An instance method double()
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

  rotate () {
    // exchanges the width and the height of the rectangle
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // multiples the width and the height of the rectangle by 2
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}

module.exports = Rectangle;
