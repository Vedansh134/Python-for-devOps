# reversed() : A built-in function in tuple
# Used : To convert reverse the elements of tuple
# Syntax : reversed(tuple)
# Returns : Returing the reversed iterator of the tuple

list_data = [1, 2, 3, 4, 5, "string", 7.8]

reversed = reversed(list_data)
print(f"Reversed elements of the tuple : {tuple(reversed)}")

# output :
# Reversed elements of the tuple : (7.8, 'string', 5,