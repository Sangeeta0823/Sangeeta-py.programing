grades = {"sangeeta":"A","vidya":"B"}
Attendance = {"sangeeta":90,"vidya":85}
grades["vidya"]="A"
Attendance["vidya"]=85
grades["mudra"]="c"
Attendance["mudra"]=80
grades.pop("sangeeta")
Attendance.pop("sangeeta")
for student in grades:
    print(student,"-grade",grades[student],"attendance",Attendance[student])
