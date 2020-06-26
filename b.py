money = 0
def startPage(): #Start of the game...
    print("Press Y to continue...")
    start = input()
    if start == "Y" or start == "y":
        print("Welcome!")
        characterchoice()
    else:
        startPage()

def characterchoice():
    print("Choose your character!")
    print("Options: \n 1. Fighter: Small damage, Melee Damage, big health! \n 2. Mage: Decent Damage, Magic Damage, Moderate Health! \n 3. Archer: Average Damage, Ranged Damage, Decent Health!  \n 4. Assassin: Crazy Damage, Melee & Ranged Damage, Low Health! \n")
    character = input("Character Number: ")
    if character == "1":
        charactertype = "Fighter"
        damage = 8
        health = 20
        money = 100
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", health)
        print("Coins: ", money)
        confirm = input("Confirm Class? y/n: ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Sword Equipped! Damage:", damage)
            print("Basic Armor Equipped! Damage:", health)
        else:
            print("\nCancelled! \n")
            characterchoice()
    else:
        if character == "2":
            charactertype = "Mage"
            damage = 12
            health = 15
            money = 100
            print("\nCharacter Class Selected: ", charactertype)
            print("Damage:", damage)
            print("Health:", health)
            print("Coins: ", money)
            confirm = input("Confirm Class? : ")
            if confirm == "Y" or confirm == "y":
                print("\nClass Selected!\n")
                print("Basic Staff Equipped! Damage:", damage)
                print("Basic Robes Equipped! Damage:", health)
            else:
                print("\nCancelled! \n")
                characterchoice()
        else:
            if character == "3":
                charactertype = "Archer"
                damage = 10
                health = 18
                money = 100
                print("\nCharacter Class Selected: ", charactertype)
                print("Damage:", damage)
                print("Health:", health)
                print("Coins: ", money)
                confirm = input("Confirm Class? : ")
                if confirm == "Y" or confirm == "y":
                    print("\nClass Selected!\n")
                    print("Basic Bow Equipped! Damage:", damage)
                    print("Basic Light Armor Equipped! Health:", health)
                else:
                    print("\nCancelled! \n")
                    characterchoice()
            else:
                if character == "4":
                    charactertype = "Assassin"
                    damage = 18
                    health = 10
                    money = 100
                    print("\nCharacter Class Selected: ", charactertype)
                    print("Damage:", damage)
                    print("Health:", health)
                    print("Coins: ", money)
                    confirm = input("Confirm Class? : ")
                    if confirm == "Y" or confirm == "y":
                        print("\nClass Selected!\n")
                        print("Basic Knife Equipped! Damage:", damage)
                        print("Basic Stealth Armor Equipped! Damage:", health)
                    else:
                        print("\nCancelled! \n")
                        characterchoice()
                else:
                    print("\nNot Valid \n")
                    characterchoice()

print("Welcome to the Game!")
startPage()

