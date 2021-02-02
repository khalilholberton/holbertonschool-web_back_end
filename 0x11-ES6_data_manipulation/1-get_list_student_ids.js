export default function getListStudentIds(studs) {
  if (Array.isArray(studs) === false) {
    return [];
  }

  return studs.map((v) => v.id);
}
