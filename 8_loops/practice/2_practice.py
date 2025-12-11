# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["vedansh", "Saraswati", "devansh", "lakshmi", "radha", "sakshi"]

start_with_s = []
start_notwith_s = []

def greet_s(name_list):

    print("--- Greetings for names starting with 'S' ---")

    for name in name_list:
        if name.lower().startswith("s"):
            print(f"Hello {name}")
            start_with_s.append(name)
        else:
            print(f"Hi {name}")
            start_notwith_s.append(name)

    print(f"\nName start with S ------ : {start_with_s}")
    print(f"\nName which is not start with S ------- : {start_notwith_s}")


greet_s(l)



