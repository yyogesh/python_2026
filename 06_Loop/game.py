import random


secret = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 10: "))

while True:

    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")




