# with open('sample.txt', 'r') as file:: Opens the file in read mode. The with statement ensures that the file is properly closed after its suite finishes.
# file.readlines(): Reads all lines from the file and returns them as a list.
# print(line.strip()): Prints each line after stripping away any leading or trailing whitespace, including newline characters.

# open the file in read mode
with open("xample.txt","r") as file:
    # use readlines() to get list of lines
    lines = file.readlines()

# print each line
for line in lines:
    print(f"{line.strip()}")

# Using strip() to remove newline characters