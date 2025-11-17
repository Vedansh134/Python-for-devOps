# lists are like a data structure to store values

list_mixed = ["fruits",True,0,100.0,False]

# Use typeof keyword
print("Type of object : ",type(list_mixed))

# Access the values of list / slicing (access any particular element from range)
print(list_mixed[0:])
print(list_mixed[:2])
print(list_mixed[2:4])

# nested list

my_list = [1,2,3,4,[5,6,7],8]

print("The elements : ", my_list)
print("Nested elements : ", my_list[4][0])

# change elements
my_list[4][2] = "append"
print("The elements : ", my_list)

# appending elements in nested
my_list[4].append(9)
print("The elements : ", my_list)