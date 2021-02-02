export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((v) => v.location.localeCompare(city) === 0)
    .map((a) => {
      const gr = newGrades.filter((b) => b.studentId === a.id);
      const v = a;

      if (gr.length === 1) {
        v.grade = gr[0].grade;
      } else {
        v.grade = 'N/A';
      }
      return v;
    });
}
