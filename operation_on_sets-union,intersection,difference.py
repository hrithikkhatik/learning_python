student_1={"english","maths","cs","chemistry","physics"}
student_2={"english","biology","chemistry","physics"}

#common subjects of student_1 and student_2 - intersection
common_subjects=student_1 & student_2
print(common_subjects)
common_subjects=student_1.intersection(student_2)
print(common_subjects)

#all subjects of student_1 and student_2 - union
all_subjects=student_1.union(student_2)
print(all_subjects)

student_3={"sanskrit","maths","cs"}

#all subjects of student_1,student_2 and student_3
all_subjects=student_1.union(student_2,student_3)
print(all_subjects)

common_subjects = student_1.intersection(student_2,student_3)
print(common_subjects)

all_subjects=student_1 | student_2 | student_3
print(all_subjects)

days={"mon","tue","wed","thu","fri","sat","sun"}
weekends={"sat","sun"}

#difference of sets
weekdays = days - weekends
print(weekdays)

