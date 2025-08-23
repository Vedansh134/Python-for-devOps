# list in python
# indexing start from 0

mixed = [34,"string",True,"types",4.5,False]

# Access the ele
print(mixed[0:]) # print all
print(mixed[:2]) # print till 0,1 not include 2

l = len(mixed)
print(mixed[3:l])  # print particular 3 to l

# Length
print(len(mixed)) # 6

# Append
mixed.append("append")
print(mixed)

# Remove
mixed.remove(False)
print(mixed)

# Pop
mixed.pop(3)
print(mixed)

# Reverse
mixed.reverse()
print(mixed)

# Extend
mixed.extend(["python",["libraray","pandas","NumPy","Scikit","Tensorflow","openCV"]])
print(mixed)
print(mixed[6][1]) # pandas
print(len(mixed[6][0])) # library=8

# Insert
mixed.insert(2,"insert")
print(mixed)

