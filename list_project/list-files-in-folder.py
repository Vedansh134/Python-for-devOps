import os

# example -- c:/Users/HP/Desktop/Python - folder
folders = input("Please provide a list of folder names with spaces between like /opt /bin ... : ").split()
for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like folder does'nt exist!!")
        continue
    except PermissionError:
        print("You don't have neccesary rights for access this folder" + folder)
        continue

    print("listing files for the folder -" + folder)

    for file in files:
        print(file)
