"""
extend() - add at end like append
remove() - remove item
pop() - remove with index

#extend
fruits= ["apple","mango","orange"]
#fruits.append("banana","grapes") #give error 2 argument given but append takes only 1

fruits= ["apple","mango","orange"]
print(fruits)
fruits.extend(["banana","grapes"])
print(fruits)

fruits= ["apple","mango","orange"]
#fruits.extend("banana","grapes")
fruits.append(["banana","grapes"])
print(fruits)
print(len(fruits))


#remove()
fruits= ["apple","mango","orange","mango"]
print(fruits)
fruits.remove("mango")
print(fruits)
#fruits.remove("banana")
print(fruits)
"""
#pop
fruits= ["apple","mango","orange","mango"]
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop(-1)
print(fruits)
fruits.pop()
print(fruits)










