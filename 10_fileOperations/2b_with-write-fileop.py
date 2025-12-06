# Write to a file
# Use write() with with

lines_to_write = ["First line\n", "Second line\n", "Third line\n"]

with open("xample.txt","w") as file:
    file.write("Write this content to the file")
