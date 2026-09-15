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


# suggest commenting
print(name("from return"))

# suggest commenting 
result = name("unknown")
print(result)
