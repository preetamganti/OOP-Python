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


#Simple Numbers guessing game coded in Python - user needs to guess between 1 and 100 
#play_game() method is the main loop used for the player to make their guesses, and receive feedback on if its too high or low 
#get_player_guess() method prompts the player/user for their guess and validates it 
#if the player gets it right, they will receive a messages saying "Congratulations! You guessed the number in __ attempts."

