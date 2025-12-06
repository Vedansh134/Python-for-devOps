# Using the 'with' statement is a best practice as it automatically closes the file
with open("xample.txt","r") as file:
    content = file.read()

# print content on console
print(content)

# The with statement ensures the file is closed properly, even if errors occur.