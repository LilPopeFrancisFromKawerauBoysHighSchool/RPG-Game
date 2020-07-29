#-------------------------------------------------------------Variables-------------------------------------------------Variables
money = 0
points = 5
damagemult = 0
magicmult = 0
rangedmult = 0
healthmult = 0
bartermult = 0
#-------------------------------------------------------------Startpage-------------------------------------------------Startpage
def startPage(): #Start of the game...
    print("Press Y to continue...")
    start = input()
    if start == "Y" or start == "y":
        print("Welcome!")
        characterchoice()
    else:
        startPage()
#-----------------------------------------------------------Character Choice Menu---------------------------------------Character Choice Menu
def characterchoice():
    print("Choose your character!")
    print("Options: \n 1. Fighter: Small damage, Melee Damage, Big health! \n 2. Mage: Decent Damage, Magic Damage, Moderate Health! \n 3. Archer: Average Damage, Ranged Damage, Decent Health!  \n 4. Assassin: Crazy Damage, Melee & Ranged Damage, Low Health! \n")
    character = input("Character Number: ")
#----------------------------------------------------------Character Option 1: Fighter----------------------------------Character Option 1: Fighter
    if character == "1":
        charactertype = "Fighter"
        damage = 8
        health = 20
        money = 100
        points = 5
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", health)
        print("Coins: ", money)
        confirm = input("Confirm Class? y/n: ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Sword Equipped! Damage:", damage)
            print("Basic Armor Equipped! Damage:", health)
            skills()
        else:
            print("\nCancelled! \n")
            characterchoice()
#----------------------------------------------------------Character Option 2: Mage-------------------------------------Character Option 2: Mage
    else:
        if character == "2":
            charactertype = "Mage"
            damage = 12
            health = 15
            money = 100
            points = 5
            print("\nCharacter Class Selected: ", charactertype)
            print("Damage:", damage)
            print("Health:", health)
            print("Coins: ", money)
            confirm = input("Confirm Class? : ")
            if confirm == "Y" or confirm == "y":
                print("\nClass Selected!\n")
                print("Basic Staff Equipped! Damage:", damage)
                print("Basic Robes Equipped! Damage:", health)
                skills()
            else:
                print("\nCancelled! \n")
                characterchoice()
#------------------------------------------------------------Character Option 3: Archer---------------------------------Character Option 3: Archer
        else:
            if character == "3":
                charactertype = "Archer"
                damage = 10
                health = 18
                money = 100
                points = 5
                print("\nCharacter Class Selected: ", charactertype)
                print("Damage:", damage)
                print("Health:", health)
                print("Coins: ", money)
                confirm = input("Confirm Class? : ")
                if confirm == "Y" or confirm == "y":
                    print("\nClass Selected!\n")
                    print("Basic Bow Equipped! Damage:", damage)
                    print("Basic Light Armor Equipped! Health:", health)
                    skills()
                else:
                    print("\nCancelled! \n")
                    characterchoice()
#--------------------------------------------------------------Character Option 4: Assassin-----------------------------Character Option 4: Assassin
            else:
                if character == "4":
                    charactertype = "Assassin"
                    damage = 18
                    health = 10
                    money = 100
                    points = 5
                    print("\nCharacter Class Selected: ", charactertype)
                    print("Damage:", damage)
                    print("Health:", health)
                    print("Coins: ", money)
                    confirm = input("Confirm Class? : ")
                    if confirm == "Y" or confirm == "y":
                        print("\nClass Selected!\n")
                        print("Basic Knife Equipped! Damage:", damage)
                        print("Basic Stealth Armor Equipped! Damage:", health)
                        skills()
                    else:
                        print("\nCancelled! \n")
                        characterchoice()
                else:
                    print("\nNot Valid \n")
                    characterchoice()
#----------------------------------------------------------------------Skill Menu   ------------------------------------Skill Menu

def skills():
  print('\033[1m' + "\nHere you can spend skill points!"+'\033[0m')
  print("Points Available: ", points)
  print("Skill Trees: \n1: Damage: Each point multiplies damage by 0.2 \n2: Magic: Each point multiplies magic damage by 0.2 \n3: Ranged: Each point multiplies ranged damage by 0.2\n4: Health: Each point adds 3 health \n5: Bartering: Bartering will be cheaper by 2% for every point")
#--------------------------------------------------------------Skill Selection------------------------------------------Skill Selection
  print("Which skill would you like to upgrade?")
  skillselection = input("Skill number to upgrade: ")
  if skillselection == "1":
    skillconfirm = input("Confirm Class? : ")
    if skillconfirm == "Y" or skillconfirm == "y":
        points -= 1
        damagemult += 1
        skills()
    else:
        print("\nCancelled! \n")
        skills()
  else:
      if skillselection == "2":
        skillconfirm = input("Confirm Class? : ")
        if skillconfirm == "Y" or skillconfirm == "y":
            points -= 1
            magicmult += 1
            skills()
        else:
            print("\nCancelled! \n")
            skills()
      else:
        if skillselection == "3":
           skillconfirm = input("Confirm Class? : ")
           if skillconfirm == "Y" or skillconfirm == "y":
              points -= 1
              rangedmult += 1
              skills()
           else:
              print("\nCancelled! \n")
              skills()
        else:
           if skillselection == "4":
              skillconfirm = input("Confirm Class? : ")
              if skillconfirm == "Y" or skillconfirm == "y":
                 points -= 1
                 healthmult += 1
                 skills()
              else:
                 print("\nCancelled! \n")
                 skills()
           else:
               if skillselection == "5":
                  skillconfirm = input("Confirm Class? : ")
                  if skillconfirm == "Y" or skillconfirm == "y":
                     points -= 1
                     bartermult += 1
                     skills()
                  else:
                     print("\nCancelled! \n")
                     skills()
               else:
                     print("Error")
                     skills()


#-----------------------------------------------------------------------------------------------------------------------
print("Welcome to the Game!")
startPage()

