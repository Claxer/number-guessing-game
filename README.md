# Number Guessing Game

A simple **Python-based Number Guessing Game** that challenges the player to guess a randomly generated number within a selected difficulty level.

The player can choose between **Easy, Medium, Hard, and Custom Game** modes. Each difficulty has a different number range and number of attempts. The game provides hints by telling the player if their guess is **too high, too low, hot, cold, closer, or farther** from the secret number.

The game also includes a **scoring system, best scores, best attempts, guess history, duplicate guess detection, accuracy tracking, win streaks, difficulty bonuses, hint penalties, statistics, achievements, game history, leaderboard, input validation, limited attempts, and a quit-game option**.

This project was created as a beginner-friendly Python project to practice **variables, user input, conditional statements, loops, lists, dictionaries, functions, exception handling, the random module, calculations, and basic game logic**.

---

## Features

* Easy difficulty
* Medium difficulty
* Hard difficulty
* Custom Game mode
* Randomly generated secret number
* Different number ranges
* Different attempt limits
* Player guess input
* Too high and too low feedback
* Hot and cold hints
* Closer and farther hints
* Even or odd hints
* Lower-half or upper-half hints
* Smaller number range hints
* Optional hint system
* Hint score penalties
* Score system
* Difficulty-based score bonuses
* Win streak score bonuses
* Separate best scores
* Best attempts tracking
* Guess history
* Duplicate guess detection
* Guess analysis
* Games played counter
* Games won counter
* Win rate calculation
* Average attempts per win
* Average score
* Current win streak
* Longest win streak
* Total hints used
* Game history
* Leaderboard
* Achievement system
* Perfect Guess achievement
* First Win achievement
* No Hints Used achievement
* 5 Win Streak achievement
* Input validation
* Invalid number protection
* Limited attempts
* Quit current game option
* Statistics menu
* Final statistics
* Terminal-based interface
* Beginner-friendly Python code

---

## Difficulty Levels

The game includes three standard difficulty levels and one custom mode.

| Difficulty | Number Range   | Attempts       | Difficulty Bonus |
| ---------- | -------------- | -------------- | ---------------- |
| Easy       | 1-50           | 10             | +0               |
| Medium     | 1-100          | 7              | +20              |
| Hard       | 1-500          | 10             | +40              |
| Custom     | Player chooses | Player chooses | +30              |

### Easy

The player must guess a number from **1 to 50** with a maximum of **10 attempts**.

### Medium

The player must guess a number from **1 to 100** with a maximum of **7 attempts**.

### Hard

The player must guess a number from **1 to 500** with a maximum of **10 attempts**.

### Custom Game

The player can create their own game by choosing:

* Maximum number
* Number of attempts

For example:

```text
================================
        CUSTOM GAME
================================
Enter maximum number: 1000
Enter number of attempts: 15
```

This allows the player to create a more personalized challenge.

---

## Main Menu

The current version provides the following main menu:

```text
================================
      NUMBER GUESSING GAME
================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Custom Game
5. Statistics
6. Game History
7. Leaderboard
8. Exit
================================
```

The player can choose a standard difficulty, create a custom game, view statistics, view previous games, view the leaderboard, or exit.

---

## How the Game Works

The program starts by displaying the main menu.

The player selects a game mode. The program then determines the number range and maximum attempts.

A secret number is randomly generated using Python's `random` module.

The player enters guesses until they:

1. Guess the correct number
2. Run out of attempts
3. Quit the current game

The program provides different hints and feedback throughout the game.

---

## Game Flow

