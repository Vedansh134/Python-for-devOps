#
# ======================== list practice in python ========================
mixed_list = [0,1,True,"done",4.5,2,2,2]
#

# Reverse a list
mixed_list.reverse()
print(f"Reverse : {mixed_list}")


# Appending in list
mixed_list.append("Appending")
print(f"Appending : {mixed_list}")


# Insert : To insert an element at particular index value
mixed_list.insert(3,8)
mixed_list.insert(2,False)
mixed_list.insert(5,"string")

print(f"Updated list : {mixed_list}")
print(f"Updated reverse list : {mixed_list[::-1]}")


# Pop : use for removing the element at particular index
print(f"Element at 4th position : {mixed_list[4]}")
mixed_list.pop(4)
print(f"After Removing 4th element : {mixed_list}")


# Remove : To remove the particular element
mixed_list.remove(4.5)
print(f"{mixed_list}")


# Extend : extend the list
mixed_list.extend([1000,""," "])
print(f"After the extending the list : {mixed_list}")


# Length
print(f"Length of list : {len(mixed_list)}")


# Index : find element indexing position
print(mixed_list.index("done"))


# Count : To count the particular element in the list
print(f"No of element found : {mixed_list.count(2)} times")