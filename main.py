# The Librarys
import time
import json
import random
# The Region Variable. Just for base setup!
region = "None"
snum = 1
# These are where you are in the world!
X = float(0.00)
Z = float(0.00)
player_class = "None"
player_name = "None"
Hardcore_Mode = False
attack = False
party_member1 = "None"
party_member2 = "None"
party_member3 = "None"
level = 0
exp = 0
power = 0
mana = 0
health = 0
gold = 0
NPCL = 1
NPCP = 2
NPCC = "None"
NPCA1 = "None"
NPCG = 0
NPCEXP = float(0)
# For the random generation for the desert
px1 = random.randint(1, 20)
px2 = random.randint(1, 20)
px3 = random.randint(1, 20)
px4 = random.randint(1, 20)
px5 = random.randint(1, 20)
py1 = random.randint(1, 20)
py2 = random.randint(1, 20)
py3 = random.randint(1, 20)
py4 = random.randint(1, 20)
py5 = random.randint(1, 20)
# For the random generation for the village
vx1 = random.randint(1, 20)
vx2 = random.randint(1, 20)
vx3 = random.randint(1, 20)
vx4 = random.randint(1, 20)
vx5 = random.randint(1, 20)
vy1 = random.randint(1, 20)
vy2 = random.randint(1, 20)
vy3 = random.randint(1, 20)
vy4 = random.randint(1, 20)
vy5 = random.randint(1, 20)

ntype1 = random.randint(1, 2)
ncnpc1 = random.randint(1, 5)

if ncnpc1 == 1:
    rnnpc1 = "Dave"

elif ncnpc1 == 2:
    rnnpc1 = "Jack"

elif ncnpc1 == 3:
    rnnpc1 = "Brianna"

elif ncnpc1 == 4:
    rnnpc1 = "Noah"

elif ncnpc1 == 5:
    rnnpc1 = "Adam"

# The save feature
def save_game(snum):
    filename = f"saveslot{snum}.json"
    save_data = {
        "position": {"x": X, "z": Z},
        "player_name": player_name,
        "player_class": player_class,
        "hardcore_mode": Hardcore_Mode,
        "level" : level,
        "exp" : exp,
        "power" : power,
        "mana" : mana,
        "gold" : gold,
        "attack1" : attack1
    }

    with open(filename, "w") as f:
        json.dump(save_data, f, indent=4)

    print(f"Game saved to slot {snum}!")
# The loading feature
def load_game(snum):
    filename = f"saveslot{snum}.json"
    try:
        with open(filename, "r") as f:
            save_data = json.load(f)

        X = save_data["position"]["x"]
        Z = save_data["position"]["z"]
        player_name = save_data["player_name"]
        player_class = save_data["player_class"]
        Hardcore_Mode = save_data["hardcore_mode"]
        level = save_data["level"]
        exp = save_data["exp"]
        power = save_data["power"]
        mana = save_data["mana"]
        gold = save_data["gold"]
        attack1 = save_data["attack1"]

        print(f"Game loaded from slot {snum}!")
        return X, Z, player_name, player_class, Hardcore_Mode, level, exp, power, mana, gold, attack1
    
    except FileNotFoundError:
        print(f"No save file found in slot {snum}!")
        return None

    except json.JSONDecodeError:
        print(f"Save file in slot {snum} is corrupted!")
        return None
# The base setup for the NPC variable
NPC = "None"
# Cheats settings
cheats = False
# Just to fill in space
cheating = "Standared Edition"

print("Far from here")
print('Alpha 1.8')
print("The RPG Text Engine")