```text
Main Menu
    |
    v
Choose Option
    |
    +---- Statistics ------> Display Statistics
    |
    +---- Game History ----> Display Game History
    |
    +---- Leaderboard -----> Display Leaderboard
    |
    +---- Exit ------------> End Program
    |
    v
Select Difficulty
    |
    v
Set Number Range
    |
    v
Set Attempt Limit
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
    +---- Invalid ---------> Try Again
    |
    +---- Duplicate -------> Try Again
    |
    +---- 0 ---------------> Quit Game
    |
    v
Check Guess
    |
    +---- Too Low ---------> Give Hint
    |
    +---- Too High --------> Give Hint
    |
    +---- Correct ---------> Calculate Score
                                  |
                                  v
                           Update Statistics
                                  |
                                  v
                           Check Achievements
                                  |
                                  v
                            Save Game History
                                  |
                                  v
                             Show Results
                                  |
                                  v
                              Main Menu
```

---

## Scoring System

The game starts with a base score of **100 points**.

The score decreases by **10 points for every additional attempt**.

```text
1 attempt  = 100 points
2 attempts = 90 points
3 attempts = 80 points
4 attempts = 70 points
5 attempts = 60 points
```

The game also provides difficulty bonuses.

```text
Easy   = +0 points
Medium = +20 points
Hard   = +40 points
Custom = +30 points
```

### Hint Penalty

Using a hint reduces the score by **10 points**.

```text
Hint penalty: -10 points
```

This encourages players to solve the game using fewer hints.

### Win Streak Bonus

Players can also receive additional points based on their current win streak.

The longer the win streak, the greater the possible streak bonus.

### Minimum Score

The game prevents the score from becoming lower than **10 points**.

```python
if score < 10:
    score = 10
```

---

## Hint System

The new version includes an optional hint system.

After making valid guesses, the player can choose whether to request a hint.

```text
Would you like a hint? (yes/no):
```

If the player chooses `yes`, the program randomly selects one of several hint types.

### Even or Odd Hint

The program can tell whether the secret number is even or odd.

```text
HINT
The number is EVEN.
```

or:

```text
HINT
The number is ODD.
```

### Upper or Lower Half

The program can indicate whether the secret number is in the upper or lower half of the number range.

```text
HINT
The number is in the UPPER half.
```

### Number Range Hint

The program can provide a smaller range around the secret number.

```text
HINT
The number is between 120 and 170
```

### Higher or Lower Hint

The program can directly indicate whether the secret number is higher or lower than the player's current guess.

```text
The number is higher than your guess.
```

Every optional hint used during a successful game applies a **10-point score penalty**.

---

## Hot and Cold System

The game now provides a **Hot/Cold system** based on the distance between the player's guess and the secret number.

The program calculates the difference using:

```python
difference = abs(number - guess)
```

Depending on the distance, the player may receive messages such as:

```text
VERY HOT! You are extremely close.
```

```text
Hot! You are close.
```

```text
Warm. You are getting closer.
```

```text
Cold. You are far from the number.
```

This gives the player another way to understand how close their guess is.

---

## Closer and Farther System

The game compares the current guess with the previous guess.

If the new guess is closer to the secret number:

```text
You are getting CLOSER!
```

If the new guess is farther away:

```text
You are getting FARTHER!
```

If both guesses are the same distance from the secret number:

```text
You are the same distance from the number.
```

This feature uses the difference between the guess and the secret number.

---

## Guess History

The program stores all valid guesses in a list.

```python
guess_history = []
```

Every valid guess is added using:

```python
guess_history.append(guess)
```

At the end of the game, the player can see their guesses.

Example:

```text
Your guesses:
[50, 75, 60, 64]
```

This allows the player to review their guessing pattern.

---

## Duplicate Guess Detection

The game prevents the player from entering the same number more than once.

The program checks:

```python
if guess in guess_history:
    print("You already guessed that number.")
```

A duplicate guess does not use an attempt.

This allows the player to continue using new guesses without being unnecessarily penalized.

---

## Quit Current Game

The player can quit the current game by entering:

```text
0
```

Example:

```text
Enter your guess: 0

You left the current game.
```

When the player quits, the game is recorded in the game history as:

```text
Result: Quit
```

