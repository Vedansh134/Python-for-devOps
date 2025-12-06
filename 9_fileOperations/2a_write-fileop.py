# Write to a file
# Use write()

try:
    # open a file in write mode
    f = open("xample.py","w")

    # Write a string to the file
    f.write("This files open by write mode and write to this file")

    print(f"The content of the file : \n\t{f}")

    # check file is open or not
    print(f"Check the file the mode : {f.mode}\n")
    print(f"Is file closed or not ? : {f.closed}")

except FileNotFoundError:
    print("File is not found in given location")
except PermissionError:
    print("You have no access to perform write operation to the file")
finally:
    # close the file
    f.close()
    print(f"Is file closed or not ? : {f.closed}")
