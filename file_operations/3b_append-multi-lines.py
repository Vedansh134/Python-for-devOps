# Appending Multiple Lines
# To append several lines at once, you can use the writelines() method, which accepts an iterable (like a list of strings). Remember to add newline characters (\n) to position each item on a new line

file_path = "xample.txt"
lines_to_append = [
    "\nline1"
    "\nline2"
    "\nline3"
]

try:
    with open(file_path,"a") as file:
        file.writelines(lines_to_append)

        print(f"Print successfully to file : {file_path}")
        print(f"Check file mode : {file.mode}")
        print(f"Check file open or not : {file.closed}") # false

    print(f"Now check file is closed or not ? : {file.closed}") # true

except FileNotFoundError:
    print(f"File is not found!. May be incorrect file name")
except Exception as e:
    print(f"Something went wrong! {e}")