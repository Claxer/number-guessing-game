import random

best_score = None

while True:
    print("\n================================")
    print("      NUMBER GUESSING GAME")
    print("================================")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 10 attempts)")
    print("4. Exit")
    print("================================")

    choice = input("Choose difficulty: ")

    if choice == "1":
        maximum = 50
        max_attempts = 10
        difficulty = "Easy"
    elif choice == "2":
        maximum = 100
        max_attempts = 7
        difficulty = "Medium"
    elif choice == "3":
        maximum = 500
        max_attempts = 10
        difficulty = "Hard"
    elif choice == "4":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        continue

    number = random.randint(1, maximum)
    attempts = 0
    score = 100

    print("\n================================")
    print("         GAME START")
    print("================================")
    print("Difficulty:", difficulty)
    print("I have selected a number from 1 to", maximum)
    print("You have", max_attempts, "attempts.")
    print("Try to guess the number!")

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > maximum:
            print("Please enter a number between 1 and", maximum)
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("\n================================")
            print("        CONGRATULATIONS!")
            print("================================")
            print("You guessed the correct number!")
            print("The number was:", number)
            print("Number of attempts:", attempts)

            score = score - ((attempts - 1) * 10)

            if score < 10:
                score = 10

            print("Your score:", score)

            if best_score is None or score > best_score:
                best_score = score
                print("NEW BEST SCORE!")

            print("Best score:", best_score)

            break

        print("Attempts remaining:", max_attempts - attempts)

        if attempts == 3:
            if number % 2 == 0:
                print("HINT: The number is EVEN.")
            else:
                print("HINT: The number is ODD.")

        if attempts == 5 and maximum >= 100:
            if number <= maximum // 2:
                print("HINT: The number is in the LOWER half.")
            else:
                print("HINT: The number is in the UPPER half.")

    else:
        print("\n================================")
        print("          GAME OVER")
        print("================================")
        print("You ran out of attempts.")
        print("The correct number was:", number)
        print("Better luck next time!")

    print("\n================================")
    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        print("================================")
        break
