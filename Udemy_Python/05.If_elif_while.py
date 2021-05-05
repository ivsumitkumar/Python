import random

r = random.randint(1, 50)
print("Guess the number")

while True:
    x = int(input())
    if x > r:
        print("Wrong guess, try a smaller number.")
    elif x < r:
        print("Wrong guess, try a greater number.")
    else:
        print("Congrats, you've guessed the number.")
        break
