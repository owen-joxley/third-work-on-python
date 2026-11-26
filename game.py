import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("guess 1-10: "))
    if guess < secret:
        print("low!")
    elif guess > secret:
        print("high!")
    else:
        print("correct!")