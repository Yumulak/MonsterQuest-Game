import random

def RPS():

    options = ['swing', 'bash', 'stab']

    turns = 3
    print("\nBest two out of three wins the fight!")

    necessary_wins = int(turns/2) + 1

    player_wins = 0
    computer_wins = 0

    while True:

        while True:
            playerChoice = input(">>> swing, bash, stab: ")
            if playerChoice in options:
                break
            else:
                print("Come on, fight!")
                continue


        computerChoice = random.choice(options)

        if playerChoice == computerChoice:
            print('It is a tie')
        elif playerChoice == 'swing' and computerChoice == 'bash':
            print('The enemy wins this round, bash covers swing')
            computer_wins += 1
        elif playerChoice == 'swing' and computerChoice == 'stab':
            print('You win this round, swing smashes stab')
            player_wins += 1
        elif playerChoice == 'bash' and computerChoice == 'swing':
            print('You win this round, bash covers swing')
            player_wins += 1
        elif playerChoice == 'bash' and computerChoice == 'stab':
            print('The enemy wins this round, stab cut through bash')
            computer_wins += 1
        elif playerChoice == 'stab' and computerChoice == 'swing':
            print('The enemy wins this round, swing smashes stab')
            computer_wins += 1
        elif playerChoice == 'stab' and computerChoice == 'bash':
            print('You win this round, stab cut through bash')
            player_wins += 1

        if player_wins == necessary_wins or computer_wins == necessary_wins:
            break

    if player_wins > computer_wins:
        print(f'>>> You win the fight and defeated the bandits, keeping your coin!  ')
    else:
        print(f'>>> The bandits win and take your coin! <<<')

    print(f'>>> You scored: {player_wins} win(s) out of three!! <<<')

def bareHandRPS():

    options = ['uppercut', 'jab', 'block']

    turns = 3
    print("\nBest two out of three wins the fight!")

    necessary_wins = int(turns/2) + 1

    player_wins = 0
    computer_wins = 0

    while True:

        while True:
            playerChoice = input(">>> uppercut, jab, block: ")
            if playerChoice in options:
                break
            else:
                print("Come on, fight!")
                continue


        computerChoice = random.choice(options)

        if playerChoice == computerChoice:
            print('It is a tie')
        elif playerChoice == 'uppercut' and computerChoice == 'jab':
            print('The enemy wins this round, jabbing past your uppercut')
            computer_wins += 1
        elif playerChoice == 'uppercut' and computerChoice == 'block':
            print('You win this round, uppercut smashes block')
            player_wins += 1
        elif playerChoice == 'jab' and computerChoice == 'uppercut':
            print("You win this round, jabing past the enemy's uppercut")
            player_wins += 1
        elif playerChoice == 'jab' and computerChoice == 'block':
            print('The enemy wins this round, blocking the jab')
            computer_wins += 1
        elif playerChoice == 'block' and computerChoice == 'uppercut':
            print('The enemy wins this round, uppercut smashes block')
            computer_wins += 1
        elif playerChoice == 'block' and computerChoice == 'jab':
            print("You win this round, blocking the enemy's jab")
            player_wins += 1

        if player_wins == necessary_wins or computer_wins == necessary_wins:
            break

    if player_wins > computer_wins:
        print(f'>>> You win the fight! <<<')
    else:
        print(f'>>> The enemy wins the fight! <<<')

    print(f'>>> You scored: {player_wins} win(s) out of three!! <<<')


def MonsterRPS():

    options = ['swing', 'bash', 'stab']

    turns = 5
    print("\nBest two out of three wins the fight!")

    necessary_wins = int(turns/2) + 1

    player_wins = 0
    computer_wins = 0

    while True:

        while True:
            playerChoice = input(">>> swing, bash, stab: ")
            if playerChoice in options:
                break
            else:
                print("Come on, fight!")
                continue


        computerChoice = random.choice(options)

        if playerChoice == computerChoice:
            print('It is a tie')
        elif playerChoice == 'swing' and computerChoice == 'bash':
            print('The enemy wins this round, bash covers swing')
            computer_wins += 1
        elif playerChoice == 'swing' and computerChoice == 'stab':
            print('You win this round, swing smashes stab')
            player_wins += 1
        elif playerChoice == 'bash' and computerChoice == 'swing':
            print('You win this round, bash covers swing')
            player_wins += 1
        elif playerChoice == 'bash' and computerChoice == 'stab':
            print('The enemy wins this round, stab cut bash')
            computer_wins += 1
        elif playerChoice == 'stab' and computerChoice == 'swing':
            print('The enemy wins this round, swing smashes stab')
            computer_wins += 1
        elif playerChoice == 'stab' and computerChoice == 'bash':
            print('You win this round, stab cut bash')
            player_wins += 1

        if player_wins == necessary_wins or computer_wins == necessary_wins:
            break
    
    if player_wins > computer_wins:
        print(f'>>> You scored: {player_wins} win(s) out of three!! ')
        print(f'>>> You win the fight and defeated the monster!  ')
        print("Now you can return home a hero.. for hire!")

    else:
        print(f'The monster wins and has killed you.. another adventurer dies at the hand of a beast..')
        