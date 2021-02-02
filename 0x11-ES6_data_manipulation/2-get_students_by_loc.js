export default function getStudentsByLocation(listStud, city) {
  return listStud.filter((listStud) => listStud.location === city);
}
