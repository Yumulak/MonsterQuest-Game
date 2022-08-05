import characters
import newRPS
import os
import Choices


def homepage():
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


def bountyBoard():
    print(f'''
    ___________________________________________________________________
    |                |                |              |                 |
    |-----{characters.wolfman.name}----|-----{characters.gryphon.name}----|-----{characters.golem.name}----|-----{characters.basilisk.name}----|
    |  ~~~~~~~~~~~~  |  ~~~~~~~~~~~~  |  ~~~~~~~~~~  |  ~~~~~~~~~~~~~  |
    |  ~~~~~~~~~~~~  |  ~~~~~~~~~~~~  |  ~~~~~~~~~~  |  ~~~~~~~~~~~~~  |
    |________________|________________|______________|_________________|
    ''')


def story():
    while True:
        # ask for input for play or quit
        playOrQuit = input("\nReady to play? (Y/N) ")
        if playOrQuit[0].lower() == "n":
            break
# ask for character choice
        Choices.characterChoice()
# ask for weapon class choice
        Choices.weaponChoice()
#start in town
        print(
            f"\nYou are a(n) {Choices.myName} in a small village with a talent for fighting and you feel a calling to adventure from your home...")
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
        bountyBoard()
        Choices.monsterChoice()
        input("\nPRESS ENTER TO CONTINUE\n")
# enter tavern or go to hunt
        Choices.tavernChoice()
        print("You begin down the road toward the last known location of the beast.")
        input("\nPRESS ENTER TO CONTINUE\n")
        print("A little while down the path, you come across a mysterious hut which seems to call to you..")
        input("\nPRESS ENTER TO CONTINUE\n")
# enter hut or leave
        Choices.hutChoice()
        print("You continue towards your bounty.")
        input("\nPRESS ENTER TO CONTINUE\n")
        print("A while later, a group of bandits stops you and demands all of your coin or else..")
# bandit fight
        input("\nPRESS ENTER TO CONTINUE\n")
        Choices.banditChoice()
        input("\nPRESS ENTER TO CONTINUE\n")
        os.system("cls" if os.name == "nt" else "clear")
# monster fight
        print("You continue down the path towards an eerie looking mountain..")
        print("Finally, you approach a cobbled bridge.. ")
        input("\nPRESS ENTER TO CONTINUE\n")
        print("There is a broken down caravan in the middle of the bridge.. you hear something moving around behind the caravan..")
        input("\nPRESS ENTER TO CONTINUE\n")
        print(f"Whatever it is notices you and comes out from behind the caravan.. before you now stands the {Choices.monsterName} you are hunting.. it appears to be.. {Choices.monsterHeight}.")
        newRPS.MonsterRPS()
        os.system("cls" if os.name == "nt" else "clear")
        newGame = input("\nHunt again? ")

# yes/no to restart game
        if newGame[0].lower() == "n":
            break

    print("\nGoodbye and thanks for all the fish! =) ")
