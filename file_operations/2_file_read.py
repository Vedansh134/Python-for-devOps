# open("file path","operation-r/w")

# Open the file in read mode
# Note: If you don’t specify the mode, Python uses 'r' (read mode) by default.
f = open("C:/Users/HP/Desktop/Python/Sample.txt", "r")
print(f)

# Read its content
text = f.read()
print("Mode : ", f.mode)
print("Is Closed?", f.closed) # False

# file content
print(f"File content\t\n {text}")

# Close the file
f.close()

# check file status - True
print("Is Closed?", f.closed)
