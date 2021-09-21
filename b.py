import secrets
import pickle
import random


# ------------------------------------------------------------------------------------------------------------------------ Variables
money = 0
level = 0
difficulty = level * 1.25
charactertype = 'null'
name = 'null'
questchoice = '1'
questlevel = questchoice
price = 100
points = 5
basehealth = 0
armor = 0
damage = 0
resetpoints = 0
damagemultpoints = 0
magicmultpoints = 0
rangedmultpoints = 0
healthmultpoints = 0
bartermultpoints = 0
damagemult = damage + (damagemultpoints * 0.2)
magicmult = damage + (magicmultpoints * 0.2)
rangedmult = damage + (rangedmultpoints * 0.2)
totalhealth = basehealth + (healthmultpoints * 3)
bartermult = price - (bartermultpoints * 2)
whack = damagemult + magicmult + rangedmult + damage
data = {name, level, whack, bartermult, totalhealth, rangedmult, magicmult, damagemult, bartermultpoints, healthmultpoints, rangedmultpoints, magicmultpoints, damagemultpoints, resetpoints, damage, armor, basehealth, points, price, money, questchoice, questlevel}

# ------------------------------------------------------------------------------------------------------------------------ Enemy Health

skeletonhealthmin = (float(9)*difficulty)
gianthealthmin = (float(18)*difficulty)
wizardhealthmin = (float(17)*difficulty)
witchhealthmin = (float(15)*difficulty)
bandithealthmin = (float(13)*difficulty)
trollhealthmin = (float(15)*difficulty)
bearhealthmin = (float(15)*difficulty)
spiderhealthmin = (float(9)*difficulty)
dragonhealthmin = (float(30)*difficulty)
vampirehealthmin = (float(16)*difficulty)
zombiehealthmin = (float(5)*difficulty)
werewolfhealthmin = (float(13)*difficulty)

skeletonhealthmax = (float(13)*difficulty)
gianthealthmax = (float(25)*difficulty)
wizardhealthmax = (float(20)*difficulty)
witchhealthmax = (float(20)*difficulty)
bandithealthmax = (float(17)*difficulty)
trollhealthmax = (float(23)*difficulty)
bearhealthmax = (float(20)*difficulty)
spiderhealthmax = (float(14)*difficulty)
dragonhealthmax = (float(50)*difficulty)
vampirehealthmax = (float(20)*difficulty)
zombiehealthmax = (float(10)*difficulty)
werewolfhealthmax = (float(16)*difficulty)

skeletonhealth = random.uniform(skeletonhealthmin, skeletonhealthmax)
gianthealth = random.uniform(gianthealthmin, gianthealthmax)
wizardhealth = random.uniform(wizardhealthmin, wizardhealthmax)
witchhealth = random.uniform(witchhealthmin, witchhealthmax)
bandithealth = random.uniform(bandithealthmin, bandithealthmax)
trollhealth = random.uniform(trollhealthmin, trollhealthmax)
bearhealth = random.uniform(bearhealthmin, bearhealthmax)
spiderhealth = random.uniform(spiderhealthmin, spiderhealthmax)
dragonhealth = random.uniform(dragonhealthmin, dragonhealthmax)
vampirehealth = random.uniform(vampirehealthmin, vampirehealthmax)
zombiehealth = random.uniform(zombiehealthmin, zombiehealthmax)
werewolfhealth = random.uniform(werewolfhealthmin, werewolfhealthmax)

# ------------------------------------------------------------------------------------------------------------------------ Enemy Damage

skeletondamagemin = (float(0)*difficulty)
giantdamagemin = (float(10)*difficulty)
wizarddamagemin = (float(6)*difficulty)
witchdamagemin = (float(6)*difficulty)
banditdamagemin = (float(3)*difficulty)
trolldamagemin = (float(8)*difficulty)
beardamagemin = (float(6)*difficulty)
spiderdamagemin = (float(4)*difficulty)
dragondamagemin = (float(12)*difficulty)
vampiredamagemin = (float(6)*difficulty)
zombiedamagemin = (float(1)*difficulty)
werewolfdamagemin = (float(2)*difficulty)

