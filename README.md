# Number Guessing Game

A simple **Python-based Number Guessing Game** that challenges the player to guess a randomly generated number within a selected difficulty level.

The player can choose between **Easy, Medium, Hard, and Custom Game** modes. Each difficulty has a different number range and number of attempts. The game provides hints by telling the player if their guess is **too high, too low, hot, cold, closer, or farther** from the secret number.

The game also includes a **scoring system, difficulty bonuses, hint penalties, win streaks, achievements, player profiles, smart hints, game history, recent games, leaderboards, performance ratings, best scores, best attempts, guess analysis, input validation, limited attempts, and a quit-game option**.

This project was created as a beginner-friendly Python project to practice **variables, user input, conditional statements, loops, lists, dictionaries, functions, exception handling, the random module, calculations, and basic game logic**.

---

## Features

* Player name and profile
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
* Prime number detection
* Prime number hints
* Upper-half or lower-half hints
* Smaller number range hints
* Divisibility hints
* Higher or lower hints
* Smart hint system
* Optional hints
* Hint score penalties
* Score system
* Difficulty-based score bonuses
* Win streak score bonuses
* Lucky guess bonus
* Performance rating
* Best scores
* Best attempts
* Overall best score
* Overall fewest attempts
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
* Recent games
* Leaderboard
* Achievement system
* Achievement progress
* First Win achievement
* Perfect Guess achievement
* No Hints Used achievement
* 5 Win Streak achievement
* 10 Win Streak achievement
* Score Master achievement
* Lucky Guess achievement
* Hard Mode Winner achievement
* Custom Champion achievement
* Guessing Master achievement
* Input validation
* Invalid number protection
* Limited attempts
* Quit current game option
* Game summary
* Final statistics
* Terminal-based interface
* Beginner-friendly Python code

---

## Main Menu

The current version provides **11 menu options**:

```text
================================
      NUMBER GUESSING GAME
================================
Player: Player

================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Custom Game
5. Statistics
6. Game History
7. Leaderboard
8. Achievements
9. Player Profile
10. Recent Games
11. Exit
================================
```

The player can select a difficulty, create a custom game, view statistics, review game history, check the leaderboard, view achievements, check their player profile, view recent games, or exit the program.

---

## Player Profile

When the program starts, the player is asked to enter their name.

Example:

```text
================================
       PLAYER PROFILE
================================
Enter your name: Jose

Welcome, Jose!
Your game profile has been created.
```

The player's name is then displayed throughout the program.

The Player Profile menu displays information such as:

* Player name
* Games played
* Games won
* Win rate
* Current win streak
* Longest win streak
* Total score
* Total hints used
* Achievements unlocked
* Best game score
* Best game attempts

Example:

```text
================================
         PLAYER PROFILE
================================

Player: Jose
Games played: 10
Games won: 7
Win rate: 70.0 %
Current win streak: 3
Longest win streak: 5
Total score: 850
Total hints used: 6
Achievements unlocked: 5
Best game score: 150
Best game attempts: 1

================================
```

---

## Difficulty Levels

The game includes three standard difficulty levels and one custom mode.

| Difficulty |   Number Range |       Attempts | Difficulty Bonus |
| ---------- | -------------: | -------------: | ---------------: |
| Easy       |           1-50 |             10 |               +0 |
| Medium     |          1-100 |              7 |              +20 |
| Hard       |          1-500 |             10 |              +40 |
| Custom     | Player chooses | Player chooses |              +30 |

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

Example:

```text
================================
        CUSTOM GAME
================================

Enter maximum number: 1000
Enter number of attempts: 15
```

This allows the player to create a more personalized challenge.

---

## How the Game Works

The program first asks the player for their name.

The main menu is then displayed.

The player selects a game mode.

The program determines the number range and maximum number of attempts.

A secret number is randomly generated using Python's `random` module.

The player enters guesses until they:

1. Guess the correct number
2. Run out of attempts
3. Enter `0` to quit the current game

The program provides different feedback and hints during the game.

---

## Game Flow

```text
Start Program
     |
     v
Enter Player Name
     |
     v
Main Menu
     |
     +---- Easy
     |
     +---- Medium
     |
     +---- Hard
     |
     +---- Custom Game
     |
     +---- Statistics
     |
     +---- Game History
     |
     +---- Leaderboard
     |
     +---- Achievements
     |
     +---- Player Profile
     |
     +---- Recent Games
     |
     +---- Exit
     |
     v
Select Game
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
     +---- Invalid -------> Try Again
     |
     +---- Duplicate -----> Try Again
     |
     +---- 0 -------------> Quit Game
     |
     v
Check Guess
     |
     +---- Too Low -------> Give Feedback
     |
     +---- Too High ------> Give Feedback
     |
     +---- Correct --------> Calculate Score
                                  |
                                  v
                           Update Statistics
                                  |
                                  v
                           Check Achievements
                                  |
                                  v
                           Update Records
                                  |
                                  v
                           Save Game History
                                  |
                                  v
                            Show Summary
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

Difficulty bonuses are then added.

```text
Easy   = +0
Medium = +20
Hard   = +40
Custom = +30
```

---

## Hint Penalty

Using an optional hint reduces the player's score by **10 points**.

```text
Hint penalty: -10 points
```

Example:

```text
Base Score: 100
Hint Used: -10
Final Score: 90
```

This encourages players to solve the game with fewer hints.

---

## Win Streak Bonus

The game tracks consecutive wins.

Players receive additional score bonuses based on their current win streak.

The longer the player's streak, the greater the possible streak bonus.

Example:

```text
Current win streak: 3

Streak bonus:
3 x 5 = +15 points
```

If the player loses or quits a game, the current win streak resets to zero.

---

## Lucky Guess Bonus

If the player guesses the correct number on their **first attempt**, they receive a special bonus.

```text
LUCKY GUESS BONUS: +50
```

The player also unlocks the:

```text
Lucky Guess
```

achievement.

---

## Minimum Score

The program prevents a successful game from having a score below **10 points**.

```python
if score < 10:
    score = 10
```

This ensures that a player who wins still receives some points.

---

## Smart Hint System

The game includes a smart hint system.

After making at least two valid guesses, the player can choose:

```text
Would you like a hint? (yes/no):
```

If the player chooses `yes`, the program randomly selects one of several hint types.

---

## Even or Odd Hint

The game can tell whether the secret number is even or odd.

Example:

```text
SMART HINT
--------------------------------
The secret number is EVEN.
--------------------------------
```

The program checks:

```python
number % 2
```

---

## Prime Number Hint

The program can determine whether the secret number is a prime number.

Example:

```text
SMART HINT
--------------------------------
The secret number is a PRIME number.
--------------------------------
```

The program uses the `is_prime()` function to determine whether the number is prime.

---

## Upper or Lower Half Hint

The program can tell whether the secret number is in the upper or lower half of the selected range.

Example:

```text
SMART HINT
--------------------------------
The number is in the UPPER half.
--------------------------------
```

---

## Divisibility Hint

The program can randomly select a number such as:

```text
3
5
10
```

It then checks whether the secret number is divisible by that number.

Example:

```text
SMART HINT
--------------------------------
The number is divisible by 5.
--------------------------------
```

---

## Number Range Hint

The program can provide a smaller range around the secret number.

Example:

```text
SMART HINT
--------------------------------
The number is between 120 and 150.
--------------------------------
```

This helps narrow down the possible answer.

---

## Higher or Lower Hint

The program can tell the player whether the secret number is higher or lower than their current guess.

Example:

```text
The secret number is HIGHER than your guess.
```

---

## Hot and Cold System

The game provides a **Hot/Cold system** based on the distance between the player's guess and the secret number.

The distance is calculated using:

```python
difference = abs(number - guess)
```

Depending on the distance, the player receives different feedback.

```text
🔥 VERY HOT! You are extremely close.
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

