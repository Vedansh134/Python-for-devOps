# use "with" statement in file

file_path = input("Enter your full file path like C:/Users/HP/Desktop/Python/Sample.txt : ")

try:
    with open(f"{file_path}","r") as f:
        content = f.read()
        print(f"File content\n\t {content}")
        print(f"File mode : {f.mode}")

except FileNotFoundError:
    print("File not exist that users want")

finally:
    f.close()
    print(f"Is File Closed? {f.closed}")