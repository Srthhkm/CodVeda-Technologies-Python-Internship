import random                      # module to generate a random value

def number_guessing_game():
    print("Number Guessing Game")
    print("Guess a number between 1 and 100")       # User is asked to guess a no. between 1 and 100
    print("You have 5 attempts\n")             # Multiple attempts at guessing the number

    secret_number = random.randint(1, 100)            # random module to generate a random value in range
    attempts = 5                    

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < secret_number:               # Corresponding feedback to user
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number correctly.")             # correctly guessed
                return

            attempts -= 1
            print(f"Attempts left: {attempts}\n")

        except ValueError:
            print("Please enter a valid number\n")

    print(f"Game Over! The number was {secret_number}")          # either guessed correctly or all atempts exhausted


if __name__ == "__main__":
    number_guessing_game()
