# slicing in tuples : Slicing is used to extract a portion of a tuple by specifying a range of indices.
# Syntax : tuple[start:end]
# where start is the starting index (inclusive) and end is the ending index (exclusive).
# If start is omitted, it defaults to 0.
# If end is omitted, it defaults to the length of the tuple.

tuple1 = ("Frontend","Backend","Fullstack","DevOps")

slicing1 = tuple1[1:3]
slicing2 = tuple1[0:]
slicing3 = tuple1[:0]

print(f"return the slicing1 tuple : {slicing1}")
print(f"return the slicing2 tuple : {slicing2}")
print(f"return the slicing3 tuple : {slicing3}")

# output :
# return the slicing1 tuple : ('Backend', 'Fullstack')
# return the slicing2 tuple : ('Frontend', 'Backend', 'Fullstack', 'DevOps')
# return the slicing3 tuple : ()

