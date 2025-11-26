# break keyword in for loop

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        print(f"fruit : {fruit} are found")
        print("Now breaking the loop !!")
        break

        # below print is not work after break keyword
        print(f"{fruit}")

# This print is outside the loop
print("loop finished!")

