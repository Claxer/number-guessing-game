import random

# ==========================================
# GAME DATA
# ==========================================

best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

best_attempts = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

games_played = 0
games_won = 0
total_attempts = 0
win_streak = 0
longest_streak = 0
total_score = 0
hints_used = 0

game_history = []

achievements = []


# ==========================================
# ACHIEVEMENT SYSTEM
# ==========================================

def unlock_achievement(name):

    if name not in achievements:
        achievements.append(name)
        print("\n*** ACHIEVEMENT UNLOCKED:", name, "***")


# ==========================================
# STATISTICS
# ==========================================

def show_statistics():

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

    if games_won > 0:
        average_attempts = total_attempts / games_won
        average_score = total_score / games_won

        print("Average attempts per win:",
              round(average_attempts, 2))

        print("Average score:",
              round(average_score, 2))

    else:
        print("Average attempts per win: 0")
        print("Average score: 0")

    print("\nBest Scores")
    print("--------------------------------")
    print("Easy:", best_scores["Easy"])
    print("Medium:", best_scores["Medium"])
    print("Hard:", best_scores["Hard"])

    print("\nBest Attempts")
    print("--------------------------------")
    print("Easy:", best_attempts["Easy"])
    print("Medium:", best_attempts["Medium"])
    print("Hard:", best_attempts["Hard"])

    print("\nAchievements")
    print("--------------------------------")

    if len(achievements) == 0:
        print("No achievements yet.")

    else:
        for achievement in achievements:
            print("-", achievement)

    print("================================")

    input("\nPress Enter to return to the menu...")


# ==========================================
# GAME HISTORY
# ==========================================

def show_history():

    print("\n================================")
    print("          GAME HISTORY")
    print("================================")

    if len(game_history) == 0:
        print("No games have been played yet.")

    else:

        for game in game_history:

            print("\nDifficulty:", game["difficulty"])
            print("Result:", game["result"])
            print("Attempts:", game["attempts"])
            print("Score:", game["score"])
            print("Guesses:", game["guesses"])

            print("--------------------------------")

    input("\nPress Enter to return to the menu...")


# ==========================================
# LEADERBOARD
# ==========================================

def show_leaderboard():

    print("\n================================")
    print("          LEADERBOARD")
    print("================================")

    print("\nBEST SCORES")
    print("--------------------------------")

    for difficulty in best_scores:

        score = best_scores[difficulty]

        if score is None:
            print(difficulty + ":", "No score yet")

        else:
            print(difficulty + ":", score)

    print("\nFEWEST ATTEMPTS")
    print("--------------------------------")

    for difficulty in best_attempts:

        attempts = best_attempts[difficulty]

        if attempts is None:
            print(difficulty + ":", "No record yet")

        else:
            print(difficulty + ":", attempts)

    print("================================")

    input("\nPress Enter to return to the menu...")


# ==========================================
# CUSTOM DIFFICULTY
# ==========================================

def custom_game():

    print("\n================================")
    print("        CUSTOM GAME")
    print("================================")

    try:
        maximum = int(input("Enter maximum number: "))
        max_attempts = int(input("Enter number of attempts: "))

    except ValueError:
        print("Please enter valid numbers.")
        return

    if maximum < 10:
        print("Maximum number must be at least 10.")
        return

    if max_attempts < 1:
        print("Attempts must be at least 1.")
        return

    play_game(
        maximum,
        max_attempts,
        "Custom"
    )


# ==========================================
# PLAY GAME FUNCTION
# ==========================================