while True:
    print("Please select a game option:")
    print(cheating)
    print("  1. Start Game")
    print("  2. Option")
    print("  3. Load Game")
    print("  4. Exit")
    option = input("Please choose an option between 1-4: ")

    if option == "1":
        print("Starting Game!")
        time.sleep(1)
        print("Hello adventurer! Welcome to the game! As I understand, you are new to these lands and dont have any Identification...")
        print("In order to venture into these lands, can you please answer these few questions?")
        yn = input("What say you? (y/n): ")
        
        if yn == "y" or "Y" or "yes" or "Yes":
            print("Great! Lets get started!")

        elif yn == "n" or "N" or "no" or "No":
            print("Well then, I suppose you are not prepared for these lands... goodbye brave traveler! Come back another day!")
            continue

        else:
            print("Im sorry traveler, I do not understand. Please come back later and give me a strate answer!")
            continue

        print("Ok, first things first is you're name...")
        player_name = input("What is your name?: ")
        print(f"Ok {player_name}, welcome to the lands!")
        print("Ok, now, what is you're class? Here are the options available here! We have, the Knight, the Mage, and the Ranger! Or you can be a Hero!")
        print("(The Hero is hard mode!!!)")
        print("1. Knight (A Knight is a class that takes the brunt force of the team, and does the brunt force of the damage.)")
        print("2. Mage (A mage is good for utility and damage. The damage that the mage does is decent, but the mage is better for healing and transportation.)")
        print("3. Ranger (The Ranger is a ranged attacker, better than attacking then the Knight or Mage. The best for combat!)")
        print("4. Hero (All of them combined! No choosing classes! But its also Hardcore mode!) (Hard Mode!!!)")
        while True:
            pcon = input("Please choose an option! (1-4): ")

            if pcon == "1":
                player_class = "Knight"
                Hardcore_Mode = False
                level = 1
                power = 2
                health = 15
                attack1 = "Slash"
                break

            elif pcon == "2":
                player_class = "Mage"
                Hardcore_Mode = False
                level = 1
                power = 1
                mana = 5
                health = 10
                attack1 = "Fire ball"
                break

            elif pcon == "3":
                player_class = "Ranger"
                Hardcore_Mode = False
                level = 1
                power = 5
                health = 10
                attack1 = "Shoot"
                break

            elif pcon == "4":
                player_class = "Undifined"
                Hardcore_Mode = True
                level = 1
                power = 1
                health = 10
                attack1 = "Puch"
                break

            else:
                print("Sorry, that's not an option. Try again!")
                continue

        print("Ok, great! Does this look right?")
        print(f"Name: {player_name} Class: {player_class} Hardcore Mode: {Hardcore_Mode}")
        print(f"Level: {level} Experience: {exp} Power: {power} Mana: {mana} Gold: {gold}")
        print("Attacks")
        print(f"1. {attack1}")

        yn = input("What say you? (y/n): ")

        if yn == "y" or "Y" or "yes" or "Yes":
            print("Great! Lets get going!")

        elif yn == "n" or "N" or "no" or "No":
            print("Oh, sorry. I suppose we shall restart at the menus! :(")
            continue

        else:
            print("Im sorry traviler, I do not understand. Please come back later and give me a strate answer!")
            continue



        break

    elif option == "2":
        print("Opening Settings...")
        time.sleep(1)
        print("Please choose an option to edit:")
        print("  1. Cheats ")
        print("  2. Back")
        SE = input("Please choose an option to edit (1-2): ")

        if SE == "1":
            print("Please choose an option: ")
            print("  1. False ")
            print("  2. True ")
            cheatss = input("Choose (1-2): ")
            
            if cheatss == "1":
                cheats = False
                cheating = ""

            elif cheatss == "2":
                cheats = True
                cheating = "Cheating Enabled!"


    elif option == "3":
        snum = int(input("Which slot do you want to load from? "))
        resault = load_game(snum)
        if resault is not None:
            X, Z, player_name, player_class, Hardcore_Mode, level, exp, power, mana, gold, attack1 = resault
            print(f"Name: {player_name} Class: {player_class} Hardcore Mode: {Hardcore_Mode}")
            print(f"Level: {level} Exp: {exp} Power: {power} Mana: {mana} Gold: {gold}")
            print("Attacks")
            print(f"1. {attack1}")
            break
        else:
            print("Could not load!")
            time.sleep(1)
            continue

    elif option == "4":
        print("Exiting...")
        time.sleep(1)
        exit(1)

#Before Game Starts
if cheats == True:
    print("DX1", px1)
    print("DX2", px2)
    print("DX3", px3)
    print("DX4", px4)
    print("DX5", px5)
    print("DZ1", py1)
    print("DZ2", py2)
    print("DZ3", py3)
    print("DZ4", py4)
    print("VX1", vx1)
    print("VX2", vx2)
    print("VX3", vx3)
    print("VX4", vx4)
    print("VX5", vx5)
    print("VZ1", vy1)
    print("VZ2", vy2)
    print("VZ3", vy3)
    print("VZ4", vy4)
    print("VZ5", vy5)
    print("Game Started")
else:
    print("Game Started")


