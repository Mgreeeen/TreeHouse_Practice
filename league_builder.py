import csv
import random
import re

def divider(list_of_kids):
    amount = int((len(list_of_kids)) / 3)
    random.shuffle(list_of_kids)
    try:
        Droogons = list_of_kids[:amount]
        Roopters = list_of_kids[amount:-amount]
        Shoorks = list_of_kids[-amount:]
    except IndexError:
        print("Oh well. Life's unfair too.")
    return Droogons, Roopters, Shoorks

def make_pretty(team):
    for i in range(len(team)):
        del team[i][4]
    return team

if __name__ == "__main__":

    Player_Info = []
    Dragons = []
    Raptors = []
    Sharks = []
    Exp_Player = []
    Non_Exp_Player = []

    with open("Soccer_list.csv", "r") as soccer_list:
        soccer_list_reader = csv.reader(soccer_list)
        next(soccer_list)

        for line in soccer_list_reader:
            Player_Info.append(line)

        soccer_list.close()

    for unit in Player_Info:
        if " Y" in unit:
            Exp_Player.append(unit)

    for player in Player_Info:
        if " N" in player:
            Non_Exp_Player.append(player)

#Randomizing and distributing exp players
    Dragonss, Raptorss, Sharkss = divider(Exp_Player)
    Dragons.extend(Dragonss)
    Raptors.extend(Raptorss)
    Sharks.extend(Sharkss)

#Randomizing and distributing non-exp players
    Nargons, Jarptops, Smarks = divider(Non_Exp_Player)
    Dragons.extend(Nargons)
    Raptors.extend(Jarptops)
    Sharks.extend(Smarks)

#Getting rid of some silly extra ""
    Dragons = make_pretty(Dragons)
    Raptors = make_pretty(Raptors)
    Sharks = make_pretty(Sharks)

#Writing team rosters to a txt file
    teams_file = open('---teams.txt---', 'w')
    teams_file.write("Dragons: " + (str(Dragons)) + "\nRaptors: " + (str(Raptors))
                   + "\nSharks: " + (str(Sharks)))
    teams_file.close()

#Customized letters for the guardian of each player
    for i in range(len(Dragons)):
        File_Name = re.sub(r' ','_',(Dragons[i][0]))
        this = open(f'{File_Name.lower()}.txt', 'w')
        this.write(f'Dear {Dragons[i][3]}, your child {Dragons[i][0]} has been placed on the: Dragons.'
                   f'  First practice will be at 9:00AM on Feb.1/2019.')

    for i in range(len(Raptors)):
        File_Name = re.sub(r' ','_',(Raptors[i][0]))
        this = open(f'{File_Name.lower()}.txt', 'w')
        this.write(f'Dear {Raptors[i][3]}, your child {Raptors[i][0]} has been placed on the: Raptors.'
                   f'  First practice will be at 10:00AM on Feb.1/2019.')

    for i in range(len(Sharks)):
        File_Name = re.sub(r' ','_',(Sharks[i][0]))
        this = open(f'{File_Name.lower()}.txt', 'w')
        this.write(f'Dear {Sharks[i][3]}, your child {Sharks[i][0]} has been placed on the: Sharks.'
                   f'  First practice will be at 11:00AM on Feb.1/2019.')



