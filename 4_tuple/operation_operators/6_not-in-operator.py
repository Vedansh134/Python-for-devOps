# not-in operator in Python with tuples : The 'not in' operator is used to check if a specific element does not exist within a tuple.
# It returns True if the element is not found, otherwise it returns False.
# Syntax : element not in tuple

tuple1 = ("Frontend","Backend","Fullstack","DevOps","Data Engineer","Data Scientist")
ele1 = "AIEngineer"

# using not-in operator to check element is not exist in tuple
not_in_ele = ele1 not in tuple1

print(f"{ele1} is not present in tuple1 : {not_in_ele}")

# output :
# AIEngineer is not present in tuple1 : True