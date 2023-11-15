class Rectangle {
  constructor(w, h) {
    if (this.isValidDimension(w) && this.isValidDimension(h)) {
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

  rotate() {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double() {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;

