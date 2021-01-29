export default function appendToEachArrayValue(array, appendString) {
  const s = [];
  for (const value of array) {
    s.push(`${appendString}${value}`);
  }

  return s;
}
