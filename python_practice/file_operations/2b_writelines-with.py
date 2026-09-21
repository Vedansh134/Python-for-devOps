# ========== 

lines = [
    "This is the first line.\n",
    "This is the second line.\n",
    "This line is update.\n"
]

try:
    with open("write.txt","w+") as f:
        # Write multiple lines in this file
        # use w+ operation for perform for read/write
        f.writelines(lines)
        
        print(f"File is closed : {f.closed}")
        print(f"Check file mode : {f.mode}")
        
        # Move to beginning in file to read
        f.seek(0)
        
        # Now read and display the content of the file
        content = f.read()
        print(f"Content of file : {content}")
        
        
except FileNotFoundError:
    print("Error!, File is not exist")
    
except PermissionError:
    print("Error!, You have not enough permission to open the file")
    
except Exception as e:
    print(f"Some error occured! : {e}")