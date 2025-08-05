import random

answers = [
    "Without a doubt",
    "It is certain",
    "You may rely on it",
    "Yes – definitely",
    "Signs point to yes",
    "Outlook good",
    "Most likely",
    "As I see it, yes",
    "Yes",
    "All will be revealed in time...",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "The future is unclear",
    "Concentrate and ask again",
    "Don't count on it",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "The stars say no"
]

yes =  ["yes", "ye", "y"]
no =  ["no", "nope", "n"]
def fate():
    print("Hello World, I am a magic ball, and I know the answer to any of your questions.")
    print("What's your name?")
    name = input()
    print("Hi, ", name)
    while True:
        print("Try me! Your question ")
        input()
        print(random.choice(answers))
        print("Do you have another question? Yes or No?")
        flag = input().lower()
        if flag in yes:
            continue
        elif flag in no:
            print("Come back if you want to ask me again")
            break
        else:
            print("I dont't understand. Try again")

fate()