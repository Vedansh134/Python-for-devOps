# 7. Write a program to find out whether a given post is talking about “Vedansh” or not.

post = "Hello Vedansh how are you! I hope you are fine."
name = "vedansh"

def check_word(post_text, target_name):
    cname = target_name.lower()
    cpost = post_text.lower()

    if cname in cpost:
        print(f"This post is talk about : {target_name}")

    else:
        print(f"This given post is not talk about : VEDANSH & is talk about : {target_name}")

check_word(post,name)