The current win streak is also reset.

---

## Guess Analysis

When the player wins, the program analyzes the guesses used during the game.

It displays:

* Lowest guess
* Highest guess
* Average guess

Example:

```text
Guess Analysis
Lowest guess: 50
Highest guess: 75
Average guess: 64.75
```

The program uses Python functions such as:

```python
min(guess_history)
max(guess_history)
sum(guess_history)
```

This gives the player more information about their guessing behavior.

---

## Statistics

The Statistics menu displays the player's overall performance during the current program session.

Example:

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
Average score: 96.5

Best Scores
--------------------------------
Easy: 100
Medium: 110
Hard: 130

Best Attempts
--------------------------------
Easy: 2
Medium: 3
Hard: 4

Achievements
--------------------------------
- First Win
- Perfect Guess
- No Hints Used
================================
```

---

## Games Played

The program counts the number of games started.

```python
games_played += 1
```

This value is used for calculating the player's overall win rate.

---

## Games Won

Whenever the player correctly guesses the secret number:

```python
games_won += 1
```

The games won value is used to calculate the player's performance.

---

## Win Rate

The program calculates the win rate using:

```python
win_rate = (games_won / games_played) * 100
```

For example:

```text
Games played: 5
Games won: 4
Win rate: 80.0 %
```

---

## Average Attempts

The program calculates the average number of attempts used during successful games.

```python
average_attempts = total_attempts / games_won
```

Example:

```text
Average attempts per win: 3.25
```

---

## Average Score

The program also keeps track of the total score earned from successful games.

The average score is calculated using:

```python
average_score = total_score / games_won
```

This gives the player another way to measure their performance.

---

## Win Streak

The game tracks consecutive wins.

After a successful game:

```python
win_streak += 1
```

If the player loses or quits:

```python
win_streak = 0
```

The program also stores the longest win streak:

```python
if win_streak > longest_streak:
    longest_streak = win_streak
```

---

## Best Scores

The program stores a separate best score for each standard difficulty.

```python
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

Example:

```text
Best Scores
--------------------------------
Easy: 100
Medium: 110
Hard: 130
```

A new best score is recorded when the player's current score is higher than the previous record.

---

## Best Attempts

The program also tracks the fewest attempts used for each standard difficulty.

```python
best_attempts = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

Example:

```text
Best Attempts
--------------------------------
Easy: 2
Medium: 3
Hard: 4
```

A lower number of attempts becomes the new record.

---

## Game History

The new version stores information about games played during the current session.

Each game can contain:

* Difficulty
* Result
* Number of attempts
* Score
* Guess history

Example:

```text
================================
          GAME HISTORY
================================

Difficulty: Medium
Result: Won
Attempts: 4
Score: 90
Guesses: [50, 75, 60, 64]

--------------------------------

Difficulty: Hard
Result: Lost
Attempts: 10
Score: 0
Guesses: [100, 200, 300, 400]
```

The game history is stored using a list of dictionaries.

---

## Leaderboard

The Leaderboard menu displays the player's best scores and fewest attempts.

Example:

```text
================================
          LEADERBOARD
================================

BEST SCORES
--------------------------------
Easy: 100
Medium: 110
Hard: 130

FEWEST ATTEMPTS
--------------------------------
Easy: 2
Medium: 3
Hard: 4
================================
```

The leaderboard is based on records from the current program session.

---

## Achievement System

The game now includes an achievement system.

Achievements are stored in a list.

```python
achievements = []
```

An achievement is only added if it has not already been unlocked.

### First Win

Unlocked after the player wins their first game.

```text
*** ACHIEVEMENT UNLOCKED: First Win ***
```

### Perfect Guess

Unlocked when the player guesses the correct number on the first attempt.

```text
*** ACHIEVEMENT UNLOCKED: Perfect Guess ***
```

### No Hints Used

Unlocked when the player wins without using hints.

```text
*** ACHIEVEMENT UNLOCKED: No Hints Used ***
```

### 5 Win Streak

Unlocked after achieving five consecutive wins.

```text
*** ACHIEVEMENT UNLOCKED: 5 Win Streak ***
```

The achievement system gives the player additional goals while playing.

---

## Input Validation

The program uses `try` and `except` to handle invalid input.

```python
try:
    guess = int(input("Enter your guess: "))

