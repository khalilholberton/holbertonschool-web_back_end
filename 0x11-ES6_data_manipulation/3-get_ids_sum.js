export default function getStudentIdsSum(list) {
  return list.reduce((accumulator, x) => accumulator + x.id, 0);
}
