import random

try:
    import logo
except ImportError:
    logo = None


def show_logo_and_instructions():
    print("\nNUMBER GUESSING GAME\n")
    if logo is not None:
        print(logo.logo)

    print("How to play?\n")
    print("Enter s to start the game.")
    print("Guess a number between 1 and 100.")
    print("Enter 0 anytime to exit.\n")


def play_game(round_number):
    number = random.randint(1, 100)
    attempts = 0

    print(f"\n--- ROUND {round_number} ---")
    print("A random number between 1 to 100 has been generated.")
    print("Start guessing!\n")

    while True:
        user_input = input("Guess a number between 1 to 10: ")

        # character check
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(user_input)

        # exit option
        if guess == 0:
            print("You exited the round.")
            print(f"The number was {number}")
            return False, attempts   # round lost

        # range check
        if guess < 1 or guess > 100:
            print("Guessing number is out of range. Please enter the number between 1 to 100.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"\nCorrect! The number was {number}")
            print(f"You guessed it in {attempts} attempts.")
            return True, attempts    # round won


def main():
    show_logo_and_instructions()   # shown only once

    # start validation
    while True:
        start = input("Enter s to start: ").lower()
        if start == 's':
            break
        else:
            print("Invalid input, please try again.")

    round_number = 1
    score = 0

    while True:
        won, attempts = play_game(round_number)

        if won:
            score += 1

        print(f"\nScore: {score} | Rounds Played: {round_number}")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nFinal Score Summary")
            print(f"Total Rounds Played: {round_number}")
            print(f"Total Rounds Won: {score}")
            print("Thanks for playing!")
            break

        round_number += 1


main()
