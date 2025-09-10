# tuple
# (item1,item2,...)
# sequence of items as a collection

t1= ("python",10,1.5,True,[1,2,4],(10,20))
print(t1)

#accesing items of a tuple - index
print(t1[0])
print(t1[-1])

t2= 10,20,30,40
print(t1)
print(type(t1))

l1=[1,2,3]
print(l1,type(l1))
t3=tuple(l1)
print(t3,type(t3))
print(l1,type(l1))

fruits = ("mango","orange","apple")
print(fruits,type(fruits))
fruits=list(fruits)
print(fruits,type(fruits))


