import random

'''
1 for rock
-1 for paper
0 for scissor
'''

youdict = {
    "r" : 1,   # rock
    "p" : -1,  # paper
    "s" : 0    # scissor
}

# Use random function to clet computer to choose random value
computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (r, p, s): ").lower()


if youstr not in youdict:
    print(f"You enter wrong value. Please choose from {list(youdict.keys())}")

else:
    you = youdict[youstr]
    
    if ( computer == you ):
        print("It's tie!")
    
    elif ( computer == -1 and you == 0 ):
        print(f"You win.\n\tYou choose the scissor and cut the paper.")
        
    elif ( computer == -1 and you == 1 ):
        print(f"You loose and computer win.\n\tPaper grab the rock.")
        
    elif ( computer == 0 and you == 1 ):
        print(f"You win.\n\tYou choose the rock and beat the scissor.")
        
    elif ( computer == 0 and you == -1):
        print(f"Computer won the match as it choose scissor.\n\t.Scissor cut the paper!")
    
    elif ( computer == 1 and you == 0):
        print(f"Computer won as it choose rock and you scissor.\n\tRock break the scissor.")
    
    else:
        print(f"Wrong output, PLease choose from the options {youdict}")
    
print("Game complete!")
    
    