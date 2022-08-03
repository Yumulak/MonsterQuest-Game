import characters
import weapons
import newRPS
import os

# enemies
Golem = characters.Golem("Golem", 300, 100, "at least four horses tall")
Basilisk = characters.Wyvern(
    "Basilisk", 250, 150, "at least three horses tall")
Gryphon = characters.Gryphon(
    "Gryphon", 200, 200, "at least two of those caravans tall")
Wolfman = characters.Werewolf("Wolfman", 150, 250, "at least two horses tall")

fighter = "drunken fighter"
fighterHp = 100

fightRounds = [123]

# monster name list
monsterNames = [Wolfman.name, Basilisk.name, Gryphon.name, Golem.name]

# weapons

# characters
orc = characters.Orc("Orc", 200)
elf = characters.Elf("Elf", 100)
human = characters.Human("Human", 150)

# print game title and ask the user to start or quit
while True:
    print('''



   ▄▄▄▄███▄▄▄▄    ▄██████▄  ███▄▄▄▄      ▄████████     ███        ▄████████    ▄████████ ████████▄   ███    █▄     ▄████████    ▄████████     ███     
 ▄██▀▀▀███▀▀▀██▄ ███    ███ ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███   ███    ███ ███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄ 
 ███   ███   ███ ███    ███ ███   ███   ███    █▀     ▀███▀▀██   ███    █▀    ███    ███ ███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██ 
 ███   ███   ███ ███    ███ ███   ███   ███            ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀ 
 ███   ███   ███ ███    ███ ███   ███ ▀███████████     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███     
 ███   ███   ███ ███    ███ ███   ███          ███     ███       ███    █▄  ▀███████████ ███    ███  ███    ███   ███    █▄           ███     ███     
 ███   ███   ███ ███    ███ ███   ███    ▄█    ███     ███       ███    ███   ███    ███ ███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███     
  ▀█   ███   █▀   ▀██████▀   ▀█   █▀   ▄████████▀     ▄████▀     ██████████   ███    ███  ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀   
                                                                              ███    ███                                                              
                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ''')

# ask for input for play or quit
    playOrQuit = input("\nReady to play? (Y/N) ")

    if playOrQuit[0].lower() == "n":
        break

    while True:
        print(f"\nCharacters: | Orc | Elf | Human |")
        playerCharacter = input("Choose your race: ")

        if playerCharacter[0].lower() == "o":
            myHp = orc.hp
            myName = orc.name
        elif playerCharacter[0].lower() == "h":
            myHp = human.hp
            myName = human.name
        elif playerCharacter[0].lower() == "e":
            myHp = elf.hp
            myName = elf.name

        else:
            print("\nNo correct character was chosen or name was misspelled.\n")
            continue

# ask for weapon class choice
        print(f"\nWeapon Classes: | Sword and Shield | Spear | Axe | Bow and Arrow | Sorcery |")
        weaponClass = input("What weapon class will you use? ")
        if weaponClass == "":
            print("\nNo correct weapon choice was entered or name was misspelled.\n")
            continue
        elif weaponClass[:2].lower() == "sw":
            myWpn = weapons.swordAndShield
        elif weaponClass[:2].lower() == "sp":
            myWpn = weapons.spear
        elif weaponClass[0].lower() == "a":
            myWpn = weapons.axe
        elif weaponClass[0].lower() == "b":
            myWpn = weapons.bow
        elif weaponClass[:2].lower() == "so":
            myWpn = weapons.sorcery
        else:
            print("\nNo correct weapon choice was entered or name was misspelled.\n")
            continue
#start in town
        print(
            f"\nYou are a(n) {myName} in a small village with a talent for fighting and you feel a calling to adventure from your home...")

        input("\nPRESS ENTER TO CONTINUE\n")
        os.system("cls" if os.name == "nt" else "clear")
        print("There is a bounty board at the tavern, you hope to find adventure there.")

        input("\nPRESS ENTER TO CONTINUE\n")
# encounter drunken fighters
        print("You approach and there is a drunken group of men fighting for coin outside, they challenge you..")
        print("\nYou need the coin and decide to fight.")
        newRPS.bareHandRPS()
        input("\nPRESS ENTER TO CONTINUE\n")
        os.system("cls" if os.name == "nt" else "clear")
# approach bounty board
        print("After dusting yourself off, you approach the bounty board, there are four postings up..")

        input("\nPRESS ENTER TO CONTINUE\n")
