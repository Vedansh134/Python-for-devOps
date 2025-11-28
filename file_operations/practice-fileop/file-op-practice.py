File_path = "C:/Users/HP/Desktop/Python/git/Python-for-devOps/file_operations/error.txt"
ERROR = "ERROR"

def check_error():
    try:
        with open(f"{File_path}","r") as f:
            lines = f.readlines()

        with open(f"{File_path}","a+") as file:
            for line in lines:
                if ERROR in line:
                    print(f"Containing some error :  {line.strip()} ")
                else:
                    print("No error")

        with open(f"{File_path}","a") as w:
            w.write("\n2023-09-02T12:00:12Z ERROR Application crashed unexpectedly.\n")

        f.close()
        print(f"Is file closed ? {f.closed}")

    except FileNotFoundError:
        print("File may not be exist")


check_error()
