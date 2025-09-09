"""
when all the length of sides of the triangle is known -a,b,c
semi perimeter(s)=(a+b+c)/2
area = square root of ( s* (s-a) * (s-b) * (s-c))
"""
a=float(input("enter first side: "))
b=float(input("enter second side: "))
c=float(input("enter third side: "))
s= (a+b+c) / 2
area=(s*(s-a) * (s-b) * (s-c)) **0.5
print("area of triangle with given side", round(area,2))

