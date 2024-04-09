#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // constructor of e' Rectangle class with e' size for both width and height.
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
