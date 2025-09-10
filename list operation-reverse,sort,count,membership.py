"""
reverse()
sort()
count()
membership operation

days_of_week=["mon","tue","wed","thu","fri","sat","sun"]
print(days_of_week)
# reverse()
days_of_week.reverse()
print(days_of_week)

nums=[4,9,0,1,2,8]
print(nums)
#sort() -ascending order
nums.sort()
print(nums)
print("sorted list:", nums)
nums.sort(reverse=True) #reverse
print(nums)

#count()
numbers=[0,1,3,4,1,0,5,0,0,3,0]
print(numbers.count(0))
print(numbers)

numbers=[0,1,3,4,1,0,5,0,0,3,0]
print(f"the list is: {numbers}")
item_to_count=int(input("enter the number to be counted:"))
c= numbers.count(item_to_count)
print(f"occurrence of {item_to_count} is {c}")

language=["python","java","c++","python"]
print(f"the list is: {language}")
item_to_count=input("enter the item to be counted:")
c= language.count(item_to_count)
print(f"occurrence of {item_to_count} is {c}")
"""

#in
language=["python","java","c++","python"]
print("python" in language)
print("javascript" in language)
print("python" not in language)
print("javascript" not in language)







