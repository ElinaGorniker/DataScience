import random
import math


def is_valid(num):
  if 1 <= int(num) <= 100:
      return True
  else:
      return False

def guess_number(a):
    print("Welcome to the number guessing game!")
    n = 0
    count = 0
    while True:
        print("Your number from 1 to 100:")
        n = int(input())
        if is_valid(n):
            if n > a:
                count += 1
                print("Too much, please try again")
                continue
            elif n < a:
                count += 1
                print("Too low, please try again")
                continue
            else:
                print("Congratulates! You win!")
                break
        else:
            print("Or maybe let's enter an integer from 1 to 100?")
            continue
    attemts(a)
    print ("Your attempts number: ", count)
    print("Thank you for playing the number guessing game. See you again...")
def attemts(a):
    count = math.ceil(math.log2(a+1))
    print("The minimum number of attempts required: ", count)

a = random.randint(1,101)



guess_number(a)
