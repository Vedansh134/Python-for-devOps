# sum() is a Built-in function in tuple
# Used : To get the sum of all elements in the tuple
# Syntax : sum(tuple)
# Returns : Sum of all elements in the tuple
# Note : All elements in the tuple must be of numeric type

tuple = (1,2,3,5,6,8,9,56,4,6,7,4,5)
# Gives error if tuple contains non-numeric types like "","string"

total = sum(tuple)
print(f"Sum of all elements in the tuple : {total}")

# output :
# Sum of all elements in the tuple : 116