This gives the player additional information without directly revealing the answer.

---

## Closer and Farther System

The game compares the current guess with the player's previous guess.

If the new guess is closer:

```text
You are getting CLOSER!
```

If the new guess is farther:

```text
You are getting FARTHER!
```

If both guesses have the same distance:

```text
You are the same distance from the number.
```

This makes the guessing process more interactive.

---

## Guess History

All valid guesses are stored in a list.

```python
guess_history = []
```

Each valid guess is added using:

```python
guess_history.append(guess)
```

Example:

```text
Your guesses:
[50, 75, 64]
```

The player can use the guess history to review their previous attempts.

---

## Duplicate Guess Detection

The game prevents the player from entering the same number more than once.

The program checks:

```python
if guess in guess_history:
    print("You already guessed that number.")
```

A duplicate guess does not use an attempt.

---

## Guess Analysis

After winning, the game analyzes the player's guesses.

It displays:

* Lowest guess
* Highest guess
* Average guess

Example:

```text
Guess Analysis
--------------------------------
Lowest guess: 50
Highest guess: 75
Average guess: 63.0

Your guesses:
[50, 75, 64]
```

The program uses:

```python
min(guess_history)
```

```python
max(guess_history)
```

and:

```python
sum(guess_history)
```

to calculate the results.

---

## Performance Rating

After winning, the game evaluates the player's performance.

Possible ratings include:

```text
LEGENDARY
EXCELLENT
GREAT
GOOD
DECENT
NEEDS IMPROVEMENT
```

The rating is based on the number of attempts and final score.

Example:

```text
Your score: 150
Performance: LEGENDARY
```

---

## Game Summary

After successfully guessing the number, the program displays a game summary.

Example:

```text
================================
         GAME SUMMARY
================================

Player: Jose
Result: WIN
Secret number: 64
Attempts: 3
Score: 100
Performance: EXCELLENT
Current streak: 3
Guess accuracy: 33.33 %

Guess Analysis
--------------------------------
Lowest guess: 50
Highest guess: 75
Average guess: 63.0

Your guesses:
[50, 75, 64]

================================
```

This provides the player with a complete overview of their performance.

---

## Player Statistics

The Statistics menu displays the player's overall performance during the current session.

The statistics include:

* Games played
* Games won
* Win rate
* Current win streak
* Longest win streak
* Total score
* Total hints used
* Average attempts per win
* Average score
* Best scores
* Best attempts
* Achievements

Example:

```text
================================
          STATISTICS
================================

Games played: 10
Games won: 7
Win rate: 70.0 %
Current win streak: 3
Longest win streak: 5
Total score: 850
Total hints used: 6

Average attempts per win: 3.14
Average score: 121.43

Best Scores
--------------------------------
Easy: 100
Medium: 120
Hard: 155

Best Attempts
--------------------------------
Easy: 1
Medium: 2
Hard: 3
================================
```

---

## Win Rate

The program calculates the player's win rate using:

```python
win_rate = (games_won / games_played) * 100
```

Example:

```text
Games played: 10
Games won: 7
Win rate: 70.0 %
```

---

## Average Attempts

The game calculates the average number of attempts used during successful games.

```python
average_attempts = total_attempts / games_won
```

Example:

```text
Average attempts per win: 3.14
```

---

## Average Score

The game calculates the average score earned from successful games.

```python
average_score = total_score / games_won
```

Example:

```text
Average score: 121.43
```

---

## Win Streak

The game keeps track of consecutive wins.

After a successful game:

```python
win_streak += 1
```

After losing or quitting:

```python
win_streak = 0
```

The program also records the longest streak:

```python
if win_streak > longest_streak:
    longest_streak = win_streak
```

---

## Best Scores

