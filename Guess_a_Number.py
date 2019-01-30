#TreeHouse, Maxwell Green
#Project #1: Number Guessing Game
import random

guess_count = 1
high_score = 999
the_game = True

while True:

#The main game loop
    while the_game is True:
        print("Welcome to the Number Guessing Game!")
        print()
        valid_int = True
        while valid_int is True:
            try:
                x = int(input("Pick a number between 1 and 10 inclusive: "))
                valid_int = False
            except ValueError:
                print("A NUMBER between 1 and 10 inclusive please. ")
            else:
                if x < 1 or x > 10:
                    print("Noice one. Pick a number BETWEEN 1 and 10 inclusive: ")
                    valid_int = True

#Picking the magic number
        number = range(1, 11)
        magic_number = random.choice(number)
        print(magic_number)

#If the number is too high.
        while x != magic_number:
            if x > magic_number:
                print("Too high.")
                valid = True
                while valid is True:
                    try:
                        x = int(input("Try something lower: "))
                        valid = False
                    except ValueError:
                        print("A NUMBER between 1 and 10 inclusive please. ")
                        valid = True
                    else:
                        if x < 1 or x > 10:
                            print("Noice one. Pick a number BETWEEN 1 and 10 inclusive: ")
                            valid = True
                guess_count += 1
#If the number is too low.
            elif x < magic_number:
                print("Too low.")
                valid = True
                while valid is True:
                    try:
                        x = int(input("Try something lower: "))
                        valid = False
                    except ValueError:
                        print("A NUMBER between 1 and 10 inclusive please. ")
                        valid = True
                    else:
                        if x < 1 or x > 10:
                            print("Noice one. Pick a number BETWEEN 1 and 10 inclusive: ")
                            valid = True
                guess_count += 1

#Success and results section
        if x == magic_number:
            print("Well slap my titties and call me Shirley. You got it!")
            if guess_count == 1:
                print(f"It took you {guess_count} guess!")
                high_score = guess_count
                print(f"The current high score is {high_score}.")
            elif guess_count > 1:
                print(f"It took you {guess_count} guesses!")
                if guess_count < high_score:
                    high_score = guess_count
                    print(f"The current high score is {high_score}.")
                else:
                    print(f"The current high score is {high_score}.")
                print()

#Prompts to either finish/quit the game, or to replay.
        another_loop_lol = True
        while another_loop_lol is True:
            response = (input("Would you like to play another round? [y]es/[n]o: "))
            if response.lower() == "y":
                the_game = True
                another_loop_lol = False
            elif response.lower() == "n":
                the_game = False
                print("\nThank you for playing! Goodbye.")
                quit()
            else:
                another_loop_lol = True
