#
# ================== function with default parameters ================
#
#
# Program to find the sum of first n natural numbers using while loop.
#
# 1. Take a number from the user. 
# 2. If the user does not provide a number, use the # default parameter. 
# 3. Put the sum calculation inside a function.
# 4. Use if-else for basic validation. 
# 5. Later, we will add error handling. 
#
# ------------------------------------------------------------


def cal_sum(no=30):
    
    # Check whether the no is positive integer
    if type(no) == int and no > 0:
        print("Number is interger , Now calulating the sum...")
        
        # Variable is used to store the total sum
        sum = 0
        for n in range(1,no+1):
            sum = sum + n
            print(f"Sum of till number {n} : {sum}")
            
        # Return the final calculated sum.
        return sum
    
    else:
        # If validation is failed, user enter wrong no.
        print("Please provide a positive integer.")
        return 0
    
# -------------- Take input from user -----------------
user_input = input(
    "Enter the number you want to calculate the sum up to "
    "(Press enter for default is 30):"
)


if user_input == "":
    print("User not enter any value, python use default value")
    # User pressed Enter without providing a number. 
    # Therefore, call the function without an argument. 
    # Python will automatically use the default value : no = 30
    result = cal_sum()
    
else:
    print("User provided a no")
    result = cal_sum(int(user_input))
    

# Display the final result
print(f"Final sum : {result}")
    