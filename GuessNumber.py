import random

secretNum = random.randint(1, 100)
# if you want a condition like guess the number in only 3 chance then you can use these guessCount and guessLimit variables.
# guessCount = 0
# guessLimit = 5

while True:
    guess = int(input("Guess: "))
    # guessCount += 1
    if guess == secretNum:
        print("You Won! :)")
        break
    elif guess < secretNum:
        print("Your number is too small !")
    else:
        print("Your number is too big !")


# print("Sorry, Better Luck next time")
print("------------- Game Over -----------------")
