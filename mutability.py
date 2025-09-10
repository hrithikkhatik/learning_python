# mutability & immutability
# lists are mutable
# tuples and strings are immutable

s1="python is fun"
s1.replace("python","java")
print(s1)

s1 = "python is fun"
s2 = s1.replace("python","java")
print(s1)
print(s2)

t1=("mango","orange","apple")
#t2=t1.append("banana")
#print(t2)

l1=["mango","orange","apple"]
print(id(l1))
l1.append("banana")
print(l1)
print(id(l1))

l1 = ["mango","orange","aple"]
print(id(l1))
l1[-1]="apple"
print(l1)
print(id(l1))

fruits=("mango","orange","aple")
#fruits[-1]="apple"

s1="python is fun"
print(s1)
#s1[0]="p"
print(s1)












