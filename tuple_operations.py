"""
concatenation, repetition, membership
count, index
min, max ,sum
"""
student_detail1=(1001,"john")
student_detail2=(78.5,91.0,83.5,79.5)

# +
student_details=student_detail1+student_detail2
print(student_details)

# *
t1=("class 5",5000)
print(t1*3)

# in, not in
print(91.0 in student_detail2)
print(99.0 in student_detail2)
print(91.0 not in student_detail2)
print(99.0 not in student_detail2)

# count()
t1=(10,4,1,9,0,3)
# tuple.count(element)
print(t1.count(1))

#index()
t1=(10,4,1,9,0,3,1)
# tuple.count(element)
print(t1.index(1))
print(t1.index(4))
#print(t1.index(40))

#min()
t1=(10,4,1,9,0,3,1)
#min(tuple)
#max(tuple)
#sum(tuple)
print(f"smallest number is:{min(t1)}")
print(f"biggest number is:{max(t1)}")
print(f"sum of {t1} is:{sum(t1)}")








 
