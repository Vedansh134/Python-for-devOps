#
# ===================== file operations in python ======================
#
# Use open() to open the file and use close() for closing the file
# Use try-except for handling the errors
#
#  ---------- common error :
# 1. File not exist
# 2. File name may be incorrect
# 3. Not enough permissions to open the file


# use try-except for handling the errors occured during file operations
try:
    # opens the file in default mode
    f = open("servers.txt","r")

    # read its content
    text = f.read()

    # print its content
    print(f"CONTENT OF FILE \n{text}")
    
except FileNotFoundError:
    print("Error! File not exist")
    
except PermissionError:
    print("You have not enough permissions to open the file")
    
except Exception as e:
    print(f"Error! occured : {e}")
    
else:
    # Closing the file
    f.close()