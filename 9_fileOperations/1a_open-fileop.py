# Opening a File
# The open() function is used to open a file and takes the filename and an access mode as arguments. It returns a file object, often called a file handle, which is used to perform subsequent operations.

# opens a file in default mode
f = open("xample.txt","r")

# read its content
text = f.read()

# print its content
print(f"The content of file : \n{text}")

# Close the file
f.close()
