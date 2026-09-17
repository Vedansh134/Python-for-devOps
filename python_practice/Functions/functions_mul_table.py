#
# ===============================================================================
#
#
# Program to print multiplication table of n using for loops in forward order.
#
# 1. Take a number from the user. 
# 2. If the user does not provide a number, use the # default parameter. 
# 3. Put the multiplication table inside a function.
# 4. Use if-else for basic validation. 
# 5. Later, we will add error handling. 
#
# -------------------------------------------------------------------------------


def cal_mul_tab(no=34):
    
    if type(no) == int and no >= 1:
        for num in range(1,11):
            print(f"{no} * {num} = {num*no}")
    else:
        print("Please enter the positive whole integer number greater than or equal to 1")
        

# Error handling using try-except
try:
    user_input = input("Enter the number for printing the multiplication table (Press Enter for default): ").strip()
    
    if user_input == "":
        print("User did not enter any value.\nUse default parameter(n=30).")
        cal_mul_tab()
    else:
        cal_mul_tab(int(user_input))
        
except ValueError:
    print("Invalid Value! Please enter the valid integer value")
    
except Exception as e:
    print(f"An unexpected error occured : {e}")

else:
    print("Exceute if try block is successful")
    
finally:
    print("Execute regardless of error")