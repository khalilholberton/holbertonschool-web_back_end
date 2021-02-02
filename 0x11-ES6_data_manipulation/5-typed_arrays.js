export default function createInt8TypedArray(length, position, value) {
  try {
    const Buf = new ArrayBuffer(length);

    const Ct = new DataView(Buf);

    Ct.setInt8(position, value);
    return Ct;
  } catch (err) {
    throw Error('Position outside range');
  }
}
