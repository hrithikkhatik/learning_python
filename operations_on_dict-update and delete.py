from learning_python_1.intro_dictionaries import groceries

student_1 = {"maths":80.5 , "english":76.0 ,"physics":89.0}
print(student_1)

# fetch the marks for "physics"
print(student_1["physics"])
#print(student_1["chem"])

#get()
print(student_1.get("physics"))
print(student_1.get("chem"))

emp1 = {"id":1001 ,"name":"john" ,"salary":10000}
print(emp1.get("phone"))

#membership operator => in
print(1000 in emp1)
print("name" in emp1)

emp1["phone"] =9876543210
print(emp1)

sem1_marks = {"maths":78.5 , "eng": 71.0 ,"phy": 86.5}
sem2_marks = {"chem":81.5 ,"bio":90.5}

sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 ={"milk":60,"rice":100,"biscuits":20,}
groceries_2={"rice":110,"bread":30}
groceries_1.update(groceries_2)
print(groceries_1)

#pop()
groceries_1.pop("milk")
print(groceries_1)

groceries_3={"milk":60,"rice":100,"biscuits":20,"milk":85,}
print(groceries_3)

#key cannot be duplicate in a dict