skeletondamagemax = (float(5)*difficulty)
giantdamagemax = (float(17)*difficulty)
wizarddamagemax = (float(11)*difficulty)
witchdamagemax = (float(11)*difficulty)
banditdamagemax = (float(7)*difficulty)
trolldamagemax = (float(15)*difficulty)
beardamagemax = (float(11)*difficulty)
spiderdamagemax = (float(7)*difficulty)
dragondamagemax = (float(20)*difficulty)
vampiredamagemax = (float(11)*difficulty)
zombiedamagemax = (float(6)*difficulty)
werewolfdamagemax = (float(11)*difficulty)

skeletondamage = random.uniform(skeletondamagemin, skeletondamagemax)
giantdamage = random.uniform(giantdamagemin, giantdamagemax)
wizarddamage = random.uniform(wizarddamagemin, wizarddamagemax)
witchdamage = random.uniform(witchdamagemin, witchdamagemax)
banditdamage = random.uniform(banditdamagemin, banditdamagemax)
trolldamage = random.uniform(trolldamagemin, trolldamagemax)
beardamage = random.uniform(beardamagemin, beardamagemax)
spiderdamage = random.uniform(spiderdamagemin, spiderdamagemax)
dragondamage = random.uniform(dragondamagemin, dragondamagemax)
vampiredamage = random.uniform(vampiredamagemin, vampiredamagemax)
zombiedamage = random.uniform(zombiedamagemin, zombiedamagemax)
werewolfdamage = random.uniform(werewolfdamagemin, werewolfdamagemax)


# ------------------------------------------------------------------------------------------------------------------------ Save game
def save():
    global data
    print("Saved Game Successfully!")
    pickle.dump(data, open("save.p", "wb"))


# ------------------------------------------------------------------------------------------------------------------------ Save game in quests
def questsave():
    global data
    print("Saved Game Successfully!")
    pickle.dump(data, open("save.p", "wb"))
    quest()


# ------------------------------------------------------------------------------------------------------------------------ Load game
def loadsave():
    global name
    global level
    global data
    global questlevel
    print("Do you want to load a save game?")
    save = input()
    if save == "Y" or save == "y":
        print("Loading Save.")
        print("Loading Save..")
        print("Loading Save...")
        data = pickle.load(open("save.p", "rb"))
        print('\033[1m'+"Loaded Save Successfully!" + '\033[0m')
        print("Loaded Character:", name)
        print('\033[1m'+"Loaded Level:" + '\033[0m', level)
        if questlevel == "1":
            skeleton()
        elif questlevel == "2":
            cave()
        elif questlevel == "3":
            wizard()
        elif questlevel == "4":
            village()
        elif questlevel == "5":
            witch()
        elif questlevel == "6":
            forest()
        elif questlevel == "7":
            bandits()
        elif questlevel == "8":
            chest()
        elif questlevel == "9":
            troll()
        elif questlevel == "10":
            bear()
        elif questlevel == "11":
            spider()
        elif questlevel == "12":
            dragon()
        elif questlevel == "13":
            vampire()
        elif questlevel == "14":
            zombie()
        elif questlevel == "15":
            werewolf()
        elif questlevel == "16":
            giant()
        elif questlevel == "17":
            crossroads()
    else:
        characterchoice()


# ------------------------------------------------------------------------------------------------------------------------ Start page
def startpage():  # Start of the game...
    print("Press Y to continue...")
    start = input()
    if start == "Y" or start == "y":
        print("Welcome!")
        loadsave()
    else:
        startpage()


# ------------------------------------------------------------------------------------------------------------------------ Character Choice Menu
def characterchoice():
    global name
    global charactertype
    global damage
    global basehealth
    global money
    global armor
    global points
    global level
    print("What will you character be called?")
    name = input("Character Name: ")
    print("Choose your character!")
    print(
        "Options: \n 1. Fighter: Small damage, Melee Damage, Big health! \n 2. Mage: Decent Damage, Magic Damage, Moderate Health! \n 3. Archer: Average Damage, Ranged Damage, Decent Health!  \n 4. Assassin: Crazy Damage, Melee & Ranged Damage, Low Health! \n")
    character = input("Character Number: ")
