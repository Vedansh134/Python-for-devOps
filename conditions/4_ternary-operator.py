# ternary operator in python is a one-liner conditional statement that evaluates a condition and returns one of two values based on whether the condition is true or false.

# Syntax : value_if_true if condition else value_if_false
#        : <var> = <var> if (condition) else<var2>


food = input("Enter your favourite food : ")
print("spicy") if food == "paneer chilli" or food == "paneer tikka" else print("not spicy")

food = input("Eat which food : ")
eat="YES" if food == "pizza" else "Burger"
print(f"you ate {eat}")

