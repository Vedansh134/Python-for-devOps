# Practice different methods in string in python

# ================================================================
# ---- concatenation
# ---- Combining two or more strings together using the + operator.

str1 = "hello"
str2 = "WorLD"

concat = str1 + " " + str2
print(f"Concat string : {concat}")


# ================================================================
# ---- lower and upper case
# ---- To make lower and upper case

print(str1.upper())
print(str2.lower()) 


# =================================================================
# ---- slicing
# ---- To make a substring

str = "I love you"
substring = str[2:5]
print(substring)


# ===============================================================================
# ---- split
# ---- Splits the string into a list of substrings based on a specified separator.

str4 = "aws,azure,gcp"
split1 = str4.split(",")
print(f"spliting : {split1}")

split2 = str4.split(":")
print(split2)


# ============================================
# ---- replace
# ---- replace a substring with another

str5 = "Cloud computing and devops"
replace = str5.replace("computing","engineer")

print(f"replace str : {replace}")


# ============================================
# ---- strip
# ---- Removes leading and trailing whitespace.

space = "      my name is vedansh      "
print(space.strip())


# =====================================================================
# ---- join
# ---- Joins elements of an iterable (like a list) into a single string.

tech = ["aws","azure","gcp","docker","kubernetes"]

joined = ", ".join(tech)
print(joined)

# joined.split(" | ")
# print(joined)

# =====================================================================
# ---- find
# ---- Returns the lowest index of the substring if found, otherwise -1.

techi = "There are different tech stack like frontend, backend, iot, blockchain, ai & ml"
fnd = techi.find("ml")
print(fnd) # return index value : 77