# ------------------------------------------------------------------------------------------------------------------------ Character Option 1: Fighter
    if character == "1":
        charactertype = "Fighter"
        damage = 8
        basehealth = 20
        money = 100
        armor = 2
        points = 5
        level = 0
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", basehealth)
        print("Coins: ", money)
        confirm = input("Confirm Class? y/n: ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Sword Equipped! Damage:", damage)
            print("Basic Armor Equipped! Damage:", armor)
            save()
            skills()
        else:
            print("\nCancelled! \n")
            characterchoice()
# ------------------------------------------------------------------------------------------------------------------------ Character Option 2: Mage
    if character == "2":
        charactertype = "Mage"
        damage = 12
        basehealth = 15
        money = 100
        armor = 2
        points = 5
        level = 0
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", basehealth)
        print("Coins: ", money)
        confirm = input("Confirm Class? : ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Staff Equipped! Damage:", damage)
            print("Basic Robes Equipped! Damage:", armor)
            save()
            skills()
        else:
            print("\nCancelled! \n")
            characterchoice()
# ------------------------------------------------------------------------------------------------------------------------ Character Option 3: Archer
    if character == "3":
        charactertype = "Archer"
        damage = 10
        basehealth = 18
        money = 100
        armor = 2
        points = 5
        level = 0
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", basehealth)
        print("Coins: ", money)
        confirm = input("Confirm Class? : ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Bow Equipped! Damage:", damage)
            print("Basic Light Armor Equipped! Health:", armor)
            save()
            skills()
        else:
            print("\nCancelled! \n")
            characterchoice()
# ------------------------------------------------------------------------------------------------------------------------ Character Option 4: Assassin
    if character == "4":
        charactertype = "Assassin"
        damage = 18
        basehealth = 10
        money = 100
        armor = 2
        points = 5
        level = 0
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", basehealth)
        print("Coins: ", money)
        confirm = input("Confirm Class? : ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Knife Equipped! Damage:", damage)
            print("Basic Stealth Armor Equipped! Damage:", armor)
            save()
            skills()
        else:
            print("\nCancelled! \n")
            characterchoice()
    else:
        print("\nNot Valid \n")
        characterchoice()


# ------------------------------------------------------------------------------------------------------------------------ Skill Menu
def skills():

    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack

    resetpoints = (damagemultpoints + magicmultpoints + rangedmultpoints + healthmultpoints + bartermultpoints)
    if points == 0:
        quest()
    else:
        print('\033[1m' + "\nHere you can spend skill points!" + '\033[0m')
        print("Points Available: ", points)
        print("Skill Trees: \n1: Damage: Each point multiplies damage by 0.2   Level:", damagemultpoints,
              "\n2: Magic: Each point multiplies magic damage by 0.2   Level:", magicmultpoints,
              "\n3: Ranged: Each point multiplies ranged damage by 0.2   Level:", rangedmultpoints,
              "\n4: Health: Each point adds 3 health    Level:", healthmultpoints,
              "\n5: Bartering: Bartering will be cheaper by 2% for every point   Level:", bartermultpoints)
# ------------------------------------------------------------------------------------------------------------------------ Skill Selection
        print("Which skill would you like to upgrade?")
        skillselection = input("Skill number to upgrade: ")
