# C:/Users/HP/Desktop/Python/Sample.txt
file_path = input("enter a file path for write operation : ")

try:
    with open(f"{file_path}","w") as w:
        # Write a string to the file
        w.write("you are nice!!")
        print(f"file mode : {w.mode}")

except FileNotFoundError:
    print("File not found may be you give incorrect path")
except PermissionError:
    print("you have no permission to write into it")

finally:
    w.close()
    print(f"Is file closed? {w}")