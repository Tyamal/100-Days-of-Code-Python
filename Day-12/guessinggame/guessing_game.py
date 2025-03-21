import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number_to_guess:
            attempts -= 1
            print("Too low!")
        elif guess > number_to_guess:
            attempts -= 1
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        else:
            print(f"You have {attempts} attempts left.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