# ------------------------------------------------------------------------------------------------------------------------ Upgrade Skill 1
        if skillselection == "1":
            skillconfirm = input("Confirm Upgrade? : ")
            if skillconfirm == "Y" or skillconfirm == "y":
                points -= 1
                damagemultpoints += 1
                damagemult = damage + (damagemultpoints * 0.2)  # Calculates Melee Damage
                magicmult = damage + (magicmultpoints * 0.2)  # Calculates Magic Damage
                rangedmult = damage + (rangedmultpoints * 0.2)  # Calculates Ranged Damage
                totalhealth = basehealth + (healthmultpoints * 3)  # Calculates Health
                bartermult = price - (bartermultpoints * 2)  # Calculates Barter Prices
                if points == 0:
                    skillsconfirm = input("Continue? y/n: ")
                    if skillsconfirm == "Y" or skillsconfirm == "y":
                        save()
                        quest()
                    else:
                        # ------------------------------------------------------------------------------------------------ Reset Skills
                        print("Reset Skills?")
                        resetconfirm = input("Reset? y/n: ")
                        if resetconfirm == "Y" or resetconfirm == "y":
                            resetpoints = (damagemultpoints + magicmultpoints + rangedmultpoints + healthmultpoints + bartermultpoints)
                            damagemultpoints = 0
                            magicmultpoints = 0
                            rangedmultpoints = 0
                            healthmultpoints = 0
                            bartermultpoints = 0
                            points = points + resetpoints
                            skills()
                        else:
                            quest()
                else:
                    skills()
            else:
                # -------------------------------------------------------------------------------------------------------- Cancel
                print("\nCancelled! \n")
                skills()
        else:
            # ------------------------------------------------------------------------------------------------------------ Upgrade Skill 2
            if skillselection == "2":
                skillconfirm = input("Confirm Upgrade? : ")
                if skillconfirm == "Y" or skillconfirm == "y":
                    points -= 1
                    magicmultpoints += 1
                    damagemult = damage + (damagemultpoints * 0.2)
                    magicmult = damage + (magicmultpoints * 0.2)
                    rangedmult = damage + (rangedmultpoints * 0.2)
                    totalhealth = basehealth + (healthmultpoints * 3)
                    bartermult = price - (bartermultpoints * 2)
                    if points == 0:
                        skillsconfirm = input("Continue? y/n: ")
                        if skillsconfirm == "Y" or skillsconfirm == "y":
                            save()
                            quest()
                        else:
                            # -------------------------------------------------------------------------------------------- Reset Skills
                            print("Reset Skills?")
                            resetconfirm = input("Reset? y/n: ")
                            if resetconfirm == "Y" or resetconfirm == "y":
                                resetpoints = (damagemultpoints + magicmultpoints + rangedmultpoints + healthmultpoints + bartermultpoints)
                                damagemultpoints = 0
                                magicmultpoints = 0
                                rangedmultpoints = 0
                                healthmultpoints = 0
                                bartermultpoints = 0
                                points = points + resetpoints
                                skills()
                            else:
                                quest()
                    else:
                        skills()
                else:
                    # ---------------------------------------------------------------------------------------------------- Cancel
                    print("\nCancelled! \n")
                    skills()
            else:
                # -------------------------------------------------------------------------------------------------------- Upgrade Skill 3
                if skillselection == "3":
                    skillconfirm = input("Confirm Upgrade? : ")
                    if skillconfirm == "Y" or skillconfirm == "y":
                        points -= 1
                        rangedmultpoints += 1
                        damagemult = damage + (damagemultpoints * 0.2)
                        magicmult = damage + (magicmultpoints * 0.2)
                        rangedmult = damage + (rangedmultpoints * 0.2)
                        totalhealth = basehealth + (healthmultpoints * 3)
                        bartermult = price - (bartermultpoints * 2)
                        if points == 0:
                            skillsconfirm = input("Continue? y/n: ")
                            if skillsconfirm == "Y" or skillsconfirm == "y":
                                save()
                                quest()
                            else:
                                # ---------------------------------------------------------------------------------------- Reset Skills
                                print("Reset Skills?")
                                resetconfirm = input("Reset? y/n: ")
                                if resetconfirm == "Y" or resetconfirm == "y":
                                    resetpoints = (damagemultpoints + magicmultpoints + rangedmultpoints + healthmultpoints + bartermultpoints)
                                    damagemultpoints = 0
                                    magicmultpoints = 0
                                    rangedmultpoints = 0
                                    healthmultpoints = 0
                                    bartermultpoints = 0
                                    points = points + resetpoints
                                    skills()
                                else:
                                    quest()
                        else:
                            skills()
                    else:
                        # ------------------------------------------------------------------------------------------------ Cancel
                        print("\nCancelled! \n")
                        skills()
                else:
                    # ---------------------------------------------------------------------------------------------------- Upgrade Skill 4
                    if skillselection == "4":
                        skillconfirm = input("Confirm Upgrade? : ")
                        if skillconfirm == "Y" or skillconfirm == "y":
                            points -= 1
                            healthmultpoints += 1
                            damagemult = damage + (damagemultpoints * 0.2)
                            magicmult = damage + (magicmultpoints * 0.2)
                            rangedmult = damage + (rangedmultpoints * 0.2)
                            totalhealth = basehealth + (healthmultpoints * 3)
                            bartermult = price - (bartermultpoints * 2)
                            if points == 0:
                                skillsconfirm = input("Continue? y/n: ")
                                if skillsconfirm == "Y" or skillsconfirm == "y":
                                    save()
                                    quest()
                                else:
                                    # ------------------------------------------------------------------------------------ Reset Skills
                                    print("Reset Skills?")
                                    resetconfirm = input("Reset? y/n: ")
                                    if resetconfirm == "Y" or resetconfirm == "y":
                                        resetpoints = (damagemultpoints + magicmultpoints + rangedmultpoints + healthmultpoints + bartermultpoints)
                                        damagemultpoints = 0
                                        magicmultpoints = 0
                                        rangedmultpoints = 0
                                        healthmultpoints = 0
                                        bartermultpoints = 0
                                        points = points + resetpoints
                                        skills()
                                    else:
                                        quest()
                            else:
                                skills()
                        else:
                            # -------------------------------------------------------------------------------------------- Cancel
                            print("\nCancelled! \n")
                            skills()
                    else:
                        # ------------------------------------------------------------------------------------------------ Upgrade Skill 5
                        if skillselection == "5":
                            skillconfirm = input("Confirm Upgrade? : ")
                            if skillconfirm == "Y" or skillconfirm == "y":
                                points -= 1
                                bartermultpoints += 1
                                damagemult = damage + (damagemultpoints * 0.2)
                                magicmult = damage + (magicmultpoints * 0.2)
                                rangedmult = damage + (rangedmultpoints * 0.2)
                                totalhealth = basehealth + (healthmultpoints * 3)
                                bartermult = price - (bartermultpoints * 2)
                                if points == 0:
                                    skillsconfirm = input("Continue? y/n: ")
                                    if skillsconfirm == "Y" or skillsconfirm == "y":
                                        save()
                                        quest()
                                    else:
                                        # -------------------------------------------------------------------------------- Reset Skills
                                        print("Reset Skills?")
                                        resetconfirm = input("Reset? y/n: ")
                                        if resetconfirm == "Y" or resetconfirm == "y":
                                            resetpoints = (damagemultpoints + magicmultpoints + rangedmultpoints + healthmultpoints + bartermultpoints)
                                            damagemultpoints = 0
                                            magicmultpoints = 0
                                            rangedmultpoints = 0
                                            healthmultpoints = 0
                                            bartermultpoints = 0
                                            points = points + resetpoints
                                            skills()
                                        else:
                                            quest()
                                else:
                                    skills()
                            else:
                                # ---------------------------------------------------------------------------------------- Cancel
                                print("\nCancelled! \n")
                                skills()
