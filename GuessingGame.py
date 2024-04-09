# Justin Schamel
# CIS261
# Guessing Game

# Import required modules
import random

# Display title of game
print("""
  ____ _   _ _____ ____ ____    _____ _   _ _____   _   _ _   _ __  __ ____  _____ ____  _ 
 / ___| | | | ____/ ___/ ___|  |_   _| | | | ____| | \ | | | | |  \/  | __ )| ____|  _ \| |
| |  _| | | |  _| \___ \___ \    | | | |_| |  _|   |  \| | | | | |\/| |  _ \|  _| | |_) | |
| |_| | |_| | |___ ___) ___) |   | | |  _  | |___  | |\  | |_| | |  | | |_) | |___|  _ <|_|
 \____|\___/|_____|____|____/    |_| |_| |_|_____| |_| \_|\___/|_|  |_|____/|_____|_| \_(_)
""")

# Greet the user
print("Welcome to the number guessing game!")

# Function to house the workings of the game
def game():
    """Prompts the user for a guess and compares that guess to the random number."""
    guesses = 0
    guess = 0
    while guess != random_number:
        guess = int(input("Your guess: "))
        guesses += 1
        if guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low: ")
        else:
            print(f"Right on. You guessed it in {guesses} tries.")

# While loop to give user option to keep playing
playing = True
while playing:
    
    # Prompt user to set the number limit
    number_limit = int(input("\nEnter the number limit: "))

    # Generate a random number
    random_number = random.randint(1, number_limit)

    # Display message to user to show the range of possible numbers
    print(f"I am thinking of a number from 1 to {number_limit}.\n")
    # Call game function
    game()
    if input("\nWould you like to play again? (y/n): ") == "n":
        playing = False
