#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    }
    else {
      for (let x = 0; x < this.height; x++) {
        let x = '';
        for (let y = 0; y < this.width; y++) x += c;
        console.log(x);
      }
    }
  }
}
module.exports = Square;
