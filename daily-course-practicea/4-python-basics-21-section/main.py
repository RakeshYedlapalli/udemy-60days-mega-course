list = ["rakesh","Rajesh",3939,"dfjad"]

dictss = (293,994,"rakesh","Mahes")

print("This is list: ", list)
print("This is dict: ", dictss)

student = 'John Doe', 27, 'Python v3', 1234567890

print(student)

#tuples are immutable, so we can't change once it is assigned...


#strings way of accessing
str1 = "Rakesh"
print(str1[1])

list2 = ["rakesh","Rajesh"]

print(list2[0])
print(list2[1])
list2.append("Mahesh")
print(list2)


print(str1[1:3])
print(str1[1:])

print("Hell",str1[:-2])

jsonDictionary = {"Rakesh":"Y","Age":30,"gender":"Males","ROle":"Software engineer"}

# print(dict.get("Rakesh"))

arrayDictionary = [{"Rakesh":"Y","Age":30,"gender":"Male","ROle":"Software engineer"}, jsonDictionary]

print(arrayDictionary)

arrayDictionary.pop(0)

print(arrayDictionary)

print(arrayDictionary[0].get("Rakesh"))