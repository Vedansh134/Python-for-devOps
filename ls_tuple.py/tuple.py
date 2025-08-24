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

# Concat
t1 = (2,4,6)
t2 = (1,3,5)

concat = t1 + t2
print(f"concatiantion : {concat}")

# repeat
repeat = t1*3
print(repeat)

# check
print(2 in t2) # false

# sliced
print(tup[0:3]) # 0 1 2 index only not 3

# min and max
print(max(t1))
print(min(t2))

# unpacking
tupl = ("python","js","node.js","express.js")
a,b,c,d = tupl
print(f"unpacking tupl :\n {a},\n {b},\n {c},\n {d}\n")