"""s1="hello world"
print(s1)

# length of the string
print(len(s1))

#indexing
print("first char",s1[0])
print("last char",s1[-1])
"""

s1="hello world"
"""
syntax of indexing : string[index]
syntax of slicing: string[start:end:stop]
-start: starting index at which the slicing operation starts
-end:ending index at which the slicing stops (excluded)
-stop: integer that specifies the stop for the slicing
"""
#print(s1[2:7:1])
#print(s1[2:9:2])
s1_slice=s1[1:12:3]
print(s1_slice)
print(type(s1_slice))





