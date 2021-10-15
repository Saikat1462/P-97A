import random

num = random.randint(1, 10)
chances=0

print("guess a number between 1 and 10: ")

while chances < 5:
    guess = int(input("Enter Your guess:"))

    if guess == num:
        print("congratulations! you won!")
        break
    elif guess < num:
        print("Guess is too low go with some higher number than ",guess)
    else:
        print("Guess was too high!! go with lower than ",guess)
    chances +=1
if not chances < 5:
    print("You Lose!! and the number is ",num)