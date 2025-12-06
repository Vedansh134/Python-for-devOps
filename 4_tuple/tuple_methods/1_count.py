# Count method in tuple
# Used : Count how many times a particular element is repeat in tuple

tuple = (2,4,6,8,(1,3,5,7),10,True,""," ","string",0,10)

no1 = 10
count = tuple.count(no1)
print(f"{no1} number repeat {count} times")

no2 = " "
count2 = tuple.count(no2)
print(f"{no2} repeat {count2} times")
print(type(no2))
