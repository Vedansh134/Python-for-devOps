import random

try: 
    # use random function to create the random values
    #secret = random.randint(1,100)
    attempts = 0
    
    # check the random value generate
    # print(f"Random value : {secret}")
    
    print("Guess the number between the 1 and 100!")
    
    while True:
        secret = random.randint(1,100)
        guess = int(input("Enter your guess number : "))
        
        if guess > secret:
            print("You guess higher value")
            print(f"You guess : {guess} and random : {secret}")
            
        elif guess < secret:
            print("You guess the lower value")
            print(f"You guess {guess} and random : {secret}")
            
        else:
            print("Rare!, Value match")
            print(f"You guess value : {guess} and random : {secret}")
            break
            
    print("Guess work copmplete!")
    
except KeyboardInterrupt:
    print("User intrupted the keyword, Please reagain exceute the code!")
    
except Exception as e:
    print(f"Some error occured! : {e}")
