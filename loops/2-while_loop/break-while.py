# The break statement immediately terminates the current loop entirely, skipping any remaining code in the loop and moving execution to the next statement after the loop block.

count = int(input("Enter number : "))

while count <= 30:
    print(f"The count is {count}")
    if count == 4:
        print(f"found target number {count}")
        break
    count = count + 1

print("outside the loop")