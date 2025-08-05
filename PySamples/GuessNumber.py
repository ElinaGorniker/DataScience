import random

def guessNumber():
    a = random.randint(1,101)
    n = 0
    while n != a:
        print("Your number:")
        n = int(input())
        if n > a:
            print("Too much, please try again")
            continue
        elif n < a:
            print("Too low, please try again")
            continue
        else:
            print("Congratulates! You win!")
            break
guessNumber()