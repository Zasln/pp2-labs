import random
print("Hello what is your name?")
name=input()
print("\nWell, " + name +", I am thinking of a number between 1 and 20.","\nTake a guess")
def guess_game(name, cnt=0):
    number=random.randint(1, 20)
    while True:
        guess=int(input())
        if (guess<number):
            print("\nYour guess is too low.\nTake a guess")
            cnt=cnt+1
        if (guess>number):
            print("\nYour guess is too high.\nTake a guess")
            cnt=cnt+1
        if (guess==number):
            print("\nGood job, "+name+"! You guessed my nymber in "+str(cnt+1)+" guesses!")
            break
guess_game(name)