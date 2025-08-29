#C:/Users/HP/Desktop/Python/git/Python-for-devOps/file_operations/server.conf

path = input("Enter path of file : ")
key = input("Enter key : ")
value = input("Enter value : ")

def update_server_config(file_path, key, value):
    try:
        with open(file_path,"r") as file:
            lines = file.readlines()

        with open(file_path,"w") as file:
            for line in lines:
                if key in line:
                    file.write(key + "=" + value +"\n")
                else:
                    file.write(line)

    except  FileNotFoundError:
        print("File path is incorrect or may be not exist")
    finally:
        file.close()

#path="C:/Users/HP/Desktop/Python/git/Python-for-devOps/file_operations/server.conf"
#update_server_config(path,"MAX_CONNECTIONS","100")

update_server_config(path,key,value)