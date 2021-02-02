export default function updateUniqueItemsi(iMap) {
  if (!(iMap instanceof Map)) {
    throw Error('Cannot process');
  }
  for (const [k, v] of iMap) {
    if (v === 1) { iMap.set(k, 100); }
  }
  return iMap;
}
