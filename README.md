# Number Guessing Game

A simple **Python-based Number Guessing Game** that challenges the player to guess a randomly generated number between 1 and 100.

The program gives the player hints after every guess by telling them if their number is **too high** or **too low**. The game continues until the player correctly guesses the number and then displays the total number of attempts.

This project was created as a beginner-friendly Python project to practice **variables, user input, conditional statements, loops, the random module, and basic program control**.

## Features

* Randomly generates a number between 1 and 100
* Allows the player to enter guesses
* Checks whether the guess is too high or too low
* Tells the player when the correct number is guessed
* Counts the number of attempts
* Displays the correct answer after winning
* Simple terminal-based interface
* Beginner-friendly Python code

## How It Works

The program first generates a random number between 1 and 100 using Python's `random` module.

The player is then asked to enter a guess.

The program compares the player's guess with the randomly generated number.

```text
Guess
  |
  v
Compare Guess
  |
  +---- Too Low ----> Try Again
  |
  +---- Too High ---> Try Again
  |
  +---- Correct ----> You Win
```

The game continues using a `while` loop until the correct number is guessed.

## Example

```text
================================
      NUMBER GUESSING GAME
================================

I have selected a number from 1 to 100.
Try to guess the number!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Too low! Try again.

Enter your guess: 42
Congratulations!
You guessed the correct number!
The number was: 42
Number of attempts: 4

================================
        GAME OVER
================================
```

## Technologies Used

* Python
* Random Module
* Terminal / Command Prompt

## Python Concepts Used

This project uses several basic Python concepts:

### Variables

Variables are used to store the randomly generated number, the player's guess, and the number of attempts.

```python
number = random.randint(1, 100)
attempts = 0
```

### User Input

The `input()` function allows the player to enter a number.

```python
guess = int(input("Enter your guess: "))
```

### Conditional Statements

The program uses `if`, `elif`, and `else` to compare the player's guess with the secret number.

```python
if guess < number:
    print("Too low! Try again.")
elif guess > number:
    print("Too high! Try again.")
else:
    print("Congratulations!")
```

### While Loop

The `while` loop allows the game to continue until the player guesses the correct number.

```python
while True:
```

### Random Number Generation

The `random.randint()` function generates a random number between 1 and 100.

```python
number = random.randint(1, 100)
```

### Break Statement

The `break` statement stops the game once the player guesses the correct number.

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

* Difficulty levels
* Limited number of attempts
* Play Again option
* Score system
* High score tracking
* Different number ranges
* Input validation
* Difficulty-based scoring
* Timer
* Multiple rounds

## Purpose

This project was created for learning and practice while studying Python programming.

It demonstrates how basic Python concepts can be combined to create a simple interactive program.

## Author

**Jose Manuel Navoa**

Aspiring Information Technology Student

GitHub: `Claxer`

## License

This project is available for educational and personal use.
