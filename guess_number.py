import random

def guess_number(a):
    ran_num = random.randint(1,a+1)
    guess = 0
    while guess != ran_num:
        guess = int(input(f"Guess a number between 1 to {a} : "))
        if guess < ran_num:
            print("Numbre is too low")
        elif guess > ran_num:
            print("Numbre is too high")

    print("congrats you win!!")


guess_number(10)
