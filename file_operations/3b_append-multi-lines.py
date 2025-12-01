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

except FileNotFoundError:
    print(f"File is not found!. May be incorrect file name")
except Exception as e:
    print(f"Something went wrong! {e}")