while True:
    time.sleep(1.5)
    
    if X == float(600.06) and Z == float(700.07):
        region = "Jimbob"
    
    elif round(X, 1) == px1 or round(X, 1) == px2 or round(X, 1) == px3 or round(X, 1) == px4 or round(X, 1) == px5 and round(Z, 1) == py1 or round(Z, 1) == py2 or round(Z, 1) == py3 or round(Z, 1) == py4 or round(Z, 1) == py5:
        region = "Desert"

    elif round(X, 1) == vx1 or round(X, 1) == vx2 or round(X, 1) == vx3 or round(X, 1) == vx4 or round(X, 1) == vx5 and round(Z, 1) == vy1 or round(Z, 1) == vy2 or round(Z, 1) == vy3 or round(Z, 1) == vy4 or round(Z, 1) == vy5:
        region = "Village"

    else:
        region = "Plains"

    if X == float(600.06) and Z == float(700.07):
        NPC = "Jimbob"

    elif X == float(400.00) and Z == float(400.00):
        NPC = "Joj_ Reference"

    elif X == float(240.00) and Z == float(240.00):
        NPC = "Rotisory Chicken_724"
        region = "Villager_Render"

    elif X == vx1 + .02 and vy1 + .01:
        NPC = rnnpc1

    else:
        NPC = "None"

    if attack == False:
        print("")

    elif attack == True:
        print(f"Attacking {NPC}")
        ap = random.randint(1, 2)

        if ap == 1:
            NPCL = 1
            NPCP = 2
            NPCC = "Ranger"
            NPCA1 = "Shoot"
            NPCG = 15
            NPCEXP = float(.25)

        elif ap == 2:
            NPCL = 1
            NPCP = 1
            NPCC = "Knight"
            NPCA1 = "Slash"
            NPCG = 15
            NPCEXP = float(.25)

    print("What do you want to do?")
    print("1. Attack")
    print("2. Leave")
    fight = input("")




    if region == "Desert":
        print("-----------------------------------")
        print("|             Desert              |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("|     | #                         |")
        print("|     --#  |                      |")
        print("|       #--                       |")
        print("|       #                         |")
        print("|*********************************|")
        print("|*********************************|")
        print("-----------------------------------")

    elif region == "Plains":
        print("-----------------------------------")
        print("|             Plains              |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("|  **                             |")
        print("|******                     **    |")
        print("|********                 ******  |")
        print("|**********             **********|")
        print("|*********************************|")
        print("|*********************************|")
        print("-----------------------------------")

    elif region == "Village":
        print("-----------------------------------")
        print("|           # Village             |")
        print("|            #                    |")
        print("|             #                   |")
        print("|             |                   |")
        print("|            _|____               |")
        print("|           /******\              |")
        print("|          /********\             |")
        print("|         /**********\            |")
        print("|          |**|---|*|             |")
        print("|          |**|  .|*|             |")
        print("|          |**|___|*|             |")
        print("-----------------------------------")


    elif region == "Jimbob":
        print("-----------------------------------")
        print("|             Jimbob              |")
        print("|                                 |")
        print("|               _                 |")
        print("|              |_|                |")
        print("|              /|\                |")
        print("|               |                 |")
        print("|              / \                |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("|                                 |")
        print("-----------------------------------")
        
    elif region == "Villager_Render":
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!77777777!!!~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
      print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!7777777???JJJJJYYYJ?77!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!7?JY55555555555555555555YYYYJ?7!!~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!7?JJYY5555555555555555555555YYJJ??7!!~~~~~~~~~~~~~~~~~~~!!!!!!!!!!~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!77???JJJYYYYY555555Y555555YY5555YYJ?77!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!7??J??????JJYY555555555555YYYYYYYYYYYYJJ?7!~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!!77?JJ????????JJJYY5555555YYYYYYJJJJJJJJJJJ?!~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!!7??JJ????JJ??????JYYYYYYYYYYYYJJJJJJJJJJJJ?!~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!77??JJ????JJJJJ?????JJJJJJJJJJJJJJ??JJJJJ??7!~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!77??????JJJJJJJ?????JJJJJJJ???????JJJYYJJ?7!!~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!?Y5PGP5J??JJJJJ?????JJJJJJJJJJJJJJJJJYYJ?7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~!77?J5PB#BG5JJ???????JJJJJJJJJJJJJJJJJJJJ?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~!!7777?JPB#BGP5YJ?????JJJJ???JJJJJJJJJJJ??7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~!!7?JJJ7!!7JYPB#BP5YJ??????????JJJJJJJJJJ??7!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~!?Y55555YY555YY5PBBG5JJJ????????JJJJJJJJJ?7!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~!?YPPPPPPGGGGG5JJJYYYYJJJ????JJJJJJJJJJJYJ?7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~!7J5GGP55PGB##BG5J7~^!7JJJJJJJJJJJJJJYYY55Y?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~!?J5PGGP555PGBBBG5YJ???????JJJJJJJJJJYPBBBGPJ!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~!?5GBGGP5555PGGBBGPP55YYJJJJJJJJJ??JY5GB##&#B5?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~!YG&&BGP555PPGGBBGPPP555YYYJJJJJJJJ5GB##B#&&&BPY?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~!7J5G##GPP555PPGBBGP5Y5555YYJJJJJJY5PGBB#######&&#P?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~?YPGBBBBGPP55PGBB#BGP5555YYJJJJJY5PGB##########&&&BPY?!~^~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~!JG##BBBBBGGPPGGB#&&##BGP5YYJJJY5PBB############BBB###PJ!~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~!7?5B&#BGGGGGGGGGGBB#&&@@&#BP5Y5G#####BBBGGGGGGGGGGBB###BP5J7~^~~~!!!!!~~~~~~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~!7J5GBBBBBGGGGGGGGBBB##&&@&&#B#####BBBBGGGGGGGGGGGGGBBB###GJ7!~~~~!!!!!!!!!~~~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~!7JYPBBBBBGGGGGGBBBGGB#&@@@@@&#BBBGBBGGGGGGGGGGGGGGBB#&&#G5J7!~!!!!!!!!!!!!!!~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~!7?YG##BBGGGBBBBBGGGGB##&&###BBGGBGGGGGGGGBBBBBBB####&@&B5?!!!!!!!!!!!!!!!~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~!7?J5PGBBBBBBBBBBGGGGBBBBBBBGGGBGGGGGGGBBBBBBBB##B##&&B5?7!!!!!!!!!!!!!!~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~7J5PGGBBBBBBBGGGGGGGGGGGBBGGGGGGGGBBBBBBBB###B##&#GY?7!!!!!!!!!!!!!!~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!J5G#&&#BGGGGGGGGGGGGBBGGGGGGBBBBBBB######BB#&&#5J77!!!!!77!!!!!!~~~!!")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~!7?Y5GBB#BGGGGGGGGBBBBGGGGGGBBB##&######BBB#&@#G5J?7!!7777!!!!~~~~~~~")
      print("~~~~~^^^^^~~~~~~~~~~~~~~~~~~~~~^^~!7?YPGBBBGGGGGBBBBGGGGGGBB###BBBB######&&&&#PYJ?7!!77777!!!~~~~~~~")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!7?5G#BBGGGGGGGGGGGBB#&&#PJJYPBBB##@@@&BPJ7!!77777777777!~~~~~~")
      print("~~~~~~~~~~~~~~~~^^~~~~~~~~~~~~~~~~~^~~~!7?J5GBBBBBGGGGGBBBBBGPJ!!7?JJJYY555YYJ77!!777777!!!7!!!~~~~~")
      print("^^^^^^^^^^^^^^^^^~^^~~~~~~~~~~~~~~~~~~^~~~!7J5PGGGBBBBB#&&#PY?!~~~!!!777777777777777777!!!!!!!!!!~~~")
      print("^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7J5PGB###&&&#57~~~~!!77777777777777!!!!!!!!!!!!!!!!!!~")
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~!77?JJJJJJJ?!~^~~~!!77777777777777!!!!!!!!!!!!!!!!!!!")
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~!!!!~~~~^^^^~~!!!7777777777777!!!!!!!!!!!!!!!!!!!")
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~^^^^^^^^^~~~~~~~~~~!!777777777777!!!!!!!!!!!!!!!!~~~")
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~^^^^^^^^^~~~~~^^~~~~!!!!!!!777777!!!!!!!!!!!!!!~~~~~")
      print("::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~^^^^^^^^^^^^^^~~~!!!!!!!!!!!!!!!!!!!!!!!!~~~~!!!!!!")
      print("......::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^~~~^^^^^^^^^^^^^^~~~!77777!!!!!!!!~~~~~~~~~~~~~~~!7????")
      print("::::::::::::..........:::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~!77????7777!!~~~~~~~~~~~~~~~~7?JJ?77")
      print("::::..................::::::::::::::::::::::^^^^^^^^^^^^^^^^^~~!!77???????77!!!!!!~~~~~~~~~~~7?JYJJJ")
      print(".............:::::::::.............:::::::::::::::^^^^^^^^^^^~~!!7?????????7777777!!!~~~~~~~~!?JY55P")


    print(f"Region : {region}")
    time.sleep(1)
    print(f"X Cords : {X}")
    print(f"Z Cords : {Z}")
    time.sleep(1)
    print(f"NPC: {NPC}")
    time.sleep(1)
    action = input("What do you want to do? (Say 'help' if you don't know!): ")
    if action == "help":
        print("Commands: help, move, exit, interact, help cheats (Only if cheats are enabled!!!)")

    elif action == "load":
        snum = int(input("Which slot do you want to load from? "))
        resault = load_game(snum)
        if resault is not None:
            X, Z, player_name, player_class, Hardcore_Mode, level, exp, power, mana, gold, attack1 = resault
            print(f"Name: {player_name} Class: {player_class} Hardcore Mode: {Hardcore_Mode}")
            print(f"Level: {level} Exp: {exp} Power: {power} Mana: {mana} Gold: {gold}")
            print("Attacks")
            print(f"1. {attack1}")
        else:
            print("Could not load!")
        time.sleep(1)
    
    elif action == "save":
        try:
            snum = int(input("Please type the slot you want to save to: "))
            save_game(snum)
        except ValueError:
            print("Unable to save to that slot! Invalid value!")
        time.sleep(1)
    
    elif action == "help cheats":
        if cheats == True:
            print("Cheat Commands: teleport, help cheats")

        else:
            print("Invalid Command! Cheats Disabled!")

    elif action == "teleport":
        if cheats == True:
            X = float(input("X Cords: "))
            Z = float(input("Z Cords: "))

        elif cheats == False:
            print("Invalid Command! Cheats Disabled!")

    
        
            #print("Plains----")
            #print("|*|  |*|5|")
            #print("|*!****|4|")
            #print("|******|3|")
            #print("|******|2|")
            #print("|******|1|")
            #print("|******|0|")
            #print("|543210|--")
            #print("----------")

        #elif region == "Village":
            #print("Plains----")
            #print("-|**||*|10|")
            #print("-|*^^**|9|")
            #print("-|*||**|8|")
            #print("-|*^^**|7|")
            #print("-|*||!*|6|")
            #print("|109876|--")
            #print("----------")
        

        #else:
            #print("**********************************************")
            #print("**********************************************")
            #print("**********************************************")
            #print("**********************************************")
            #print("**********************************************")
            #print("**************Map Not Available!!!************")
            #print("**********************************************")
            #print("**********************************************")
            #print("**********************************************")
            #print("**********************************************")


    elif action == "exit":
        print("Exiting the game! This will NOT save!!!")
        time.sleep(1.5)
        exit(1)

    elif action == "move":
        print("Move in what direction?")
        time.sleep(1)
        print("1. Forward")
        print("2. Backward")
        print("3. Left")
        print("4. Right")
        time.sleep(2)
        move = input("(1-4): ")

        if move == "1":
            X += float(0.01)
            time.sleep(1)
            print("Moved successfully!")

        elif move == "2":
            X -= float(0.01)
            time.sleep(1)
            print("Moved successfully!")

        elif move == "3":
            Z += float(0.01)
            time.sleep(1)
            print("Moved successfully!")

        elif move == "4":
            Z -= float(0.01)
            time.sleep(1)
            print("Moved successfully!")

        else:
            print("Invalid movement!")
            continue

    elif action == "w":
        X += float(0.01)
        time.sleep(1)
        print("Moved successfully!")

    elif action == "s":
        X -= float(0.01)
        time.sleep(1)
        print("Moved successfully!")

    elif action == "d":
        Z -= float(0.01)
        time.sleep(1)
        print("Moved successfully!")

    elif action == "a":
        Z += float(0.01)
        time.sleep(1)
        print("Moved successfully!")

    elif action == "interact":
        time.sleep(1)
         
        if NPC == "None":
            time.sleep(0)

        elif NPC == "Jimbob":
            print("Jimbob says: die")

        elif NPC == "Rotisory Chicken_724":
            print("Rotisory Chicken_724 says: Oh yeah we have to school 15 min later each day.")

        elif NPC == "Joj_ Reference":
            print("Joj_ Reference says: Kono Dio Da! >;) Here you go Cy Cy.")

        elif NPC == rnnpc1:
            if ntype1 == 1:
                print("Hello! I am a friendly villager!")

            if ntype1 == 2:
                print("Lets fight!")
                attack = True

        else:
            print("Nothing to Interact!")

    elif action == "e":
        time.sleep(1)
         
        if NPC == "None":
            time.sleep(0)

        elif NPC == "Jimbob":
            print("Jimbob says: die")

        elif NPC == "Rotisory Chicken_724":
            print("Rotisory Chicken_724 says: Oh yeah we have to school 15 min later each day.")

        elif NPC == "Joj_ Reference":
            print("Joj_ Reference says: Kono Dio Da! >;) Here you go Cy Cy.")

        elif NPC == rnnpc1:
            print("Hello! I am a freindly villager!")

        else:
            print("Nothing to Interact!")


    else:
        print("Invalid input!")

