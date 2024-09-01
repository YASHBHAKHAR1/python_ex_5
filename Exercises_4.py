import random

def main():
    # The computer draws a random integer between 1 and 10
    target_number = random.randint(1, 10)

    while True:
        # Prompt the user to guess the number
        user_guess = int(input("Guess a number between 1 and 10: "))

        # Check if the guess is too low, too high, or correct
        if user_guess < target_number:
            print("Too low!")
        elif user_guess > target_number:
            print("Too high!")
        else:
            print("Correct! You guessed the right number.")
            break  # Exit the loop since the user guessed correctly

if __name__ == "__main__":
    main()
