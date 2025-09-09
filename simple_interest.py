"""
simple interest=(p * r * t) / 100
p=principal amount
r=rate of interest
t=time duration in year
"""
principal=float(input("enter principal amount:"))
rate=float(input("enter interest rate:"))
time=float(input("enter time:"))
si=(principal * rate * time) / 100
print("simple interest is:",si)