except ValueError:
    print("Please enter a valid number.")
```

If the player enters text instead of a number, the program does not crash.

It simply asks the player to enter a valid number.

The program also checks whether the guess is within the selected range.

Example:

```text
Please enter a number between 1 and 50
```

Invalid input does not use an attempt.

---

## Attempt System

Each difficulty has a different number of attempts.

The attempt counter starts at:

```python
attempts = 0
```

Every valid and unique guess increases the counter:

```python
attempts += 1
```

The game continues while:

```python
while attempts < max_attempts:
```

Invalid inputs and duplicate guesses do not use an attempt.

---

## Game Over

If the player uses all available attempts without guessing the correct number, the game ends.

Example:

```text
================================
          GAME OVER
================================
You ran out of attempts.
The correct number was: 347

Better luck next time!
```

The player's guesses are also displayed.

The current win streak is reset after losing.

---

## Technologies Used

* **Python**
* **Random Module**
* **Terminal / Command Prompt**
* **PyCharm**
* **Visual Studio Code**

No external libraries are required.

---

## Python Concepts Used

This project demonstrates several beginner-level Python programming concepts.

### Variables

Variables store information such as the secret number, score, difficulty, attempts, and statistics.

```python
number = random.randint(1, maximum)
attempts = 0
score = 100
```

### Lists

Lists are used for guess history, game history, and achievements.

```python
guess_history = []
game_history = []
achievements = []
```

### Dictionaries

Dictionaries store organized information such as best scores and game records.

```python
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

Game history also uses dictionaries:

```python
{
    "difficulty": difficulty,
    "result": "Won",
    "attempts": attempts,
    "score": score,
    "guesses": guess_history.copy()
}
```

### Functions

The expanded version uses functions to separate different parts of the program.

Examples include:

```python
def unlock_achievement(name):
```

```python
def show_statistics():
```

```python
def show_history():
```

```python
def show_leaderboard():
```

```python
def custom_game():
```

```python
def play_game(maximum, max_attempts, difficulty):
```

Functions make the code easier to organize, read, test, and explain.

### User Input

The `input()` function allows the player to interact with the game.

```python
choice = input("Choose an option: ")
```

```python
guess = int(input("Enter your guess: "))
```

### Conditional Statements

The program uses `if`, `elif`, and `else` to make decisions.

```python
if guess < number:
    print("Too low!")

elif guess > number:
    print("Too high!")

else:
    print("Congratulations!")
```

Conditional statements are also used for scoring, hints, achievements, validation, and statistics.

### While Loops

The game uses `while` loops to repeat the main menu and guessing process.

```python
while True:
```

and:

```python
while attempts < max_attempts:
```

### For Loops

The program uses `for` loops when displaying achievements, game history, and leaderboard information.

Example:

```python
for achievement in achievements:
    print("-", achievement)
```

### Random Number Generation

The secret number is generated using:

```python
number = random.randint(1, maximum)
```

The maximum value changes according to the selected difficulty.

### Try and Except

Exception handling prevents invalid input from crashing the program.

```python
try:
    guess = int(input("Enter your guess: "))

except ValueError:
    print("Please enter a valid number.")
```

### Absolute Value

The `abs()` function calculates the distance between the guess and the secret number.

```python
difference = abs(number - guess)
```

This is used by the Hot/Cold and Closer/Farther systems.

### Min and Max

The program uses `min()` and `max()` to analyze the player's guesses.

```python
min(guess_history)
```

```python
max(guess_history)
```

