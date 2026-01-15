
import random

# Try importing logo
try:
    import logo
except ImportError:
    logo = None


while True:
    
    # Print logo if available
    if logo is not None:
        print(logo.logo)

    print("How to play?\n")
    print("Enter s to start the game.")
    print("Type a number between 1 to 100 from the keyboard.")
    print("Enter 0 anytime to exit.\n")

    start = input("Enter s to start: ").lower()

    if start != 's':
        print("Invalid input! Program stopped.")
        break

    print("\nA random number between 1 and 100 has been generated.")
    print("Start guessing!\n")

    generated_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guessed_number = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guessed_number == 0:
            print("You exited the game.")
            print(f"The number was {generated_number}")
            break

        attempts += 1

        if guessed_number < generated_number:
            print("Your guess is too low")
        elif guessed_number > generated_number:
            print("Your guess is too high")
        else:
            print(f"\nYour guess is right! The number was {generated_number}")
            print(f"You guessed it in {attempts} attempts!")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
