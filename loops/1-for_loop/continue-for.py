# continue keyword in for loop

choice_no = int(input("Enter your number : "))

for num in range(1,40):
    if num == choice_no:
        print(f"no is {num} is found")
        continue

    print(f"All numbers : {num}")

print("Loop finished.")
