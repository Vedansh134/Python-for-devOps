# Reverse method in list
# Used : To reverse the elements of list

mixed_list = [2,"devOps",True,"",78,"cloud",0]

mixed_list.reverse()
print(mixed_list)

rev_string = mixed_list[::-1]
print("Using list slicing",rev_string) # [0, 'cloud', 78, '', True, 'devOps', 2]
