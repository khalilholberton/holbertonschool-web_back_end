export default function getListStudentIds(obj) {
  if (obj instanceof Array) return st.map((st) => st.id);
  return [];
}
