import characters
import os
import weapons
from newRPS import RPS
import Story

# class Choice:
#     def __init__(self, choice):
#         self.choice = choice

#     def fightOrFlee(self, choice):
#         pass

# class monsterChoice(self, choice):
#     def __init__(self, choice):
#         super().__init__()
#         self.choice = choice


# global variables for use in story
monsterName = "name"
monsterHp = 0
monsterDmg = 0
monsterHeight = 0


def monsterChoice():
    global monsterName
    global monsterHp
    global monsterDmg
    global monsterHeight

    while True:
        print("\nWHICH BEAST WILL YOU HUNT?")
        Choice = input("ENTER A MONSTER NAME: ")

        if Choice == "":
            print("\nYou did not enter a monster name. Try again.")
            continue
        elif Choice == "g":
            whatG = input("Gryphon or Golem? ")
            if whatG[:2].lower() == "gr":
                monsterName = characters.gryphon.name
                monsterHp = characters.gryphon.hp
                monsterDmg = characters.gryphon.dmg
                monsterHeight = characters.gryphon.height

            elif whatG[:2].lower() == "go":
                monsterName = characters.golem.name
                monsterHp = characters.golem.hp
                monsterDmg = characters.golem.dmg
                monsterHeight = characters.golem.height
            else:
                print("You did not enter a monster name. Try again.")
                continue
            break
        elif Choice[:2].lower() == "go":
            monsterName = characters.golem.name
            monsterHp = characters.golem.hp
            monsterDmg = characters.golem.dmg
            monsterHeight = characters.golem.height
            break
        elif Choice[0].lower() == "b":
            monsterName = characters.basilisk.name
            monsterHp = characters.basilisk.hp
            monsterDmg = characters.basilisk.dmg
            monsterHeight = characters.basilisk.height
            break
        elif Choice[:2].lower() == "gr":
            monsterName = characters.gryphon.name
            monsterHp = characters.gryphon.hp
            monsterDmg = characters.gryphon.dmg
            monsterHeight = characters.gryphon.height
            break
        elif Choice[0].lower() == "w":
            monsterName = characters.wolfman.name
            monsterHp = characters.wolfman.hp
            monsterDmg = characters.wolfman.dmg
            monsterHeight = characters.wolfman.height
            break
        else:
            print("\nNo correct choice was entered or name was misspelled.\n")
            continue
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\nYou will hunt the {monsterName}...")


def tavernChoice():
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
        else:
            break


# global variables for use in story
myName = "name"
myHp = 0


def characterChoice():
    global myName
    global myHp

    while True:
        print(f"\nCharacters: | Orc | Elf | Human |")
        playerCharacter = input("Choose your race: ")

        if playerCharacter[0].lower() == "o":
            myHp = characters.orc.hp
            myName = characters.orc.name
            return myName, myHp
        elif playerCharacter[0].lower() == "h":
            myHp = characters.human.hp
            myName = characters.human.name
            return myName, myHp
        elif playerCharacter[0].lower() == "e":
            myHp = characters.elf.hp
            myName = characters.elf.name
            return myName, myHp
        else:
            print("\nNo correct character was chosen or name was misspelled.\n")
            continue


def weaponChoice():
    while True:
        print(f"\nWeapon Classes: | Sword and Shield | Spear | Axe | Bow and Arrow | Sorcery |")
        weaponClass = input("What weapon class will you use? ")
        if weaponClass == "":
            print("\nNo correct weapon choice was entered or name was misspelled.\n")
            continue
        elif weaponClass[:2].lower() == "sw":
            myWpn = weapons.swordAndShield
            break
        elif weaponClass[:2].lower() == "sp":
            myWpn = weapons.spear
            break
        elif weaponClass[0].lower() == "a":
            myWpn = weapons.axe
            break
        elif weaponClass[0].lower() == "b":
            myWpn = weapons.bow
            break
        elif weaponClass[:2].lower() == "so":
            myWpn = weapons.sorcery
            break
        else:
            print("\nNo correct weapon choice was entered or name was misspelled.\n")
            continue


def banditChoice():
    while True:
        banditChoice = input(
            "Fight the bandits or give up your coin? (Fight/Give Up) ")

        if banditChoice == "":
            print("\nNo correct choice was entered or name was misspelled.\n")

        elif banditChoice[0].lower() == "f":
            print("You fight the bandits.. ")
            RPS()
            break
        elif banditChoice[0].lower() == "g":
            print("You give the bandits all of your coin and they let you pass..")
            break
        else:
            print("\nNo correct choice was entered or name was misspelled.\n")
            continue


def hutChoice():
    while True:
        hutChoice = input("Will you enter the hut or press on? (Y/N)")
        if (hutChoice == ""):
            print("\nNo correct choice was entered or name was misspelled.\n")
            continue
        elif (hutChoice[0].lower() == "e") or (hutChoice[0].lower() == "y"):
            print("You enter the hut..")
            input("\nPRESS ENTER TO CONTINUE\n")
            print(
                "You wake up.. back in your home in the village, as if you never left..")
            os.system("cls" if os.name == "nt" else "clear")
            Story.story()
        else:
            break
