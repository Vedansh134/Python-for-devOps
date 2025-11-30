data = [2,3,4,"error",0]

try:
    total = sum(data)
    print(f"Sum : {total}")
except (ValueError, TypeError) as e:
    print(f"A datatype error occured {e}")
    print("Please ensure all the data elements is integer!")
except Exception as e:
    print(f"Error happens : {e}")