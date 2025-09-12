# comma separated  key_value pairs enclosed within{}
# {key1:value , key2;value2 ...}

groceries = {"milk":60,"biscuits":20 ,"rice":90,"bread":30}
print(groceries)
print(type(groceries))
print(len(groceries))

#print(groceries[0])
print(groceries["milk"])

#dict are mutable
groceries["milk"] = 65
print(groceries)
#print(groceries["eggs"])
groceries["eggs"] = 10
print(groceries)
