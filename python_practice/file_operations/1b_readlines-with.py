#
# with open('sample.txt', 'r') as file:: Opens the file in read mode. 
# with statement ensures that the file is properly closed.
# file.readlines(): Reads all lines from the file and returns them as a list.
# print(line.strip()): Prints each line after stripping away any leading or trailing whitespace, including newline characters.
#

try:
    # open the file in read mode
    with open("servers.txt") as file:
        # use readlines() to get a list of lines
        lines = file.readlines()
    
    # print each line
    for line in lines:
        print(f"{line.strip()}")
    
except FileNotFoundError:
    print("Error!, File does not exist.")
    
except PermissionError:
    print("Error!, you have not enough permissions to open the file.")
    
except Exception as e:
    print(e)
    
finally:
    print("This runs always")
    