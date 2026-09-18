#
# =========================== Write operation in file =======================
#
# - open()   : To open the file
# - write()  : To perform write to the file
# - mode()   : To check the mode of the file
# - closed() : To check the status of the file
#

def write_file():
    f = None  # Initialize to avoid NameError
    
    try:
        # open the file in write mode
        f = open("C:/Users/kumar.vedansh/k8s/Python-for-devOps/python_practice/file_operations/write.txt","w")
        
        # write into the file
        f.write("Write text into the file.\n\tThis operation is perform by vedansh!")
        
        # Show file details
        print(f"File name : {f.name}\n")
        print(f"File status (Is file Closed?) : {f.closed}\n")
        print(f"File mode : {f.mode}")
        
        
    except FileNotFoundError:
        print("Error!, File may not exist.")
        
    except PermissionError:
        print("Error!, You have not enough permission to open the file.")
        
    except Exception as e:
        print(f"Unexpected error! : {e}")
        
    finally:
        # Always closed the file
        if f:
            f.close()
            print(f"Is file Closed Now? : {f.closed}")
            
        # Now read file content
        with open("write.txt","r") as read_file:
            content = read_file.read()
            print(f"File content : \n\t{content}")
    

write_file()