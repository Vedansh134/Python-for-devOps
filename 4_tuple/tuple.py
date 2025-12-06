# tuple is used to store multiple items in a single variable
# tuple is one of 4 built-in data types in Python used to store collections of data
# tuple is ordered, unchangeable, and allow duplicate values

# create a tuple
empty_tuple=()
print(type(empty_tuple))

tup=(1)
print(type(tup)) # class : int (needs atleast one comma for tuple)

tupb=(1,)
print(type(tupb))

tup1 = (1,3,5,9,(10,11,12,(13,14),15),16,"string",True,16)
print("elements : ",tup1)
print("1st : ",tup1[0])
print("Access nested elements : ",tup1[4][3][1])