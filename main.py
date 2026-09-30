import random

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")

number = random.randint(1, 100)
attempts = 0

print("I have selected a number from 1 to 100.")
print("Try to guess the number!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations!")
        print("You guessed the correct number!")
        print("The number was:", number)
        print("Number of attempts:", attempts)
        break

print("================================")
print("        GAME OVER")
print("================================")
