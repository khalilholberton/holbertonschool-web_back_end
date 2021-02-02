export default function createIteratorObject(report) {
  const list = [];

  for (const x of Object.keys(report.allEmployees)) {
    list.push(...report.allEmployees[x]);
  }
  return list;
}
