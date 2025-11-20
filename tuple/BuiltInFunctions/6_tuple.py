# tuple() : A built-in function that can convert other data types (like lists) into tuples.
# Used : To convert other data types into tuple
# Syntax : tuple(iterable)
# Returns : A tuple containing elements of the iterable

list_data = [1, 2, 3, 4, 5, "string", 7.8]
# Converting list to tuple

tuple_data = tuple(list_data)
print(f"Converted tuple : {tuple_data}")

# output :
# Converted tuple : (1, 2, 3, 4, 5, 'string', 7.8)