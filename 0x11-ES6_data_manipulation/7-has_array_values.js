export default function hasValuesFromArray(set, array) {
  return array.filter((v) => set.has(v)).length === array.length;
}
