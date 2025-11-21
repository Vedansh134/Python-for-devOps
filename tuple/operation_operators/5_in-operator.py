# in operation with tuples : The 'in' operator is used to check if a specific element exists within a tuple.
# It returns True if the element is found, otherwise it returns False.
# Syntax : element in tuple

tuple1 = ("Frontend","Backend","Fullstack","DevOps","Data Engineer","Data Scientist")
element1 = "DevOps"
element2 = "AI Engineer"

# using 'in' operator to check if element1 exists in the tuple
is_element1_in_tuple = element1 in tuple1

# using 'in' operator to check if element2 exists in the tuple
is_element2_in_tuple = element2 in tuple1

print(f"Is '{element1}' in tuple? : {is_element1_in_tuple}")
print(f"Is '{element2}' in tuple? : {is_element2_in_tuple}")

# output :
# Is 'DevOps' in tuple? : True
# Is 'AI Engineer' in tuple? : False
