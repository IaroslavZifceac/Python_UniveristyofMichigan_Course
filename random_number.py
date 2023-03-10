import random

# Generate a random number between 1 and 100
answer = random.randint(1, 5)

# Ask the user to guess the number
guess = int(input("Guess the number (1-100): "))

# Keep track of the number of guesses
guesses = 1

# Loop until the user guesses the correct number
while guess != answer:
    if guess < answer:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the number (1-100): "))
    guesses += 1

# Print a message when the user wins
print("Congratulations! You guessed the number in", guesses, "tries.")
