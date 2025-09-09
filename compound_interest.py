"""
Amount = P(1+R/100) ** T
Ci=Amount-P
"""
principal=float(input("enter principal amount:"))
rate=float(input("enter interest rate:"))
time=float(input("enter time:"))
Amount1 = principal * (1 + rate/100) **time
Amount2 = principal *  pow((1 + rate/100),time)
print(round(Amount2,2))
ci=Amount2-principal
print("compound interest:",round(ci))