def play_game(maximum, max_attempts, difficulty):

    global games_played
    global games_won
    global total_attempts
    global win_streak
    global longest_streak
    global total_score
    global hints_used

    number = random.randint(1, maximum)

    attempts = 0
    score = 100

    guess_history = []

    previous_difference = None

    hints_this_game = 0

    games_played += 1

    print("\n================================")
    print("         GAME START")
    print("================================")

    print("Difficulty:", difficulty)
    print("Number range: 1 -", maximum)
    print("Attempts:", max_attempts)

    print("\nType 0 at any time to quit this game.")

    print("================================")

    # ==========================================
    # GUESSING LOOP
    # ==========================================

    while attempts < max_attempts:

        try:

            guess = int(
                input("\nEnter your guess: ")
            )

        except ValueError:

            print("Please enter a valid number.")
            continue

        # ==========================================
        # QUIT CURRENT GAME
        # ==========================================

        if guess == 0:

            print("\nYou left the current game.")

            win_streak = 0

            game_history.append({
                "difficulty": difficulty,
                "result": "Quit",
                "attempts": attempts,
                "score": 0,
                "guesses": guess_history
            })

            return

        # ==========================================
        # RANGE CHECK
        # ==========================================

        if guess < 1 or guess > maximum:

            print(
                "Please enter a number between 1 and",
                maximum
            )

            continue

        # ==========================================
        # DUPLICATE CHECK
        # ==========================================

        if guess in guess_history:

            print("You already guessed that number.")
            continue

        attempts += 1
        total_attempts += 1

        guess_history.append(guess)

        difference = abs(number - guess)

        # ==========================================
        # CORRECT GUESS
        # ==========================================

        if guess == number:

            print("\n================================")
            print("        CONGRATULATIONS!")
            print("================================")

            print("You guessed the correct number!")
            print("The number was:", number)
            print("Attempts:", attempts)

            # ==========================================
            # SCORE CALCULATION
            # ==========================================

            score = 100 - ((attempts - 1) * 10)

            # Difficulty bonus

            if difficulty == "Medium":
                score += 20

            elif difficulty == "Hard":
                score += 40

            elif difficulty == "Custom":
                score += 30

            # Hint penalty

            score -= hints_this_game * 10

            # Win streak bonus

            if win_streak >= 2:
                score += win_streak * 5

            # Minimum score

            if score < 10:
                score = 10

            print("Your score:", score)

            # ==========================================
            # UPDATE STATISTICS
            # ==========================================

            games_won += 1
            total_score += score

            win_streak += 1

            if win_streak > longest_streak:
                longest_streak = win_streak

            # ==========================================
            # ACHIEVEMENTS
            # ==========================================

            if games_won == 1:
                unlock_achievement("First Win")

            if attempts == 1:
                unlock_achievement("Perfect Guess")

            if hints_this_game == 0:
                unlock_achievement("No Hints Used")

            if win_streak == 5:
                unlock_achievement("5 Win Streak")

            # ==========================================
            # BEST SCORE
            # ==========================================

            if difficulty in best_scores:

                if best_scores[difficulty] is None:

                    best_scores[difficulty] = score

                    print("NEW BEST SCORE!")

                elif score > best_scores[difficulty]:

                    best_scores[difficulty] = score

                    print("NEW BEST SCORE!")

                print(
                    "Best",
                    difficulty,
                    "score:",
                    best_scores[difficulty]
                )

            # ==========================================
            # BEST ATTEMPTS
            # ==========================================

            if difficulty in best_attempts:

                if best_attempts[difficulty] is None:

                    best_attempts[difficulty] = attempts

                elif attempts < best_attempts[difficulty]:

                    best_attempts[difficulty] = attempts

                    print("NEW BEST ATTEMPT RECORD!")

            # ==========================================
            # ACCURACY
            # ==========================================

            accuracy = (1 / attempts) * 100

            print(
                "Guess accuracy:",
                round(accuracy, 2),
                "%"
            )

            # ==========================================
            # GUESS ANALYSIS
            # ==========================================

            print("\nGuess Analysis")

            print("Lowest guess:",
                  min(guess_history))

            print("Highest guess:",
                  max(guess_history))

            average_guess = (
                sum(guess_history) /
                len(guess_history)
            )

            print(
                "Average guess:",
                round(average_guess, 2)
            )

            print("\nYour guesses:")
            print(guess_history)

            # ==========================================
            # SAVE GAME HISTORY
            # ==========================================

            game_history.append({
                "difficulty": difficulty,
                "result": "Won",
                "attempts": attempts,
                "score": score,
                "guesses": guess_history.copy()
            })

            break

        # ==========================================
        # WRONG GUESS
        # ==========================================

        elif guess < number:

            print("Too low!")

        else:

            print("Too high!")

        # ==========================================
        # HOT / COLD SYSTEM
        # ==========================================

        if difference <= 5:

            print("🔥 VERY HOT! You are extremely close.")

        elif difference <= 15:

            print("Hot! You are close.")

        elif difference <= 30:

            print("Warm. You are getting closer.")

        else:

            print("Cold. You are far from the number.")

        # ==========================================
        # CLOSER / FARTHER SYSTEM
        # ==========================================

        if previous_difference is not None:

            if difference < previous_difference:

                print("You are getting CLOSER!")

            elif difference > previous_difference:

                print("You are getting FARTHER!")

            else:

                print(
                    "You are the same distance "
                    "from the number."
                )

        previous_difference = difference

        # ==========================================
        # ATTEMPTS REMAINING
        # ==========================================

        print(
            "Attempts remaining:",
            max_attempts - attempts
        )

        # ==========================================
        # HINT OPTION
        # ==========================================

        if attempts >= 2:

            hint_choice = input(
                "Would you like a hint? (yes/no): "
            ).lower()

            if hint_choice == "yes":

                hints_this_game += 1
                hints_used += 1

                print("\nHINT")

                # Random hint

                hint_type = random.randint(1, 4)

                if hint_type == 1:

                    if number % 2 == 0:
                        print(
                            "The number is EVEN."
                        )
                    else:
                        print(
                            "The number is ODD."
                        )

                elif hint_type == 2:

                    if number <= maximum // 2:
                        print(
                            "The number is in the "
                            "LOWER half."
                        )
                    else:
                        print(
                            "The number is in the "
                            "UPPER half."
                        )

                elif hint_type == 3:

                    lower_range = max(
                        1,
                        number - 20
                    )

                    upper_range = min(
                        maximum,
                        number + 20
                    )

                    print(
                        "The number is between",
                        lower_range,
                        "and",
                        upper_range
                    )

                else:

                    if number > guess:

                        print(
                            "The number is higher "
                            "than your guess."
                        )

                    else:

                        print(
                            "The number is lower "
                            "than your guess."
                        )

                print(
                    "Hint penalty: -10 points"
                )

        # ==========================================
        # EXTRA HINTS
        # ==========================================

        if attempts == 3:

            if number % 2 == 0:

                print(
                    "EXTRA HINT: The number is EVEN."
                )

            else:

                print(
                    "EXTRA HINT: The number is ODD."
                )

        if attempts == 5 and maximum >= 100:

            if number <= maximum // 2:

                print(
                    "EXTRA HINT: The number is "
                    "in the LOWER half."
                )

            else:

                print(
                    "EXTRA HINT: The number is "
                    "in the UPPER half."
                )

    # ==========================================
    # GAME OVER
    # ==========================================

    else:

        print("\n================================")
        print("          GAME OVER")
        print("================================")

        print("You ran out of attempts.")
        print("The correct number was:", number)

        print("\nBetter luck next time!")

        print("\nYour guesses:")
        print(guess_history)

        win_streak = 0

        game_history.append({
            "difficulty": difficulty,
            "result": "Lost",
            "attempts": attempts,
            "score": 0,
            "guesses": guess_history.copy()
        })


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n================================")
    print("      NUMBER GUESSING GAME")
    print("================================")

    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 10 attempts)")
    print("4. Custom Game")
    print("5. Statistics")
    print("6. Game History")
    print("7. Leaderboard")
    print("8. Exit")

    print("================================")

    choice = input("Choose an option: ")

    # ==========================================
    # EASY
    # ==========================================

    if choice == "1":

        play_game(
            50,
            10,
            "Easy"
        )

    # ==========================================
    # MEDIUM
    # ==========================================

    elif choice == "2":

        play_game(
            100,
            7,
            "Medium"
        )

    # ==========================================
    # HARD
    # ==========================================

    elif choice == "3":

        play_game(
            500,
            10,
            "Hard"
        )

    # ==========================================
    # CUSTOM
    # ==========================================

    elif choice == "4":

        custom_game()

    # ==========================================
    # STATISTICS
    # ==========================================

    elif choice == "5":

        show_statistics()

    # ==========================================
    # HISTORY
    # ==========================================

    elif choice == "6":

        show_history()

    # ==========================================
    # LEADERBOARD
    # ==========================================

    elif choice == "7":

        show_leaderboard()

    # ==========================================
    # EXIT
    # ==========================================

    elif choice == "8":

        print("\n================================")
        print("       FINAL STATISTICS")
        print("================================")

        print("Games played:", games_played)
        print("Games won:", games_won)

        if games_played > 0:

            win_rate = (
                games_won /
                games_played
            ) * 100

            print(
                "Win rate:",
                round(win_rate, 2),
                "%"
            )

        print(
            "Longest win streak:",
            longest_streak
        )

        print(
            "Total hints used:",
            hints_used
        )

        print("\nBest Scores")
        print("--------------------------------")

        print(
            "Easy:",
            best_scores["Easy"]
        )

        print(
            "Medium:",
            best_scores["Medium"]
        )

        print(
            "Hard:",
            best_scores["Hard"]
        )

        print("\nAchievements")

        if len(achievements) == 0:

            print("None")

        else:

            for achievement in achievements:

                print("-", achievement)

        print("\nThank you for playing!")
        print("================================")

        break

    # ==========================================
    # INVALID CHOICE
    # ==========================================

    else:

        print(
            "Invalid choice. "
            "Please select 1-8."
        )
