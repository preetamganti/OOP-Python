import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def play_game(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            guess = self.get_player_guess()
            self.attempts += 1

            if guess < self.secret_number:
                print("Too low! Try again.")
            elif guess > self.secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {self.attempts} attempts.")
                break

    def get_player_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                else:
                    return guess
            except ValueError:
                print("Invalid input. Please enter a number.")

# Create a new instance of the game
game = NumberGuessingGame()

# Start the game
game.play_game()