The program stores separate best scores for the standard difficulties.

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
Medium: 120
Hard: 155
```

A new record is created when the player earns a higher score.

---

## Best Attempts

The program also stores the fewest attempts used for each standard difficulty.

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
Easy: 1
Medium: 2
Hard: 3
```

A lower number of attempts becomes the new record.

---

## Overall Records

The game also keeps track of:

* Highest game score
* Fewest attempts in any game

Example:

```text
OVERALL RECORDS
--------------------------------
Highest game score: 155
Fewest attempts: 1
```

These records are separate from the difficulty-specific records.

---

## Game History

Every completed game is stored in `game_history`.

The program records information such as:

* Difficulty
* Result
* Attempts
* Score
* Performance rating
* Guesses

Example:

```text
================================
          GAME HISTORY
================================

Game 1
Difficulty: Medium
Result: Won
Attempts: 3
Score: 100
Performance: EXCELLENT
Guesses: [50, 75, 64]

--------------------------------

Game 2
Difficulty: Hard
Result: Lost
Attempts: 10
Score: 0
Performance: Failed
Guesses: [100, 200, 300, 400]
```

---

## Recent Games

The Recent Games feature displays the latest **five games**.

This provides a quick way for the player to review their most recent performance without displaying the entire game history.

Example:

```text
================================
         RECENT GAMES
================================

Game 1
Difficulty: Easy
Result: Won
Attempts: 2
Score: 105
Performance: GREAT

--------------------------------
```

---

## Leaderboard

The Leaderboard displays the player's current records.

It includes:

* Best score for Easy
* Best score for Medium
* Best score for Hard
* Fewest attempts per difficulty
* Overall best score
* Overall fewest attempts
* Longest win streak

Example:

```text
================================
          LEADERBOARD
================================

BEST SCORES
--------------------------------
Easy: 100
Medium: 120
Hard: 155

FEWEST ATTEMPTS
--------------------------------
Easy: 1
Medium: 2
Hard: 3

OVERALL RECORDS
--------------------------------
Highest game score: 155
Fewest attempts: 1

LONGEST WIN STREAK
--------------------------------
5
================================
```

---

## Achievement System

The game includes an achievement system that rewards different accomplishments.

Achievements are stored in:

```python
achievements = []
```

An achievement is only unlocked once.

---

### First Win

Unlocked after winning the first game.

```text
*** ACHIEVEMENT UNLOCKED: First Win ***
```

---

### Perfect Guess

Unlocked when the correct number is guessed on the first attempt.

```text
*** ACHIEVEMENT UNLOCKED: Perfect Guess ***
```

---

### No Hints Used

Unlocked when the player wins without using any hints.

```text
*** ACHIEVEMENT UNLOCKED: No Hints Used ***
```

---

### 5 Win Streak

Unlocked after five consecutive wins.

```text
*** ACHIEVEMENT UNLOCKED: 5 Win Streak ***
```

---

### 10 Win Streak

Unlocked after ten consecutive wins.

```text
*** ACHIEVEMENT UNLOCKED: 10 Win Streak ***
```

---

### Score Master

Unlocked after achieving a high score of at least 150 points.

```text
*** ACHIEVEMENT UNLOCKED: Score Master ***
```

---

### Lucky Guess

Unlocked when the player guesses the correct number on the first attempt.

```text
*** ACHIEVEMENT UNLOCKED: Lucky Guess ***
```

---

### Hard Mode Winner

Unlocked after winning a Hard difficulty game.

```text
*** ACHIEVEMENT UNLOCKED: Hard Mode Winner ***
```

---

### Custom Champion

Unlocked after winning a Custom Game.

```text
*** ACHIEVEMENT UNLOCKED: Custom Champion ***
```

---

### Guessing Master

Unlocked after winning at least ten games.

```text
*** ACHIEVEMENT UNLOCKED: Guessing Master ***
```

---

## Achievement Progress

The Achievements menu shows which achievements have been unlocked and which are still locked.

