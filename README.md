# Number Guessing Game

A simple **Python-based Number Guessing Game** that challenges the player to guess a randomly generated number within a selected difficulty level.

The player can choose between **Easy, Medium, and Hard** difficulty levels. Each difficulty has a different number range and number of attempts. The game provides hints by telling the player if their guess is **too high** or **too low**, and additional hints are provided after several attempts.

The game also includes a **score system, best score tracking, input validation, limited attempts, and a play-again option**.

This project was created as a beginner-friendly Python project to practice **variables, user input, conditional statements, loops, functions, exception handling, the random module, and basic program control**.

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
* Score system starting at 100 points
* Best score tracking
* Input validation
* Prevents invalid numbers from crashing the program
* Play Again option
* Exit option
* Simple terminal-based interface
* Beginner-friendly Python code

## Difficulty Levels

The game provides three difficulty levels:

| Difficulty | Number Range | Attempts |
| ---------- | -----------: | -------: |
| Easy       |         1-50 |       10 |
| Medium     |        1-100 |        7 |
| Hard       |        1-500 |       10 |

The player can also choose **Exit** from the main menu.

## How It Works

The program first displays the difficulty menu.

```text
================================
      NUMBER GUESSING GAME
================================
1. Easy   (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-500, 10 attempts)
4. Exit
================================
```

After the player selects a difficulty, the program generates a random number within the selected range.

The player then enters a guess.

```text
Difficulty
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
    +---- Invalid ----> Try Again
    |
    +---- Too Low ----> Try Again
    |
    +---- Too High ---> Try Again
    |
    +---- Correct ----> Calculate Score
                              |
                              v
                         Display Result
                              |
                              v
                          Play Again?
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
4. Exit
================================

Choose difficulty: 2

================================
         GAME START
================================
Difficulty: Medium
I have selected a number from 1 to 100
You have 7 attempts.
Try to guess the number!

Enter your guess: 50
Too low! Try again.
Attempts remaining: 6

Enter your guess: 75
Too high! Try again.
Attempts remaining: 5

Enter your guess: 60
Too low! Try again.
Attempts remaining: 4

HINT: The number is EVEN.

Enter your guess: 64
Congratulations!
You guessed the correct number!
The number was: 64
Number of attempts: 4
Your score: 70
```

## Scoring System

The player starts with a score of **100 points**.

The score decreases by **10 points for every additional attempt**.

For example:

```text
1 attempt  = 100 points
2 attempts = 90 points
3 attempts = 80 points
4 attempts = 70 points
5 attempts = 60 points
```

The minimum score is **10 points**, so the player will still receive a score even if they take many attempts.

## Hints

The game provides additional hints to help the player.

After three valid guesses, the game checks whether the secret number is **even or odd**.

Example:

```text
HINT: The number is EVEN.
```

For larger number ranges, another hint is provided after five attempts.

The game checks whether the number is in the **lower half** or **upper half** of the selected range.

Example:

```text
HINT: The number is in the UPPER half.
```

These hints help the player narrow down the possible number.

## Input Validation

The program checks whether the player enters a valid number.

If the player enters text instead of a number, the program displays:

```text
Please enter a valid number.
```

The program also checks whether the entered number is within the selected range.

For example, if the player chooses Easy mode and enters `100`, the program displays:

```text
Please enter a number between 1 and 50
```

This prevents invalid input from causing the program to crash.

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

the program returns to the difficulty selection menu and starts a new game.

If the player enters anything other than `yes`, the program exits.

## Technologies Used

* Python
* Random Module
* Terminal / Command Prompt

## Python Concepts Used

This project uses several basic Python concepts.

### Variables

Variables are used to store information such as the secret number, maximum number, number of attempts, score, and best score.

```python
number = random.randint(1, maximum)
attempts = 0
score = 100
```

### Dictionary

The program can use different values depending on the difficulty selected by the player.

For example, the selected difficulty determines the maximum number and the number of attempts.

```python
maximum = 100
max_attempts = 7
difficulty = "Medium"
```

### User Input

The `input()` function allows the player to enter their difficulty choice and guesses.

```python
choice = input("Choose difficulty: ")
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

Conditional statements are also used for difficulty selection, hints, score calculation, and input validation.

### While Loop

The `while` loop allows the game to continue while the player still has attempts.

```python
while attempts < max_attempts:
```

Another loop is used to allow the player to start another game.

```python
while True:
```

### For/Range Concepts

The project focuses mainly on `while` loops because the number of attempts changes depending on the difficulty. The attempt counter is used to control how long the guessing process continues.

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
score = score - ((attempts - 1) * 10)
```

The score is then checked to make sure it does not become lower than 10.

### Comparison Operators

The program uses comparison operators to determine whether the player's guess is lower, higher, or equal to the secret number.

```python
if guess < number:
elif guess > number:
else:
```

### Break Statement

The `break` statement stops the current game when the player guesses the correct number.

```python
break
```

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

* Timer system
* Multiple rounds
* Total score across multiple games
* Leaderboard
* More difficulty levels
* Custom number ranges
* Sound effects
* Graphical user interface
* Player name system
* Statistics tracking
* Win and loss counter
* Average number of attempts
* Saved high scores using a file or database

## Purpose

This project was created for learning and practice while studying Python programming.

It demonstrates how basic Python concepts can be combined to create a simple interactive terminal-based game.

The project also provides practice with **user input, random number generation, loops, conditional statements, error handling, scoring, and basic game logic**.

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

GitHub: `Claxer`

## License

This project is available for educational and personal use.
