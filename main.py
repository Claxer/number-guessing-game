import random

best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

games_played = 0
games_won = 0
total_attempts = 0
win_streak = 0
longest_streak = 0


while True:
    print("\n================================")
    print("      NUMBER GUESSING GAME")
    print("================================")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 10 attempts)")
    print("4. Statistics")
    print("5. Exit")
    print("================================")

    choice = input("Choose an option: ")

    # ==============================
    # STATISTICS
    # ==============================

    if choice == "4":
        print("\n================================")
        print("          STATISTICS")
        print("================================")

        print("Games played:", games_played)
        print("Games won:", games_won)

        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print("Win rate:", round(win_rate, 2), "%")
        else:
            print("Win rate: 0%")

        print("Current win streak:", win_streak)
        print("Longest win streak:", longest_streak)

        if total_attempts > 0:
            average_attempts = total_attempts / games_won if games_won > 0 else 0
            print("Average attempts per win:", round(average_attempts, 2))
        else:
            print("Average attempts per win: 0")

        print("\nBest Scores")
        print("--------------------------------")
        print("Easy:", best_scores["Easy"])
        print("Medium:", best_scores["Medium"])
        print("Hard:", best_scores["Hard"])
        print("================================")

        input("\nPress Enter to return to the menu...")
        continue

    # ==============================
    # DIFFICULTY SELECTION
    # ==============================

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

    elif choice == "5":
        print("\nThank you for playing!")
        print("================================")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
        continue

    # ==============================
    # GAME SETUP
    # ==============================

    number = random.randint(1, maximum)

    attempts = 0
    score = 100
    guess_history = []
    previous_difference = None

    games_played += 1

    print("\n================================")
    print("         GAME START")
    print("================================")
    print("Difficulty:", difficulty)
    print("I have selected a number from 1 to", maximum)
    print("You have", max_attempts, "attempts.")
    print("Try to guess the number!")
    print("================================")

    # ==============================
    # GUESSING LOOP
    # ==============================

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check range
        if guess < 1 or guess > maximum:
            print("Please enter a number between 1 and", maximum)
            continue

        # Check duplicate guess
        if guess in guess_history:
            print("You already guessed that number.")
            continue

        attempts += 1
        total_attempts += 1

        guess_history.append(guess)

        # Calculate distance from correct number
        difference = abs(number - guess)

        # ==============================
        # CORRECT GUESS
        # ==============================

        if guess == number:

            print("\n================================")
            print("        CONGRATULATIONS!")
            print("================================")
            print("You guessed the correct number!")
            print("The number was:", number)
            print("Number of attempts:", attempts)

            # Calculate score
            score = 100 - ((attempts - 1) * 10)

            # Difficulty bonus
            if difficulty == "Easy":
                score += 0

            elif difficulty == "Medium":
                score += 20

            elif difficulty == "Hard":
                score += 40

            # Minimum score
            if score < 10:
                score = 10

            print("Your score:", score)

            # Update win statistics
            games_won += 1
            win_streak += 1

            if win_streak > longest_streak:
                longest_streak = win_streak

            # Best score
            if best_scores[difficulty] is None:
                best_scores[difficulty] = score
                print("NEW BEST SCORE!")

            elif score > best_scores[difficulty]:
                best_scores[difficulty] = score
                print("NEW BEST SCORE!")

            print("Best", difficulty, "score:", best_scores[difficulty])

            # Accuracy
            accuracy = (1 / attempts) * 100
            print("Guess accuracy:", round(accuracy, 2), "%")

            # Guess history
            print("\nYour guesses:")
            print(guess_history)

            break

        # ==============================
        # WRONG GUESS
        # ==============================

        elif guess < number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

        # ==============================
        # CLOSENESS HINT
        # ==============================

        if previous_difference is not None:

            if difference < previous_difference:
                print("You are getting CLOSER!")

            elif difference > previous_difference:
                print("You are getting FARTHER!")

            else:
                print("You are the same distance from the number.")

        previous_difference = difference

        # ==============================
        # ATTEMPTS REMAINING
        # ==============================

        print("Attempts remaining:", max_attempts - attempts)

        # ==============================
        # HINT 1 - EVEN OR ODD
        # ==============================

        if attempts == 3:

            if number % 2 == 0:
                print("HINT: The number is EVEN.")

            else:
                print("HINT: The number is ODD.")

        # ==============================
        # HINT 2 - UPPER OR LOWER HALF
        # ==============================

        if attempts == 5 and maximum >= 100:

            if number <= maximum // 2:
                print("HINT: The number is in the LOWER half.")

            else:
                print("HINT: The number is in the UPPER half.")

        # ==============================
        # HINT 3 - NUMBER RANGE
        # ==============================

        if attempts == 7 and maximum >= 100:

            lower_range = max(1, number - 25)
            upper_range = min(maximum, number + 25)

            print("HINT: The number is between",
                  lower_range, "and", upper_range)

    # ==============================
    # GAME OVER
    # ==============================

    else:

        print("\n================================")
        print("          GAME OVER")
        print("================================")
        print("You ran out of attempts.")
        print("The correct number was:", number)
        print("Better luck next time!")

        # Reset streak after losing
        win_streak = 0

        print("\nYour guesses:")
        print(guess_history)

    # ==============================
    # PLAY AGAIN
    # ==============================

    print("\n================================")

    play_again = input(
        "Would you like to play again? (yes/no): "
    ).lower()

    if play_again != "yes":

        print("\n================================")
        print("       FINAL STATISTICS")
        print("================================")

        print("Games played:", games_played)
        print("Games won:", games_won)

        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print("Win rate:", round(win_rate, 2), "%")

        print("Longest win streak:", longest_streak)

        print("\nBest Scores")
        print("--------------------------------")
        print("Easy:", best_scores["Easy"])
        print("Medium:", best_scores["Medium"])
        print("Hard:", best_scores["Hard"])

        print("\nThank you for playing!")
        print("================================")

        break
