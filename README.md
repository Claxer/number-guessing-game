# Number Guessing Game

A simple **Python-based Number Guessing Game** that challenges the player to guess a randomly generated number within a selected difficulty level.

The player can choose between **Easy, Medium, and Hard** difficulty levels. Each difficulty has a different number range and number of attempts. The game provides hints by telling the player if their guess is **too high** or **too low**, along with additional hints that help narrow down the possible number.

The game also includes a **score system, separate best scores, guess history, duplicate guess detection, accuracy tracking, win streaks, difficulty bonuses, statistics, input validation, limited attempts, and a play-again option**.

This project was created as a beginner-friendly Python project to practice **variables, user input, conditional statements, loops, lists, dictionaries, exception handling, the random module, calculations, and basic game logic**.

## Features

* Three difficulty levels
* Easy mode with numbers from 1 to 50
* Medium mode with numbers from 1 to 100
* Hard mode with numbers from 1 to 500
* Different attempt limits for each difficulty
* Randomly generates a secret number
* Allows the player to enter guesses
* Checks whether the guess is too high or too low
* Shows the number of attempts remaining
* Provides additional hints
* Gives an even or odd hint after several attempts
* Gives a lower-half or upper-half hint on larger difficulties
* Tells the player if they are getting closer or farther from the number
* Stores the player's guess history
* Prevents duplicate guesses
* Score system starting at 100 points
* Difficulty-based score bonuses
* Separate best scores for Easy, Medium, and Hard
* Win streak tracking
* Longest win streak tracking
* Games played counter
* Games won counter
* Win rate calculation
* Average attempts per win
* Guess accuracy calculation
* Statistics menu
* Final statistics when exiting
* Input validation
* Prevents invalid numbers from crashing the program
* Limited number of attempts
* Play Again option
* Exit option
* Simple terminal-based interface
* Beginner-friendly Python code

## Difficulty Levels

The game provides three difficulty levels:

| Difficulty | Number Range | Attempts | Score Bonus |
| ---------- | -----------: | -------: | ----------: |
| Easy       |         1-50 |       10 |          +0 |
| Medium     |        1-100 |        7 |         +20 |
| Hard       |        1-500 |       10 |         +40 |

The player can also select **Statistics** to view their game records or **Exit** to close the program.

## Main Menu

When the program starts, the player is shown the main menu.

```text
================================
      NUMBER GUESSING GAME
================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Statistics
5. Exit
================================
```

The player can select a difficulty, view statistics, or exit the game.

## How It Works

The program first displays the main menu and waits for the player's choice.

After a difficulty is selected, the program sets the maximum number, number of attempts, and difficulty name.

A random number is then generated using the selected number range.

The player enters guesses until they either guess the correct number or use all available attempts.

```text
Main Menu
    |
    v
Choose Difficulty
    |
    +---- Statistics ----> Display Statistics
    |
    +---- Exit ----------> End Program
    |
    v
Set Difficulty
    |
    v
Generate Random Number
    |
    v
Enter Guess
    |
    v
Validate Input
    |
    +---- Invalid -------> Try Again
    |
    +---- Duplicate -----> Try Again
    |
    +---- Too Low -------> Give Hint
    |
    +---- Too High ------> Give Hint
    |
    +---- Correct --------> Calculate Score
                              |
                              v
                         Update Statistics
                              |
                              v
                         Display Results
                              |
                              v
                          Play Again?
                              |
                       +------+------+
                       |             |
                      Yes            No
                       |             |
                       v             v
                  Main Menu       Exit
```

The game continues until the player guesses the correct number or runs out of attempts.

## Example

```text
================================
      NUMBER GUESSING GAME
================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Statistics
5. Exit
================================

Choose an option: 2

================================
         GAME START
================================
Difficulty: Medium
I have selected a number from 1 to 100
You have 7 attempts.
Try to guess the number!
================================

Enter your guess: 50
Too low! Try again.
Attempts remaining: 6

Enter your guess: 75
Too high! Try again.
You are getting FARTHER!
Attempts remaining: 5

Enter your guess: 60
Too low! Try again.
You are getting CLOSER!
Attempts remaining: 4

HINT: The number is EVEN.

Enter your guess: 64
You guessed the correct number!

The number was: 64
Number of attempts: 4
Your score: 90
```

## Statistics

The game now includes a **Statistics** option in the main menu.

The statistics system keeps track of the player's performance while the program is running.

It displays information such as:

```text
================================
          STATISTICS
================================
Games played: 5
Games won: 4
Win rate: 80.0 %
Current win streak: 2
Longest win streak: 3
Average attempts per win: 3.25

Best Scores
--------------------------------
Easy: 100
Medium: 110
Hard: 130
================================
```

The statistics help the player see their performance across multiple games.

## Games Played

The program counts how many games have been started.

The counter increases whenever the player selects one of the three difficulty levels.

```python
games_played += 1
```

This value is used when calculating the player's win rate.

## Games Won

Whenever the player correctly guesses the secret number, the games won counter increases.

```python
games_won += 1
```

This allows the program to calculate how many games the player has successfully completed.