Example:

```text
================================
          ACHIEVEMENTS
================================

Unlocked: 5 / 10

--------------------------------

[UNLOCKED] First Win
[UNLOCKED] Perfect Guess
[UNLOCKED] No Hints Used
[LOCKED] 5 Win Streak
[LOCKED] 10 Win Streak
[UNLOCKED] Score Master
[UNLOCKED] Lucky Guess
[LOCKED] Hard Mode Winner
[LOCKED] Custom Champion
[LOCKED] Guessing Master

================================
```

---

## Input Validation

The program uses `try` and `except` to prevent invalid input from crashing the game.

```python
try:
    guess = int(input("Enter your guess: "))

except ValueError:
    print("Please enter a valid number.")
```

If the player enters text instead of a number, the program displays an error message.

The program also checks whether the guess is inside the allowed range.

Example:

```text
Please enter a number between 1 and 50
```

Invalid inputs do not use an attempt.

---

## Attempt System

Each difficulty has a different number of attempts.

The attempt counter starts at:

```python
attempts = 0
```

Each valid and unique guess increases the counter:

```python
attempts += 1
```

The guessing loop continues while:

```python
while attempts < max_attempts:
```

Invalid inputs and duplicate guesses do not use an attempt.

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

The game is then saved in the game history with:

```text
Result: Quit
```

The current win streak is also reset.

---

## Game Over

If the player uses all available attempts without guessing correctly, the game ends.

Example:

```text
================================
          GAME OVER
================================

You ran out of attempts.
The correct number was: 347

Better luck next time!

Your guesses:
[100, 200, 250, 300, 320, 330, 340, 345, 346, 348]
```

The game is saved in the history as a lost game.

---

## Data Storage

The program uses lists and dictionaries to store information while it is running.

### Best Scores

```python
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

### Best Attempts

```python
best_attempts = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

### Guess History

```python
guess_history = []
```

### Game History

```python
game_history = []
```

### Achievements

```python
achievements = []
```

These structures allow the program to organize player and game information.

---

## Data Stored During the Game

```text
Game Data
│
├── Player Name
│
├── Difficulty
│
├── Secret Number
│
├── Maximum Number
│
├── Maximum Attempts
│
├── Current Attempts
│
├── Score
│
├── Guess History
│
├── Game History
│   ├── Difficulty
│   ├── Result
│   ├── Attempts
│   ├── Score
│   ├── Performance
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
├── Overall Records
│
└── Achievements
```

The current version stores this information only during the current program session.

Closing the program resets the game history, statistics, leaderboard, and achievements.

---

## Python Concepts Used

This project demonstrates several fundamental Python programming concepts.

### Variables

Variables store values such as the secret number, attempts, score, difficulty, and statistics.

```python
number = random.randint(1, maximum)
attempts = 0
score = 100
```

### Lists

Lists are used for storing guesses, game history, and achievements.

```python
guess_history = []
game_history = []
achievements = []
```

### Dictionaries

Dictionaries are used to organize information.

```python
best_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}
```

Game records are also stored using dictionaries.

```python
{
    "difficulty": difficulty,
    "result": "Won",
    "attempts": attempts,
    "score": score,
    "rating": rating,
    "guesses": guess_history.copy()
}
```

### Functions

The project uses functions to separate different parts of the program.

Examples include:

```python
def setup_player():
```

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
def show_achievements():
```

```python
def custom_game():
```

```python
def calculate_score():
```

```python
def update_records():
```

```python
def play_game():
```

Functions make the program easier to organize and maintain.

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

The game uses `while` loops for the main menu and guessing process.

```python
while True:
```

```python
while attempts < max_attempts:
```

### For Loops

`for` loops are used to display achievements, game history, and other stored information.

```python
for achievement in achievements:
    print("-", achievement)