### Sum

The `sum()` function is used when calculating the average guess.

```python
sum(guess_history)
```

### Break

The `break` statement is used to stop a loop when the game ends.

```python
break
```

### Continue

The `continue` statement skips the current loop iteration when the input is invalid or duplicated.

```python
continue
```

### Arithmetic Operators

Arithmetic operators are used for score calculations, win rate, averages, streak bonuses, and hint penalties.

Examples:

```python
score = 100 - ((attempts - 1) * 10)
```

```python
win_rate = (games_won / games_played) * 100
```

---

## Data Stored During the Game

The program stores several types of information while it is running.

```text
Game Data
│
├── Difficulty
├── Secret Number
├── Maximum Number
├── Maximum Attempts
├── Current Attempts
├── Score
│
├── Guess History
│
├── Game History
│   ├── Difficulty
│   ├── Result
│   ├── Attempts
│   ├── Score
│   └── Guesses
│
├── Statistics
│   ├── Games Played
│   ├── Games Won
│   ├── Win Rate
│   ├── Current Win Streak
│   ├── Longest Win Streak
│   ├── Average Attempts
│   ├── Average Score
│   └── Total Hints
│
├── Best Scores
│
├── Best Attempts
│
└── Achievements
```

The current version stores this information only while the program is running.

Closing the program resets the statistics, leaderboard, game history, and achievements.

---

## Project Structure

```text
Number-Guessing-Game/
│
├── main.py
└── README.md
```

---

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the installed version by opening a terminal and running:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Number-Guessing-Game.git
```

### 3. Open the Project

Open the project folder using:

* PyCharm
* Visual Studio Code
* Another Python IDE

### 4. Run the Program

Run:

```bash
python main.py
```

---

## Example Gameplay

```text
================================
      NUMBER GUESSING GAME
================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Custom Game
5. Statistics
6. Game History
7. Leaderboard
8. Exit
================================

Choose an option: 2

================================
         GAME START
================================
Difficulty: Medium
Number range: 1 - 100
Attempts: 7

Type 0 at any time to quit the game.

================================

Enter your guess: 50
Too low!

Cold. You are far from the number.

Attempts remaining: 6

Enter your guess: 75
Too high!

Hot! You are close.
You are getting CLOSER!

Attempts remaining: 5

Would you like a hint? (yes/no): yes

HINT
The number is EVEN.

Hint penalty: -10 points

Enter your guess: 64

================================
        CONGRATULATIONS!
================================

You guessed the correct number!
The number was: 64
Attempts: 3

Your score: 100

Guess Analysis
Lowest guess: 50
Highest guess: 75
Average guess: 63.0

Your guesses:
[50, 75, 64]
```

---

## Future Improvements

Possible future features include:

* Save statistics to a file
* Permanent high scores
* Player name system
* Multiple player support
* Timer system
* Countdown timer
* Multiple rounds
* Persistent scores
* More achievement types
* More difficulty levels
* More hint types
* Sound effects
* Graphical user interface
* Colorful terminal interface
* Database support
* Persistent game history
* Export statistics to a file
* Online leaderboard
* Player profiles
* Difficulty-specific statistics

---

## Purpose

This project was created for learning and practice while studying Python programming.

It demonstrates how basic Python concepts can be combined to create an interactive terminal-based game.

The project provides practice with **user input, random number generation, variables, lists, dictionaries, functions, loops, conditional statements, exception handling, calculations, score systems, statistics, and game logic**.

The project was expanded from a basic guessing game into a more complete game system by adding **custom difficulty, optional hints, hint penalties, hot/cold feedback, guess analysis, game history, leaderboards, best attempts, achievements, win streak bonuses, and session statistics**.

The project remains focused on beginner-friendly Python programming while providing enough features to demonstrate how a simple program can be gradually expanded.

---

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

GitHub: `Claxer`

---

## License

This project is available for educational and personal use.
