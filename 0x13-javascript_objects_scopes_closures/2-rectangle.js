#!/usr/bin/node

// class Rectangle that defines a rectangle:

class Rectangle {
  constructor (w, h) {
    if ( w <= 0 || h <= 0) {
      const new_obj = {};
      return new_obj;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
