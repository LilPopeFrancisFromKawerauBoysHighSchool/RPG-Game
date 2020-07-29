#-------------------------------------------------------------Variables-------------------------------------------------Variables
money = 0
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
#-------------------------------------------------------------Startpage-------------------------------------------------Startpage
def startpage(): #Start of the game...
    print("Press Y to continue...")
    start = input()
    if start == "Y" or start == "y":
        print("Welcome!")
        characterchoice()
    else:
        startpage()
#-----------------------------------------------------------Character Choice Menu---------------------------------------Character Choice Menu
def characterchoice():
    print("Choose your character!")
    print("Options: \n 1. Fighter: Small damage, Melee Damage, Big health! \n 2. Mage: Decent Damage, Magic Damage, Moderate Health! \n 3. Archer: Average Damage, Ranged Damage, Decent Health!  \n 4. Assassin: Crazy Damage, Melee & Ranged Damage, Low Health! \n")
    character = input("Character Number: ")
#----------------------------------------------------------Character Option 1: Fighter----------------------------------Character Option 1: Fighter
    if character == "1":
        charactertype = "Fighter"
        damage = 8
        basehealth = 20
        money = 100
        armor = 2
        points = 5
        print("\nCharacter Class Selected: ", charactertype)
        print("Damage:", damage)
        print("Health:", basehealth)
        print("Coins: ", money)
        confirm = input("Confirm Class? y/n: ")
        if confirm == "Y" or confirm == "y":
            print("\nClass Selected!\n")
            print("Basic Sword Equipped! Damage:", damage)
            print("Basic Armor Equipped! Damage:", armor)
            skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
        else:
            print("\nCancelled! \n")
            characterchoice()
#----------------------------------------------------------Character Option 2: Mage-------------------------------------Character Option 2: Mage
    else:
        if character == "2":
            charactertype = "Mage"
            damage = 12
            basehealth = 15
            money = 100
            armor = 2
            points = 5
            print("\nCharacter Class Selected: ", charactertype)
            print("Damage:", damage)
            print("Health:", basehealth)
            print("Coins: ", money)
            confirm = input("Confirm Class? : ")
            if confirm == "Y" or confirm == "y":
                print("\nClass Selected!\n")
                print("Basic Staff Equipped! Damage:", damage)
                print("Basic Robes Equipped! Damage:", armor)
                skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
            else:
                print("\nCancelled! \n")
                characterchoice()
#------------------------------------------------------------Character Option 3: Archer---------------------------------Character Option 3: Archer
        else:
            if character == "3":
                charactertype = "Archer"
                damage = 10
                basehealth = 18
                money = 100
                armor = 2
                points = 5
                print("\nCharacter Class Selected: ", charactertype)
                print("Damage:", damage)
                print("Health:", basehealth)
                print("Coins: ", money)
                confirm = input("Confirm Class? : ")
                if confirm == "Y" or confirm == "y":
                    print("\nClass Selected!\n")
                    print("Basic Bow Equipped! Damage:", damage)
                    print("Basic Light Armor Equipped! Health:", armor)
                    skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                else:
                    print("\nCancelled! \n")
                    characterchoice()
#--------------------------------------------------------------Character Option 4: Assassin-----------------------------Character Option 4: Assassin
            else:
                if character == "4":
                    charactertype = "Assassin"
                    damage = 18
                    basehealth = 10
                    money = 100
                    armor = 2
                    points = 5
                    print("\nCharacter Class Selected: ", charactertype)
                    print("Damage:", damage)
                    print("Health:", basehealth)
                    print("Coins: ", money)
                    confirm = input("Confirm Class? : ")
                    if confirm == "Y" or confirm == "y":
                        print("\nClass Selected!\n")
                        print("Basic Knife Equipped! Damage:", damage)
                        print("Basic Stealth Armor Equipped! Damage:", armor)
                        skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                    else:
                        print("\nCancelled! \n")
                        characterchoice()
                else:
                    print("\nNot Valid \n")
                    characterchoice()
#----------------------------------------------------------------------Skill Menu   ------------------------------------Skill Menu

def skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints):
  print('\033[1m' + "\nHere you can spend skill points!"+'\033[0m')
  print("Points Available: ", points)
  print("Skill Trees: \n1: Damage: Each point multiplies damage by 0.2   Level:",damagemultpoints,"\n2: Magic: Each point multiplies magic damage by 0.2   Level:",magicmultpoints,"\n3: Ranged: Each point multiplies ranged damage by 0.2   Level:",rangedmultpoints,"\n4: Health: Each point adds 3 health    Level:",healthmultpoints,"\n5: Bartering: Bartering will be cheaper by 2% for every point   Level:",bartermultpoints)
#--------------------------------------------------------------Skill Selection------------------------------------------Skill Selection
  print("Which skill would you like to upgrade?")
  skillselection = input("Skill number to upgrade: ")
  if skillselection == "1":
    skillconfirm = input("Confirm Class? : ")
    if skillconfirm == "Y" or skillconfirm == "y":
        points -= 1
        damagemultpoints += 1
        damagemult = damage + (damagemultpoints * 0.2)
        magicmult = damage + (magicmultpoints * 0.2)
        rangedmult = damage + (rangedmultpoints * 0.2)
        totalhealth = basehealth + (healthmultpoints * 3)
        bartermult = price - (bartermultpoints * 2)
        if points == 0:
           skillsconfirm = input("Continue? y/n: ")
           if skillsconfirm == "Y" or skillsconfirm == "y":
              exit()
        else:
            skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
    else:
        print("\nCancelled! \n")
        skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
  else:
      if skillselection == "2":
         skillconfirm = input("Confirm Class? : ")
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
                  exit()
            else:
                skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
         else:
            print("\nCancelled! \n")
            skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
      else:
        if skillselection == "3":
           skillconfirm = input("Confirm Class? : ")
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
                    exit()
              else:
                  skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
           else:
              print("\nCancelled! \n")
              skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
        else:
           if skillselection == "4":
              skillconfirm = input("Confirm Class? : ")
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
                       exit()
                 else:
                     skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
              else:
                 print("\nCancelled! \n")
                 skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
           else:
               if skillselection == "5":
                  skillconfirm = input("Confirm Class? : ")
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
                           exit()
                        else:
                           if skillsconfirm == "N" or skillsconfirm == "n":
                              print("Reset Skills?")
                              resetconfirm = input("Reset? y/n: ")
                              if resetconfirm == "Y" or resetconfirm == "y":
                                 damagemultpoints = 0
                                 magicmultpoints = 0
                                 rangedmultpoints = 0
                                 healthmultpoints = 0
                                 bartermultpoints = 0
                                 exit()
                              else:
                                   if resetconfirm == "N" or resetconfirm == "n":
                     else:
                         skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                  else:
                     print("\nCancelled! \n")
                     skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
               else:
                     print("Error")
                     skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)


#-----------------------------------------------------------------------------------------------------------------------
print("Welcome to the Game!")
startpage()

