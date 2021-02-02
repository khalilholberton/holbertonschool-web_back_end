export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') { throw TypeError('Name must be a string'); }
    if (typeof length !== 'number') { throw TypeError('Length must be a number'); }
    students.forEach((student) => {
      if (typeof student !== 'string') { throw TypeError('Students must be an array of strings'); }
    });
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() { return this._name; }

  get length() { return this._length; }

  get students() { return this._students; }

  set name(givenName) {
    if (typeof givenName !== 'string') throw TypeError('Name must be a string');
    this._name = givenName;
  }

  set length(givenLength) {
    if (typeof givenLength !== 'number') throw TypeError('Length must be a number');
    this._length = givenLength;
  }

  set students(givenStudents) {
    givenStudents.forEach((s) => {
      if (typeof s !== 'string') { throw TypeError('Students must be an array of strings'); }
    });
    this._students = givenStudents;
  }
}
