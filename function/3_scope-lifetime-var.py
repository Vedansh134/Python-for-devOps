# Various scope in python

global_var = 24

def outer_function():
    local_var1 = "local-scope"

    def inner_function():
        local_var2 = "local-scope-inside another function"
        print(local_var1) # print
        print(local_var2) # print (local scope)
        print(global_var) # print (global scope)

    inner_function()
    print(local_var1)
    # print(local_var2) # gives an error "not defined"

outer_function()

print("if print functional scope variable so gives a error")
print("Because they have functional scope")


