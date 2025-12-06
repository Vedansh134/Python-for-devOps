# repeat is an operator that allows you to repeat the elements of a tuple a specified number of times.
# It is represented by the * symbol.
# Syntax : tuple * n
# where tuple is the original tuple and n is the number of times to repeat the tuple.

tuple1 = ("Frontend","Backend","Fullstack","DevOps")
n = 3

# using * operator to repeat the elements of the tuple
result_tuple = tuple1*n

print(f"Repeated tuple is : {result_tuple}")

# output :
# Repeated tuple is : ('Frontend', 'Backend', 'Fullstack', 'DevOps', 'Frontend', 'Backend', 'Fullstack', 'DevOps', 'Frontend', 'Backend', 'Fullstack', 'DevOps')