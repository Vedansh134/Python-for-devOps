# Tuple is inmutable
# append and remove is not allowed in tuple

a = ()
print(type(a))

a = (3,) # need , for tuple
print(type(a))
print(a)

tup = ("vedansh",22,"moz","up","india",22)
print(tup)

# count
count = tup.count(22)
print(f"Total no :  {count}")

# Length
print(len(tup))

# Reverse
rev = tuple(reversed(tup))
print(f"reverse order : {rev}")

# index
ind = tup.index(22)
print(f"{ind}")