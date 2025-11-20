# sorted() is a Build-in function in tuple
# Used : Arrange elements in ascending order
# Syntax : sorted()
# Returns : elements in ordered list

tuple = (1,2,3,5,6,8,9,56,4,6,7,4,5)
# Gives error if tuple contains unorderable types like "","string"

sorted_tuple = sorted(tuple)
print(f"Elements in the tuple in sorted order : {sorted_tuple}")

# output :
# Elements in the tuple in sorted order : [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 56]
