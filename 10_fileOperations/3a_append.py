file_path = "xample.txt"
contend_to_append = "\n This content is in appending way twice"

try:
    with open(file_path,"a") as file:
        file.write(contend_to_append)

        print(f"File is closed or not ? : {file.closed}")

    print(f"Check file mode : {file.mode}")
    print(f"Content successfully appending to : {file_path}")

except Exception as e:
    print(f"Error occurs when appending to file {e}")
