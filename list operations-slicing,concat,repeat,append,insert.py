"""

# slicing of list
l1= [3,8,1,0,4,9,7,3,6]
print(len(l1))
print(l1[1:6:1])
print(l1[2:7:2])

#concatenation of lists
l1=[1,7,2]
l2 = [0, 5]
print(l1 + l2)
print(l2 + l1)


#repetition of lists
l1=[1,7,2]
l2 = [0, 5]

# *
print(l2 * 3)

# append()
#adds an item to the end of the list

fruits = ["mango", "apple" ,"orange"]
print(fruits)
# syntax: list.append(item)
print(fruits.append("banana"))
fruits.append("banana")
print(fruits)
"""
#insert
#adds an element before the specified index
#sytax: list.insert(index,item)
fruits = ["mango", "apple" ,"orange"]
fruits.insert(2,"banana")
print(fruits)


s1="python is fun"
print(s1.replace("python","java"))









