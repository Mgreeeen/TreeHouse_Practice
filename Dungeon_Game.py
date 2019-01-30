import random
#actually have it look like something instead of just imagined
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0),
         (0, 1), (1, 1), (2, 1), (3, 1),
         (0, 2), (1, 2), (2, 2), (3, 2),
         (0, 3), (1, 3), (2, 3), (3, 3)]

def random_start_locations():
    startt, starttt, startttt = random.sample(CELLS, 3)
    return (startt, starttt, startttt)

def movement(location, direction):
    x, y = location
    if direction == "LEFT":
        if x > 0:
            x -= 1
            new_location = (x, y)
            print(new_location)
            return new_location
        else:
            print("You've hit a wall.")
            return location
    elif direction == "RIGHT":
        if x < 3:
            x += 1
            new_location = (x, y)
            print(new_location)
            return new_location
        else:
            print("You've hit a wall.")
            return location
    elif direction == "UP":
        if y > 0:
            y -= 1
            new_location = (x, y)
            print(new_location)
            return new_location
        else:
            print("You've hit a wall.")
            return location
    elif direction == "DOWN":
        if y < 3:
            y += 1
            new_location = (x, y)
            print(new_location)
            return new_location
        else:
            print("You've hit a wall.")
            return location


while True:
#The Spawning
    player, monster, door = random_start_locations()
#The Greeting
    print("Dungeons and dragons is for wimps. Let's play a real game.\n Type HELP for help or get goin bucko'.")
#The Main Game Loop
    while True:
        request = input("> ")

        if request.upper() == "HELP":
            print("""You, a monster, and a door all start in a unique cell.
            \t you must type "LEFT, RIGHT, DOWN, or UP and navigate your
            \t way to the door. If you meet the door - you win. If you
            \t meet the monster - you lose.""")

        elif request.upper() == "LEFT":
            player = movement(player, "LEFT")
        elif request.upper() == "RIGHT":
            player = movement(player, "RIGHT")
        elif request.upper() == "UP":
            player = movement(player, "UP")
        elif request.upper() == "DOWN":
            player = movement(player, "DOWN")

        if player == door:
            print("You've survived the dungeon!")
            print("Would you like to play again? [y]es / [n]o")
            retry = input("> ")

            if retry.lower() == "y":
                print("----- You return to the dungeon. A fool. -----")
                break
            elif retry.lower() == "n":
                print("---- You leave the dungeon. A hero. -----")
                quit()

        if player == monster:
            print("Lol u ded")
            print("Would you like to play again? [y]es / [n]o")
            retry = input("> ")

            if retry.lower() == "y":
                print("----- K. You DIED.    .... wtvr. REDO. -----")
                break
            elif retry.lower() == "n":
                print("---- You leave the dungeon. In a body bag. -----")
                quit()


