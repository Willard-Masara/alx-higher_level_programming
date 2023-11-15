#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  isValidDimension(dimension) {
    return Number.isInteger(dimension) && dimension > 0;
  }

  print() {
    if (this.width && this.height) {
      Array.from({ length: this.height }, () => console.log('X'.repeat(this.width)));
    }
  }
}

module.exports = Rectangle;
