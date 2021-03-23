#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        let x = '';
        for (let y = 0; y < this.width; y++) x += c;
        console.log(x);
      }
    }
  }
};
