from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Novice import Novice
from Boss import Monster
from random import randint

wins = 0
loss = 0
player1_class = "0"
nameko = input("Please enter player name:")
rank=0

while 1:
    char = Novice(nameko)
    print(f'WELCOME TO THE GAME 2020 (WINS:{wins}/LOSS:{loss})')
    print("Choose a mode:")
    choice = int(input("1.Single Player\n2.Multiplayer\nChoice:"))
    if choice==1:
        print("You have chosen SINGLE PLAYER")
        char = Novice(nameko)
        bot = Monster("Monster")
        print(f'Your name is: {char.getUsername()}')
        print(f'Monster name is:{bot.getUsername()}')
        rank_type = str(char.__class__.__name__)
        while (char.getHp() > 0 and bot.getHp() > 0):
            turna = randint(0, 2)
            turnb = randint(0, 4)
            if (char.getHp() > 0 and bot.getHp() > 0):
                if (wins > 1):
                    rank = (input("Choose a rank\n[1]Swordsman\n[2]Magician\n[3]Archer\n"))
                if rank == "1":
                    char = Swordsman(nameko)
                elif rank == "2":
                    char = Magician(nameko)
                elif rank == "3":
                    char = Archer(nameko)
                elif rank == "4":
                    char = Novice(nameko)
                else:
                    char = Novice(nameko)
                while (char.getHp() > 0 and bot.getHp() > 0):
                    turna = randint(0, 4)
                    turnb = randint(0, 4)
                    if (char.getHp() > 0 and bot.getHp() > 0):
                        while (turna > 0):
                            if (turna != 0):
                                try:
                                    if (turna == 1):
                                        char.slashAttack(bot)
                                        print(f'{bot.getUsername()} has only {bot.getHp()} remaining\n')
                                    elif (turna == 2):
                                        char.magicAttack(bot)
                                        print(f'{bot.getUsername()} has only {bot.getHp()} remaining\n')
                                    elif (turna == 3):
                                        char.rangedAttack(bot)
                                        print(f'{bot.getUsername()} has only {bot.getHp()} remaining\n')
                                    elif (turna == 4):
                                        char.heal()
                                except:
                                    char.basicAttack(bot)
                                    print(f'{bot.getUsername()} has only {bot.getHp()} remaining\n')
                            turna = turna - 1



                if (turnb > 0):
                    if (turnb != 0):
                        try:
                            if (turnb == 1):
                                bot.slashAttack(char)
                                print(f'{char.getUsername()} has only {char.getHp()} remaining\n')
                            elif (turnb == 2):
                                bot.magicAttack(char)
                                print(f'{char.getUsername()} has only {char.getHp()} remaining\n')
                            elif (turnb == 3):
                                bot.rangedAttack(char)
                                print(f'{char.getUsername()} has only {char.getHp()} remaining\n')
                            elif (turnb == 4):
                                bot.heal()
                        except:
                            bot.basicAttack(char)
                            print(f'{char.getUsername()} has only {char.getHp()} remaining\n')
                    turnb = turnb - 1

        if(char.getHp()<=0):
            print(f'{bot.getUsername()} has won')
            loss = loss+1
        else:
            print(f'{char.getUsername()} has won')
            wins = wins+1

    elif choice == 2:
        print("You chose MULTIPLAYER")
        char1_name = input("Please enter player 1 name:")
        char2_name = input("Please enter player 2 name:")
        player1_class = input(f'Please enter {char1_name} class:\n[1].Novice\n[2].Swordsman\n[3].Archer\n[4].Magician\nChoice:')
        player2_class = input(f'Please enter {char2_name} class:\n[1].Novice\n[2].Swordsman\n[3].Archer\n[4].Magician\nChoice:')
        if player1_class=="1":
            Player1 = Novice(char1_name)
        elif player1_class=="2":
            Player1 = Swordsman(char1_name)
        elif player1_class=="3":
            Player1 = Archer(char1_name)
        elif player1_class=="4":
            Player1 = Magician(char1_name)
        else:
            print("Invalid choice")
            break

        if player2_class=="1":
            Player2 = Novice(char2_name)
        elif player2_class=="2":
            Player2 = Swordsman(char2_name)
        elif player2_class=="3":
            Player2 = Archer(char2_name)
        elif player2_class=="4":
            Player2 = Magician(char2_name)
        else:
            print("Invalid choice")
            break

        while(Player1.getHp()>0 and Player2.getHp()>0):
            turna = randint(0, 4)
            turnb = randint(0, 4)
            if (Player1.getHp()>0 and Player2.getHp()>0):
                while(turna>0):
                    if(turna!=0):
                        try:
                            if(turna==1):
                                Player1.slashAttack(Player2)
                                print(f'{Player2.getUsername()} has only {Player2.getHp()} remaining\n')
                            elif(turna==2):
                                Player1.magicAttack(Player2)
                                print(f'{Player2.getUsername()} has only {Player2.getHp()} remaining\n')
                            elif(turna==3):
                                Player1.rangedAttack(Player2)
                                print(f'{Player2.getUsername()} has only {Player2.getHp()} remaining\n')
                            elif(turna==4):
                                Player1.heal()
                        except:
                            Player1.basicAttack(Player2)
                            print(f'{Player2.getUsername()} has only {Player2.getHp()} remaining\n')
                    turna=turna-1

                while(turnb>0):
                    if (turnb != 0):
                        try:
                            if (turnb == 1):
                                Player2.slashAttack(Player1)
                                print(f'{Player1.getUsername()} has only {Player1.getHp()} remaining\n')
                            elif (turnb == 2):
                                Player2.magicAttack(Player1)
                                print(f'{Player1.getUsername()} has only {Player1.getHp()} remaining\n')
                            elif (turnb == 3):
                                Player2.rangedAttack(Player1)
                                print(f'{Player1.getUsername()} has only {Player1.getHp()} remaining\n')
                            elif (turnb == 4):
                                Player2.heal()
                        except:
                            Player2.basicAttack(Player1)
                            print(f'{Player1.getUsername()} has only {Player1.getHp()} remaining\n')
                    turnb=turnb-1

            if(Player1.getHp()<=0):
                print(f'{Player2.getUsername()} has won')
                break
            if(Player2.getHp()<=0):
                print(f'{Player1.getUsername()} has won')
                break
