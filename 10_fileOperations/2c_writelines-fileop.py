# List of strings to write to the file
lines = [
    "This is the first line.\n",
    "This is the second line.\n",
    "This line is update.\n"
]

try:
    with open("xample.txt","w+") as f:
        # write multiple lines to this file
        # Use w+ mode for read/write
        f.writelines(lines)

        print("Write to file is complete!")
        print(f"File mode : {f.mode}")
        print(f"File is closed : {f.closed}")

        # Now the file is closed after the with block

        # # Re-open the file in read mode to display its content
        # with open("xample.txt","r") as file:
        #     content = file.read()
        #     print(f"The content of the file : \n\t{content}")

        # Move to beginning of file to read
        f.seek(0)

        # Read and display content
        content = f.read()
        print(f"The content of the file : \n{content}")

except PermissionError:
    print("you have no rights to write on this file")
except Exception as e:
    print(f"An error occured : {e}")
finally:
    print("This code is definitly run")
    print(f"Now check Is file closed or not ? {f.closed}")
