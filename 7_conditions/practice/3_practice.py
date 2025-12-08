# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

comment = "Hello user, Hi I getting your number from our website I have a exiciting offer for you! If you subscribe this channel you Make a lot of money and if buy now so you extra win and if you click this get a extra suprise"

spam = ["Make a lot of money","buy now","subscribe this","click this"]

def check_spam():
    # Conver comment in lower case
    comment_lower = comment.lower()

    # Loop through each individual keyword in the list
    for keyword in spam:
        if keyword.lower() in comment_lower:
            print(f"This comment is probably a spam! Detected keyword : {keyword}")
        return  # Stop checking and exit the function as soon as one is found

    # If loop run without finding a error so print ths msg is clean
    print(f"This message is ok. Not a spam!")

check_spam()