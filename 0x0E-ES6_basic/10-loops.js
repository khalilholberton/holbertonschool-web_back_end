export default function appendToEachArrayValue(array, appendString) {
  /* eslint-disable guard-for-in */
  for (const idx in array) {
    /* eslint-disable no-param-reassign */
    const value = array[idx];
    array[idx] = appendString + value;
  }

  return array;
}
