export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
  let i = weakMap.get(endpoint);

  if (i) {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else { weakMap.set(endpoint, 1); }

  i = weakMap.get(endpoint);

  if (i >= 5) {
    throw Error('Endpoint load is high');
  }
}