## Win Rate

The program calculates the player's win rate using the number of games played and games won.

```python
win_rate = (games_won / games_played) * 100
```

For example, if the player wins 4 out of 5 games:

```text
Win rate: 80.0 %
```

## Win Streak

The game tracks consecutive wins.

Every successful game increases the current win streak:

```python
win_streak += 1
```

If the player loses a game, the current streak is reset:

```python
win_streak = 0
```

The program also keeps track of the longest streak achieved during the current session.

```python
if win_streak > longest_streak:
    longest_streak = win_streak
```

## Best Scores

The program now stores a separate best score for each difficulty.

```python
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

This allows the player to have different records for each difficulty.

For example:

```text
Best Scores
--------------------------------
Easy: 100
Medium: 110
Hard: 130
```

A new best score is displayed when the player's current score is higher than the previous best score for that difficulty.

## Scoring System

The player starts with a base score of **100 points**.

The score decreases by **10 points for every additional attempt**.

For example:

```text
1 attempt  = 100 points
2 attempts = 90 points
3 attempts = 80 points
4 attempts = 70 points
5 attempts = 60 points
```

The game also provides additional score bonuses depending on the selected difficulty.

```text
Easy   = +0 points
Medium = +20 points
Hard   = +40 points
```

This means the final score is affected by both the number of attempts and the selected difficulty.

The minimum score is **10 points**.

```python
if score < 10:
    score = 10
```

## Guess History

The program stores all valid guesses made by the player in a list.

```python
guess_history = []
```

Each valid guess is added to the list:

```python
guess_history.append(guess)
```

At the end of the game, the player's guesses are displayed.

Example:

```text
Your guesses:
[50, 75, 60, 64]
```

This allows the player to review the numbers they entered during the game.

## Duplicate Guess Detection

The game prevents the player from entering the same valid guess more than once.

Before accepting a guess, the program checks whether the number is already stored in the guess history.

```python
if guess in guess_history:
    print("You already guessed that number.")
    continue
```

If the number was already guessed, the program asks the player to enter another number.

The duplicate guess does not use an attempt.

## Closeness Hint

The game compares the player's current guess with the previous guess.

The program calculates the distance between the guess and the secret number.

```python
difference = abs(number - guess)
```

The current difference is compared with the previous difference.

If the new guess is closer:

```text
You are getting CLOSER!
```

If the new guess is farther:

```text
You are getting FARTHER!
```

This gives the player additional information while guessing.

## Additional Hints

The game provides several hints during the guessing process.

### Even or Odd Hint

After three valid guesses, the program checks whether the secret number is even or odd.

Example:

```text
HINT: The number is EVEN.
```

or:

```text
HINT: The number is ODD.
```

### Lower or Upper Half Hint

For larger number ranges, another hint is provided after five attempts.

The program checks whether the number is located in the lower or upper half of the selected range.

Example:

```text
HINT: The number is in the UPPER half.
```

### Number Range Hint

For larger difficulties, an additional range hint is provided later in the game.

The program creates a smaller range around the secret number.

Example:

```text
HINT: The number is between 120 and 170
```

These hints help the player reduce the number of possible answers.

## Input Validation

The program checks whether the player enters a valid number.

If the player enters text instead of a number, the program displays:

```text
Please enter a valid number.
```

The program uses `try` and `except` to prevent invalid input from crashing the game.

```python
try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Please enter a valid number.")
```

The program also checks whether the number is within the selected range.

For example, if the player chooses Easy mode and enters `100`:

```text
Please enter a number between 1 and 50
```

The invalid input does not use an attempt.

## Attempt System

Each difficulty has a different number of attempts.

The attempt counter starts at zero.

```python
attempts = 0
```

Every valid and unique guess increases the attempt counter.

```python
attempts += 1
```

The game continues while the player still has available attempts.

```python
while attempts < max_attempts:
```

Invalid input and duplicate guesses do not use an attempt.

## Game Over

If the player uses all available attempts without finding the secret number, the game displays a Game Over message.

```text
================================
          GAME OVER
================================
You ran out of attempts.
The correct number was: 347
Better luck next time!
```

The current win streak is also reset after a lost game.

## Accuracy

When the player wins, the program calculates a simple guess accuracy value based on the number of attempts used.

The fewer attempts used, the higher the displayed accuracy.

Example:

```text
Number of attempts: 2
Guess accuracy: 50.0 %
```

This value is displayed as part of the successful game results.

## Play Again

After the game ends, the player can choose whether to play another round.

```text
================================
Would you like to play again? (yes/no):
```

If the player enters:

```text
yes
```

the program returns to the main menu.

If the player enters anything other than `yes`, the program exits and displays the final statistics.

## Final Statistics

When the player chooses to stop playing, the program displays a final statistics summary.

```text
================================
       FINAL STATISTICS
================================
Games played: 5
Games won: 4
Win rate: 80.0 %
Longest win streak: 3

Best Scores
--------------------------------
Easy: 100
Medium: 110
Hard: 130

