export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](givenHint) {
    if (givenHint === 'number') {
      return this._size;
    }
    return this._location;
  }
}
