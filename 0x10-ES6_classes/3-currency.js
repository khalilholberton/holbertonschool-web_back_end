export default class Currency {
  constructor(code, name) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof code !== 'string') throw TypeError('Code must be a string');

    this._code = code;
    this._name = name;
  }

  get code() { return this._code; }

  get name() { return this._name; }

  set name(givenName) {
    if (typeof givenName === 'string') {
      this._name = givenName;
    } else {
      throw (TypeError('Attributes must be strings'));
    }
  }

  set code(givenCode) {
    if (typeof givenCode === 'string') {
      this._code = givenCode;
    } else {
      throw (TypeError('Attributes must be strings'));
    }
  }

  displayFullCurrency() { return `${this._name} (${this._code})`; }
}