# monster choice
        print(f'''
        ___________________________________________________________________
        |                |                |              |                 |
        |----{Wolfman.name}----|-----{Gryphon.name}----|-----{Golem.name}----|------{Basilisk.name}-----|
        |  ~~~~~~~~~~~~  |  ~~~~~~~~~~~~  |  ~~~~~~~~~~  |  ~~~~~~~~~~~~~  |
        |  ~~~~~~~~~~~~  |  ~~~~~~~~~~~~  |  ~~~~~~~~~~  |  ~~~~~~~~~~~~~  |
        |________________|________________|______________|_________________|
        ''')
        while True:
            print("\nWHICH BEAST WILL YOU HUNT?")
            monsterChoice = input("ENTER A MONSTER NAME: ")

            if monsterChoice == "":
                print("\nYou did not enter a monster name. Try again.")
                continue
            elif monsterChoice == "g":
                whatG = input("Gryphon or Golem? ")
                if whatG[:2].lower() == "gr":
                    monsterName = Gryphon.name
                    monsterHp = Gryphon.hp
                    monsterDmg = Gryphon.dmg
                    monsterHeight = Gryphon.height

                elif whatG[:2].lower() == "go":
                    monsterName = Gryphon.name
                    monsterHp = Gryphon.hp
                    monsterDmg = Gryphon.dmg
                    monsterHeight = Gryphon.height
                else:
                    print("You did not enter a monster name. Try again.")
                    continue
                break
            elif monsterChoice[:2].lower() == "go":
                monsterName = Golem.name
                monsterHp = Golem.hp
                monsterDmg = Golem.dmg
                monsterHeight = Golem.height
                break
            elif monsterChoice[0].lower() == "b":
                monsterName = Basilisk.name
                monsterHp = Basilisk.hp
                monsterDmg = Basilisk.dmg
                monsterHeight = Basilisk.height
                break
            elif monsterChoice[:2].lower() == "gr":
                monsterName = Gryphon.name
                monsterHp = Gryphon.hp
                monsterDmg = Gryphon.dmg
                monsterHeight = Gryphon.height
                break
            elif monsterChoice[0].lower() == "w":
                monsterName = Wolfman.name
                monsterHp = Wolfman.hp
                monsterDmg = Wolfman.dmg
                monsterHeight = Wolfman.height
                break
            else:
                print("\nNo correct choice was entered or name was misspelled.\n")
                continue
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nYou will hunt the {monsterName}...")

        input("\nPRESS ENTER TO CONTINUE\n")
# enter tavern or go to hunt
        while True:
            tavernChoice = input(
                "Have a drink at the tavern or begin the hunt now? (Drink/Hunt) ")
            if tavernChoice == "":
                print("\nNo correct choice was entered or name was misspelled.\n")
                continue
            elif tavernChoice[0].lower() == "d":
                print("You enter the tavern.")

                input("\nPRESS ENTER TO CONTINUE\n")

                print("You end up drinking too much and pass out.")

                input("\nPRESS ENTER TO CONTINUE\n")

                print(
                    "When you wake it is night and you must hurry in order to catch your beast..")
                break

        print("You begin down the road toward the last known location of the beast.")

        input("\nPRESS ENTER TO CONTINUE\n")

        print("A little while down the path, you come across a mysterious hut which seems to call to you..")

        input("\nPRESS ENTER TO CONTINUE\n")
# enter hut or leave
        hutChoice = input("Will you enter the hut or press on? (Y/N)")
        if hutChoice == "":
            print("\nNo correct choice was entered or name was misspelled.\n")
        if (hutChoice[0].lower() == "e") or (hutChoice[0].lower() == "y"):
            print("You enter the hut..")
            input("\nPRESS ENTER TO CONTINUE\n")
            print(
                "You wake up.. back in your home in your village, as if you never left..")
            break

        print("You continue towards your bounty.")

        input("\nPRESS ENTER TO CONTINUE\n")

        print("A while later, a group of bandits stops you and demands all of your coin or else..")
# bandit fight
        input("\nPRESS ENTER TO CONTINUE\n")
        while True:
            banditChoice = input(
                "Fight the bandits or give up your coin? (Fight/Give Up) ")

            if banditChoice == "":
                print("\nNo correct choice was entered or name was misspelled.\n")

            elif banditChoice[0].lower() == "f":
                print("You fight the bandits.. ")
                newRPS.RPS()
                break
            elif banditChoice[0].lower() == "g":
                print("You give the bandits all of your coin and they let you pass..")
                break
            else:
                print("\nNo correct choice was entered or name was misspelled.\n")
                continue
        input("\nPRESS ENTER TO CONTINUE\n")
        os.system("cls" if os.name == "nt" else "clear")
        print("You continue down the path towards an eerie looking mountain..")
        print("Finally, you approach a cobbled bridge.. ")
        input("\nPRESS ENTER TO CONTINUE\n")
        print("There is a broken down caravan in the middle of the bridge.. you hear something moving around behind the caravan..")
        input("\nPRESS ENTER TO CONTINUE\n")
        print(
            f"Whatever it is notices you and comes out from behind the caravan.. before you now stands the {monsterName} you are hunting.. it appears to be.. {monsterHeight}.")
        newRPS.MonsterRPS()
        break
    os.system("cls" if os.name == "nt" else "clear")
    newGame = input("\nHunt again? ")

# yes/no to restart game
    if newGame[0].lower() == "n":
        break

print("\nGoodbye and thanks for all the fish! =) ")
