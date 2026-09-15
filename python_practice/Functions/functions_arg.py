#
# ================= function in python ================
#

# ======================================
# functions with arguments and returns
# ======================================

def name(name):
    fn = "hello" + " "+ name
    #print(f"{fn}")
    
    # Return the result to the caller 
    # The function itself does NOT print anything.
    return fn
    

# normal call the function if it contain print without return
# name("vedansh")
# name("devansh")


# The function returns "from return" and print() displays the returned value.
print(name("from return"))


# Store the returned value
# Store the value returned by the function in 'result'. and display the value stored in 'result'
result = name("unknown")
print(result)
