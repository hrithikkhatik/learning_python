"""
#counting substring from a string
#count
#string.count(substring)
s1="we are learning python. python is fun"
s2="python"
print(s1.count(s2))
print(f"occurrence of {s2} is {s1.count(s2)}")

s3="we are learning python. python is fun"
s4="e"
print(s3.count(s4))
print(f"occurrence of {s4} is {s3.count(s4)}")

s5="we are learning python. python is fun"
s6="learn"
print(s5.count(s6))
print(f"occurrence of {s6} is {s5.count(s6)}")

s7="we are learning python. python is fun"
s8=" "
print(s7.count(s8))
print(f"occurrence of space is {s7.count(s8)}")


#changing case of a string
# upper() , lower() , tittle() ,capitalize()

s1="python"
print(s1.upper())

s2="python3.13"
print(s2.upper())
print(s2.lower())

s3="we are learning Pfython. Python is fun"
print(s3.upper())
print(s3.lower())
print(s3.title())
print(s3.capitalize())
"""
#starting and ending of a string

s1="we are learning python"

# startswith()
# string.startswith(substring)

print(s1.startswith("w"))
print(s1.startswith("we"))
print(s1.startswith("we are"))
print(s1.startswith("r"))
print(s1.startswith("W"))

#endswith()
print(s1.endswith("python"))
print(s1.endswith("n"))
print(s1.endswith("pytho"))
print(s1.endswith("on"))