Thank you for playing!
================================
```

This gives the player a summary of their performance before the program closes.

## Technologies Used

* Python
* Random Module
* Terminal / Command Prompt
* PyCharm or Visual Studio Code

## Python Concepts Used

This project uses several basic Python concepts.

### Variables

Variables are used to store information such as the secret number, maximum number, number of attempts, score, difficulty, and statistics.

```python
number = random.randint(1, maximum)
attempts = 0
score = 100
```

### Dictionary

A dictionary is used to store the best score for each difficulty.

```python
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

Dictionaries allow the program to organize related values using names as keys.

### Lists

A list is used to store the player's guess history.

```python
guess_history = []
```

The `append()` method adds each valid guess to the list.

```python
guess_history.append(guess)
```

The `in` operator is also used to check whether a guess already exists in the list.

### User Input

The `input()` function allows the player to enter menu choices and guesses.

```python
choice = input("Choose an option: ")
guess = int(input("Enter your guess: "))
```

### Conditional Statements

The program uses `if`, `elif`, and `else` to make decisions.

```python
if guess < number:
    print("Too low! Try again.")

elif guess > number:
    print("Too high! Try again.")

else:
    print("Congratulations!")
```

Conditional statements are also used for difficulty selection, hints, score calculation, statistics, and validation.

### While Loop

The `while` loop allows the game to continue while the player still has attempts.

```python
while attempts < max_attempts:
```

Another `while True` loop keeps the main menu running until the player chooses to exit.

```python
while True:
```

### For/Range Concepts

The current version of the project mainly uses `while` loops because the number of attempts changes depending on the selected difficulty.

The project can be expanded later with `for` loops and `range()` for features such as displaying multiple rounds, processing statistics, or generating repeated game elements.

### Random Number Generation

The `random.randint()` function generates the secret number.

```python
number = random.randint(1, maximum)
```

The value of `maximum` changes depending on the selected difficulty.

### Try and Except

The program uses `try` and `except` to handle invalid input.

```python
try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Please enter a valid number.")
```

This prevents the program from stopping when the player enters text instead of a number.

### Score Calculation

The score is calculated based on the number of attempts used.

```python
score = 100 - ((attempts - 1) * 10)
```

Difficulty bonuses are then added depending on the selected mode.

### Absolute Value

The `abs()` function is used to calculate the distance between the player's guess and the secret number.

```python
difference = abs(number - guess)
```

This is used by the closeness hint system.

### Comparison Operators

The program uses comparison operators to determine whether the player's guess is lower, higher, or equal to the secret number.

```python
if guess < number:
elif guess > number:
else:
```

Comparison operators are also used for checking scores, attempts, streaks, and ranges.

### Break Statement

The `break` statement stops the current guessing loop when the player correctly guesses the number.

```python
break
```

It is also used to end the main program loop when the player chooses to exit.

### Continue Statement

The `continue` statement allows the program to skip the current iteration and return to the beginning of the loop.

It is used when the player enters invalid or duplicate input.

```python
continue
```

### Arithmetic Operators

Arithmetic operators are used for score calculations, win rate, average attempts, and other game statistics.

Examples include:

```python
games_won / games_played
```

and:

```python
attempts - 1
```

## Data Stored During the Game

The program stores several values while it is running.

```text
Game Data
│
├── Difficulty
├── Secret Number
├── Maximum Number
├── Maximum Attempts
├── Current Attempts
├── Score
├── Guess History
│
└── Statistics
    ├── Games Played
    ├── Games Won
    ├── Win Rate
    ├── Current Win Streak
    ├── Longest Win Streak
    ├── Average Attempts
    └── Best Scores
```

These values are stored in variables, lists, and dictionaries.

The current version stores the information only while the program is running. Closing the program resets the statistics.

## Project Structure

```text
Number-Guessing-Game/
│
├── main.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check by opening a terminal and running:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Number-Guessing-Game.git
```

### 3. Open the Project

Open the project folder using **PyCharm**, **Visual Studio Code**, or another Python IDE.

### 4. Run the Program

Run:

```bash
python main.py
```

## Future Improvements

Possible features that can be added in future versions:

* Save statistics to a file
* Permanent high scores
* Leaderboard system
* Player name system
* Multiple player support
* Timer system
* Countdown timer
* Multiple rounds
* Total score across multiple games
* Custom number ranges
* Custom attempt limits
* More difficulty levels
* More types of hints
* Sound effects
* Graphical user interface
* Colorful terminal interface
* Database support
* Difficulty statistics
* Persistent win streaks
* Detailed game history
* Export statistics to a file

## Purpose

This project was created for learning and practice while studying Python programming.

It demonstrates how basic Python concepts can be combined to create an interactive terminal-based game.

The project provides practice with **user input, random number generation, variables, lists, dictionaries, loops, conditional statements, exception handling, calculations, score systems, statistics, and basic game logic**.

It also demonstrates how a simple program can be expanded by adding features such as **guess history, duplicate detection, difficulty bonuses, best scores, win streaks, accuracy, and performance statistics**.

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

GitHub: `Claxer`

## License

This project is available for educational and personal use.
