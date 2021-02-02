export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') return '';
  if (typeof set !== 'object') return '';
  if (startString.length === 0) return '';

  const l = [];

  [...set].forEach((ob) => {
    if (ob && ob.indexOf(startString) === 0) l.push(ob.replace(startString, ''));
  });

  return l.join('-');
}
