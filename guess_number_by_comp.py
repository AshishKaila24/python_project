import random

a = 10
num = int(input(f"Please input a number between 1 to {a}"))

def guess_number(x):

    guess = 0
    tr = 1
    p = 1
    q = x

    while guess != num:
       
        guess = random.randint(p,q)
        print(guess)
        if guess < num:
            p = guess + 1
            tr += 1

        elif guess>num:
            q = guess-1
            tr += 1
        
    
    print(f"congrats you win. after {tr} round")

    
guess_number(a)