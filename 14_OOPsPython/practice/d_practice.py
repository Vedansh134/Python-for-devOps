# In this code we practice of OOPs concept in python

class Shopping:
    def __init__(self, mall):
        self.mall = mall
        self.items = []

    def add_to_cart(self, item1):
        self.items.append(item1)

# 1. Create a instance of an shopping object
shop1 = Shopping("Shopprix")
print(f"Welcome! We are shopping at : {shop1.mall}")

# 2. Add items using the method
shop1.add_to_cart("Jeans")
shop1.add_to_cart("shirt")

# 3. See the final shopping list of itms in that specific shopping mall object
print(f"You visit {shop1.mall} mall and your cart : {shop1.items}")

# same as above create another shopping mall object
shop2 = Shopping("pacific mall")
print(f"Welcome back! Now you are shopping at {shop2.mall}")

shop2.add_to_cart("T-shirt")
shop2.add_to_cart("Watch")

print(f"You visit {shop2.mall} mall and your cart : {shop2.items}")