# ------------------------------------------------------------------------------------------------------------------------ Error
                        else:
                            print("Error")
                            skills()


# ------------------------------------------------------------------------------------------------------------------------Random Events/ Story
def villageenter():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("In the village ", name, " finds a \n1. Blacksmith \n2. General Store \n3. Healer \n4. an Inn")
    option = input("Which option do you choose? : ")
    if option == "1":
        print(name, " visits the Village Blacksmith")
        questsave()
    if option == "2":
        print(name, " enters the Village General Store")
        questsave()
    if option == "3":
        print(name, " decides to visit the Village Healer")
        questsave()
    if option == "4":
        print(name, " enters the Inn")
        questsave()


# ------------------------------------------------------------------------------------------------------------------------ Skeleton Event
def skeleton():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou encounter a horde of undead skeletons... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print(name, " runs away from the skellies...\nThey try to chase you but cannot keep up")
        questsave()
    if option == "2":
        print(name, " decides to fight the skeletons")
        print(name, " attacks the skeletons")
        print(name, " deals ", whack, " damage!")
        print("The skeletons fall to bits")
        print(name, " wins the fight")
        questsave()


# ------------------------------------------------------------------------------------------------------------------------ Cave Event
def cave():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\n", name, "'s path leads you to a large cave... \nDo you?\n1. Enter?\n2. Flee?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print(name, " enters the dark dingy cave!\nScreams echo from beneath...")
        questsave()
    if option == "2":
        print(name, " decides not to go into the cave")
        print("It was probably for the better...")
        print(name, " continues on your journey!")
        questsave()


