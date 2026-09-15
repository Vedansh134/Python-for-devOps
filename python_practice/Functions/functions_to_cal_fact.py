#
# =======================================================================
#
#
# Program to find the sum of first n natural numbers using while loop.
#
# 1. Take a number from the user. 
# 2. If the user does not provide a number, use the # default parameter. 
# 3. Put the factorial calculation inside a function.
# 4. Use if-else for basic validation. 
# 5. Later, we will add error handling. 
#
# ------------------------------------------------------------------------

def cal_fact(no=3):    
    if type(no) == int and no >= 1:
        total = 1
        for fact in range(1, no+1):
            total = total * fact
                
        print(f"Factorial of {no} : {total}")       
    else:
        print("Please enter a positive whole number.")
   
     
# --- Error Handling & Input Section ---
try:
    user_input = input("Enter the no for calculate the factorial (Press Enter for default) : ")
    
    if user_input == " ":
        # take default value
        cal_fact()
    else:
        cal_fact(int(user_input))
except ValueError:
    print("Error: Invalid input! Please enter a valid integer number.")
except Exception as e:
    print(e)
    