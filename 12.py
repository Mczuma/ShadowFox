import csv
open('student_marks.csv', 'r') as file
reader="csv.DictReader(file)"
student_data=list(reader)
dictionary: total_marks
for student in student_data:
    total_marks=sum(int(mark) for mark in student.values() if mark.isdigit())
    student['total_marks']=total_marks
dictionary: average
for student in student_data:
    average=student['total_marks']/len([mark for mark in student.values() if mark.isdigit()])
    student['average']=average
open('updated_student_marks.csv','w', newline='') as file:
writer =csv.DictWriter(file,fieldnames=student_data[0].keys())
writer.writeheader()
writer.writerows(student_data)


