nums = {1,3,2,0,-1}

#membership operator - in,not in
print( 0 in nums)
print(10 not in nums)
print(10 in nums)

nums_1={1,3,2,0,-1}
nums_2 = {3,5}

#concatenation ?
#print(nums_1 + nums_2)

# repeating set ?
#print(nums_1 * 2)

weekdays = ("mon","tue","wed","thur","fri","sat","sun")
weekdays = set(weekdays)
print(weekdays)

# are sets mutable or immutable ?
set1 = {2,0,-1}
#set1[0] = 10

#add()
set1.add(5)
print(set1)

#remove()
set1.remove(0)
print(set1)
#set1.remove(10)
#print(set1)

#discard()
set1.discard(0)
print(set1)
set1.discard(10)
print(set1)
