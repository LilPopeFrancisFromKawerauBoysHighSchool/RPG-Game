import secrets
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
  resetpoints = (damagemultpoints+magicmultpoints+rangedmultpoints+healthmultpoints+bartermultpoints)
  if points == 0:
     quest()
  else:    
      print('\033[1m' + "\nHere you can spend skill points!"+'\033[0m')
      print("Points Available: ", points)
      print("Skill Trees: \n1: Damage: Each point multiplies damage by 0.2   Level:",damagemultpoints,"\n2: Magic: Each point multiplies magic damage by 0.2   Level:",magicmultpoints,"\n3: Ranged: Each point multiplies ranged damage by 0.2   Level:",rangedmultpoints,"\n4: Health: Each point adds 3 health    Level:",healthmultpoints,"\n5: Bartering: Bartering will be cheaper by 2% for every point   Level:",bartermultpoints)
    #--------------------------------------------------------------Skill Selection------------------------------------------Skill Selection
      print("Which skill would you like to upgrade?")
      skillselection = input("Skill number to upgrade: ")
      if skillselection == "1":
         skillconfirm = input("Confirm Upgrade? : ")
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
                  quest()
               else:
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
                     skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                  else:
                     quest()
            else:
                skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
         else:
             print("\nCancelled! \n")
             skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
      else:
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
                      quest()
                   else:
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
                         skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                      else:
                          quest()
                else:
                    skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
             else:
                print("\nCancelled! \n")
                skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
          else:
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
                        quest()
                     else:
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
                           skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                        else:
                           quest()
                  else:
                     skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
               else:
                  print("\nCancelled! \n")
                  skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
            else:
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
                           quest()
                        else:
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
                               skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                            else:
                               quest()
                     else:
                            skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                  else:
                     print("\nCancelled! \n")
                     skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
               else:
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
                               quest()
                            else:
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
                                   skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                                else:
                                    quest()
                         else:
                            skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                      else:
                         print("\nCancelled! \n")
                         skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)
                   else:
                         print("Error")
                         skills(damagemultpoints,magicmultpoints,rangedmultpoints,healthmultpoints,bartermultpoints,points,damagemult,magicmult,rangedmult,totalhealth,bartermult,resetpoints)

#----------------------------------------------------------------------Random Events/ Story  ---------------------------Random Events/ Story

def skeleton():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def cave():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def wizard():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def village():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def witch():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def forest():
    print("You reach a forest \nDo you?\n1. Enter?\n2. Go around?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You enter the forest\nEerie sounds surround you")
       quest()
    if option == "2":
       print("You go around because you are a fucking pussy")
       quest()
def bandits():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def chest():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def troll():
    print("You encounter a troll walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the troll you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the troll")
       print("You attack the troll")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The troll has 500 health")
       print("The troll flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def bear():
    print("A bear runs out at you from the forest \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the bear and climb up a tree\nIt cannot follow you into the tree and soon walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the bear")
       print("You attack the bear")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The bear has 500 health")
       print("The bear bites your head off")
       print("You die.")
       print("GAME OVER!")
       exit()
def spider():
    print("A giant spider scales down from a tree in front of you \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You run away because you don't like creepy crawlies\nIt tries to shoot spiderwebs at you, It misses.")
       quest()
    if option == "2":
       print("You decide to stab the spider")
       print("You stab it")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The spider has 200 health")
       print("The spider bites you")
       print("You are paralyzed")
       print("The spider eats you")
       print("You die.")
       print("GAME OVER!")
       exit()
def dragon():
    print("A dragon lands in front of you! \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the dragon like a normal person\nIt seems to only have landed for a rest and soon flies away.")
       quest()
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
def vampire():
    print("A bat flies by... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You run away from a bat\nIt ignores you and flies away")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to attack the bat")
       print("You attack the bat")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The bat transforms to a vampire")
       print("The vampire bites you")
       print("You turn into a vampire...")
       print("The sun comes up")
       print("You die!")
       print("GAME OVER!")
       exit()
def werewolf():
    print("You meet a man as the night falls. \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You run away from the man\nHe does not care.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the man")
       print("You attack the man")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The man has 100 health")
       print("The man transforms into a werewolf")
       print("He rips you to pieces")
       print("You die.")
       print("GAME OVER!")
       exit()
def zombie():
    print("You are ambushed by a group of zombies! The look very weak \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the zombies even though you are much stronger than them...\nThe zombies are much slower than you and you escape with ease.")
       quest()
    if option == "2":
       print("You decide stand your ground fight the zombies")
       print("You attack the zombies")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The zombies just get demolished by you")
       print("You escape unscathed")
       quest()


def giant():
    print("You encounter a giant walking across the road... \nDo you?\n1. Flee?\n2. Fight?\n")
    option = input("Which option do you choose? : ")
    if option == "1":
       print("You flee from the giant you fucking pussy!\nIt does not see you jump into the bushes and walks away.")
       quest()
    if option == "2":
       print("For some fucking stupid reason you decide to fight the giant")
       print("You attack the giant")
       print("You deal "+magicmult+damagemult+rangedmult+" damage!")
       print("The giant has 500 health")
       print("The giant flattens you")
       print("You die.")
       print("GAME OVER!")
       exit()
def crossroads():
    print("You reach a fork in the road! \nWhich direction do you go? ")
    direction = input("Left or Right? : ")
    if direction == "left" or direction == "Left" or direction == "l" or direction == "L"
       print("You decide to take the Left Road...")
       quest()
    else:
       print("You opt for the right road...")
       quest()


def begin():
    print("You set off on your journey of adventure!")

def quest ():
    quests = ["1","2","3","4","5","8","6","7","8","8","9","10","11","12","13","14","4","4","15","16","17","17","17"]
    questchoice = secrets.choice(quests)
    if questchoice == "1":
       skeleton()
    else:
        if questchoice == "2":
           cave()
        else:
            if questchoice == "3":
               wizard()
            else:
                if questchoice == "4":
                   village()
                else:
                    if questchoice == "5":
                       witch()
                    else:
                        if questchoice == "6":
                           forest()
                        else:
                            if questchoice == "7":
                               bandits()
                            else:
                                if questchoice == "8":
                                   chest()
                                else:
                                    if questchoice == "9":
                                       troll()
                                    else:
                                        if questchoicee == "10":
                                           bear()
                                        else:
                                            if questchoice == "11":
                                               spider()
                                            else:
                                                if questchoice == "12":
                                                   dragon()
                                                else:
                                                    if questchoice == "13":
                                                       vampire()
                                                    else:
                                                        if questchoice == "14":
                                                           zombie()
                                                        else:
                                                            if questchoice == "15":
                                                               zombie()
                                                            else:
                                                                if questchoice == "16":
                                                                   giant()
                                                                else:
                                                                    if questchoice == "17":
                                                                       crossroads()

#-----------------------------------------------------------------------------------------------------------------------
print("Welcome to the Game!")
startpage()