# ------------------------------------------------------------------------------------------------------------------------ Wizard
def wizard():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou encounter a wizard in his tower \nDo you?\n1. Flee?\n2. Talk?\n3. Fight")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You run away from the tower\nThe wizard doesn't care")
        questsave()
    if option == "2":
        print("You climb the tower to meet the wizard")
        print("He is friendly and heals you and increases your maximum health!")
        basehealth += 15
        questsave()
    if option == "3":
        print("For some fucking stupid reason you decide to fight the wizard")
        print("You attack the wizard")
        print("You deal ", whack, " damage!")
        print("The wizard blocks all damage with a spell")
        print("He shoots a fireball at you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Village Event
def village():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou reach a village \nDo you?\n1. Enter?\n2. Stay away?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You enter the village\nThe townsfolk greet you with open arms!")
        villageenter()
        questsave()
    if option == "2":
        print("You decide to stay away from the village")
        questsave()


# ------------------------------------------------------------------------------------------------------------------------ Witch Event
def witch():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
        questsave()
    if option == "2":
        print("For some fucking stupid reason you decide to fight the giant")
        print("You attack the giant")
        print("You deal ", whack, " damage!")
        print("The giant has 500 health")
        print("The giant flattens you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Forest Event
def forest():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou reach a forest \nDo you?\n1. Enter?\n2. Go around?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You enter the forest\nEerie sounds surround you")
        questsave()
    if option == "2":
        print("You go around because you are a fucking pussy")
        questsave()


# ------------------------------------------------------------------------------------------------------------------------ Bandits Event
def bandits():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou encounter a group of bandits waiting on the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You flee from the bandits!\nThey don't care because you are poor")
        questsave()
    if option == "2":
        print("You decide to fight the group of bandits")
        print("You attack the bandits")
        print("You deal ", whack, " damage!")
        print("You can't aim for shit and miss them entirely")
        print("The bandits slaughter you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Chest Event
def chest():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou find a chest on the side of the road... \nDo you?\n1. Open?\n2. Ignore?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You open the chest!\nIt does not see you jump into the bushes and walks away.")
        questsave()
    if option == "2":
        print("You open the chest!")
        print("A goblin jumps out!")
        print("You deal ", whack, " damage!")
        print("The goblin is too small!")
        print("The goblin stabs you!")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Troll Event
def troll():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou encounter a troll walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You flee from the troll you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
        questsave()
    if option == "2":
        print("For some fucking stupid reason you decide to fight the troll")
        print("You attack the troll")
        print("You deal ", whack, " damage!")
        print("The troll has 500 health")
        print("The troll flattens you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Bear Event
def bear():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nA bear runs out at you from the forest \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You flee from the bear and climb up a tree\nIt cannot follow you into the tree and soon walks away.")
        questsave()
    if option == "2":
        print("For some fucking stupid reason you decide to fight the bear")
        print("You attack the bear")
        print("You deal ", whack, " damage!")
        print("The bear has 500 health")
        print("The bear bites your head off")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Spider Event
def spider():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nA giant spider scales down from a tree in front of you \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You run away because you don't like creepy crawlies\nIt tries to shoot spiderwebs at you, It misses.")
        questsave()
    if option == "2":
        print("You decide to stab the spider")
        print("You stab it")
        print("You deal ", whack, " damage!")
        print("The spider has 200 health")
        print("The spider bites you")
        print("You are paralyzed")
        print("The spider eats you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Dragon Event
def dragon():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nA dragon lands in front of you! \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You flee from the dragon like a normal person\nIt seems to only have landed for a rest and soon flies away.")
        questsave()
    if option == "2":
        print("You seem to think that you are dragonborn and try to fight the dragon")
        print("You attack the dragon")
        print("You deal 0 damage!")
        print("The dragon has 10000 health")
        print("Your attack doesn't even leave a scratch")
        print("The dragon disintegrates you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Vampire Event
def vampire():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nA bat flies by... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You run away from a bat\nIt ignores you and flies away")
        questsave()
    if option == "2":
        print("For some fucking stupid reason you decide to attack the bat")
        print("You attack the bat")
        print("You deal ", whack, " damage!")
        print("The bat transforms to a vampire")
        print("The vampire bites you")
        print("You turn into a vampire...")
        print("The sun comes up")
        print("You die!")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Werewolf Event
def werewolf():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou meet a man as the night falls. \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You run away from the man\nHe does not care.")
        questsave()
    if option == "2":
        print("For some fucking stupid reason you decide to fight the man")
        print("You attack the man")
        print("You deal ", whack, " damage!")
        print("The man has 100 health")
        print("The man transforms into a werewolf")
        print("He rips you to pieces")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Zombie Event
def zombie():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou are ambushed by a group of zombies! The look very weak \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print(
            "You flee from the zombies even though you are much stronger than them...\nThe zombies are much slower than you and you escape with ease.")
        questsave()
    if option == "2":
        print("You decide stand your ground fight the zombies")
        print("You attack the zombies")
        print("You deal ", whack, " damage!")
        print("The zombies just get demolished by you")
        print("You escape unscathed")
        questsave()


# ------------------------------------------------------------------------------------------------------------------------ Giant Event
def giant():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
        print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
        questsave()
    if option == "2":
        print("For some fucking stupid reason you decide to fight the giant")
        print("You attack the giant")
        print("You deal ", whack, " damage!")
        print("The giant has 500 health")
        print("The giant flattens you")
        print("You die.")
        print("GAME OVER!")
        exit()


# ------------------------------------------------------------------------------------------------------------------------ Crossroads Event
def crossroads():
    global level
    global damagemultpoints
    global magicmultpoints
    global rangedmultpoints
    global healthmultpoints
    global bartermultpoints
    global points
    global damagemult
    global magicmult
    global rangedmult
    global totalhealth
    global bartermult
    global resetpoints
    global whack
    global damage
    global basehealth
    global money
    global name
    level += 1
    print("Level:", level)
    save()
    print("\nYou reach a fork in the road! \nWhich direction do you go? ")
    direction = input("Left or Right? : ")
    if direction == "left" or direction == "Left" or direction == "l" or direction == "L":
        print("You decide to take the Left Road...")
        questsave()
    else:
        print("You opt for the right road...")
        questsave()


def begin():
    print("You set off on your journey of adventure!")
    questsave()


# ------------------------------------------------------------------------------------------------------------------------ Random Event Generator
def quest():
    global questlevel
    global questchoice
    quests = ["1", "1", "1", "1", "1", "1",                                                                                # Skeleton
              "2", "2", "2", "2", "2", "2", "2",                                                                           # Cave
              "3", "3", "3",                                                                                               # Wizard
              "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4",                                                       # Village
              "5", "5", "5",                                                                                               # Witch
              "6", "6", "6", "6", "6",                                                                                     # Forest
              "7", "7", "7",                                                                                               # Bandits
              "8", "8", "8", "8", "8", "8",                                                                                # Chest
              "9", "9",                                                                                                    # Troll
              "10", "10",                                                                                                  # Bear
              "11", "11", "11", "11",                                                                                      # Spider
              "12",                                                                                                        # Dragon
              "13", "13", "13",                                                                                            # Vampire
              "14", "14", "14", "14", "14", "14", "14",                                                                    # Zombie
              "15", "15",                                                                                                  # Werewolf
              "16", "16",                                                                                                  # Giant
              "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17"]  # Crossroads
    questchoice = secrets.choice(quests)
    questlevel = questchoice
    if questchoice == "1":
        skeleton()

    elif questchoice == "2":
        cave()

    elif questchoice == "3":
        wizard()

    elif questchoice == "4":
        village()

    elif questchoice == "5":
        witch()

    elif questchoice == "6":
        forest()

    elif questchoice == "7":
        bandits()

    elif questchoice == "8":
        chest()

    elif questchoice == "9":
        troll()

    elif questchoice == "10":
        bear()

    elif questchoice == "11":
        spider()

    elif questchoice == "12":
        dragon()

    elif questchoice == "13":
        vampire()

    elif questchoice == "14":
        zombie()

    elif questchoice == "15":
        werewolf()

    elif questchoice == "16":
        giant()

    elif questchoice == "17":
        crossroads()


# ----------------------------------------------------------------------------------------------------------------------- Begin
print("Welcome to the Game!")
startpage()