```

### Random Module

The `random` module is used to generate the secret number.

```python
number = random.randint(1, maximum)
```

It is also used to randomly select smart hints.

### Exception Handling

The program uses `try` and `except` to handle invalid numerical input.

```python
try:
    guess = int(input("Enter your guess: "))

except ValueError:
    print("Please enter a valid number.")
```

### Absolute Value

The `abs()` function determines the distance between the guess and the secret number.

```python
difference = abs(number - guess)
```

This is used for the Hot/Cold system.

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

The `break` statement stops a loop when the game or program ends.

```python
break
```

### Continue

The `continue` statement skips the current loop iteration when input is invalid or duplicated.

```python
continue
```

### Arithmetic Operators

Arithmetic operators are used for score calculations, win rate, averages, streak bonuses, and hint penalties.

Example:

```python
score = 100 - ((attempts - 1) * 10)
```

---

## Technologies Used

* **Python**
* **Python Random Module**
* **PyCharm**
* **Visual Studio Code**
* **Windows Terminal / Command Prompt**

No external Python libraries are required.

---

## Project Structure

```text
Number-Guessing-Game/
│
├── main.py
└── README.md
```

The main program is contained in:

```text
main.py
```

The documentation is contained in:

```text
README.md
```

---

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the installed version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Number-Guessing-Game.git
```

### 3. Open the Project

Open the project using:

* PyCharm
* Visual Studio Code
* Another Python IDE

### 4. Run the Program

Open a terminal inside the project folder and run:

```bash
python main.py
```

---

## Example Gameplay

```text
================================
      NUMBER GUESSING GAME
================================

Player: Jose

================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Custom Game
5. Statistics
6. Game History
7. Leaderboard
8. Achievements
9. Player Profile
10. Recent Games
11. Exit
================================

Choose an option: 2

================================
         GAME START
================================

Player: Jose
Difficulty: Medium
Number range: 1 - 100
Attempts: 7

Type 0 at any time to quit this game.

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

SMART HINT
--------------------------------
The secret number is EVEN.
--------------------------------

Hint penalty: -10 points

Enter your guess: 64

================================
        CONGRATULATIONS!
================================

You guessed the correct number!
The number was: 64
Attempts: 3

Your score: 100
Performance: EXCELLENT

================================
         GAME SUMMARY
================================

Player: Jose
Result: WIN
Secret number: 64
Attempts: 3
Score: 100
Performance: EXCELLENT
Current streak: 1

Guess Analysis
--------------------------------
Lowest guess: 50
Highest guess: 75
Average guess: 63.0

Your guesses:
[50, 75, 64]

================================
```

---

## Future Improvements

Possible future improvements include:

* Save player statistics to a file
* Permanent high scores
* Multiple player accounts
* Multiplayer mode
* Timer system
* Countdown timer
* Multiple rounds
* Persistent game history
* More achievement types
* More difficulty levels
* More smart hint types
* Sound effects
* Graphical user interface
* Colored terminal interface
* Database support
* Export statistics to a file
* Online leaderboard
* Player profiles
* Difficulty-specific statistics
* Save and load player progress

---

## Purpose

This project was created as a beginner-friendly Python programming project.

The purpose of the project is to demonstrate how basic Python programming concepts can be combined to create an interactive terminal-based game.

The project provides practice with:

* Variables
* User input
* Conditional statements
* Loops
* Lists
* Dictionaries
* Functions
* Exception handling
* Random number generation
* Arithmetic calculations
* Game logic
* Score systems
* Statistics
* Achievements
* Data organization

The project started as a simple number guessing game and was expanded into a more complete game system with **multiple difficulty levels, custom games, smart hints, Hot/Cold feedback, Closer/Farther feedback, scoring, streaks, achievements, player profiles, performance ratings, game history, recent games, leaderboards, and statistics**.

The project remains focused on beginner-friendly Python programming while demonstrating how a simple program can be gradually expanded with additional features.

---

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

GitHub: `Claxer`

---

## License

This project is available for educational and personal use.
