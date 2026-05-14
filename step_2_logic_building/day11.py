import random

print("===== Guess Number Game =====")

while True:

    number_to_guess = random.randint(1, 100)

    attempts = 0

    print("\nI selected a number between 1 and 100.")

    while True:

        user_guess = int(input("Enter your guess: "))

        attempts += 1

        if user_guess < number_to_guess:
            print("Too Low! Try again.")

        elif user_guess > number_to_guess:
            print("Too High! Try again.")

        else:
            print(f"\nCorrect! The number was {number_to_guess}")
            print(f"You guessed it in {attempts} attempts.")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break