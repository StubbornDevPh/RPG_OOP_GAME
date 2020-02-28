from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Novice import Novice
from Boss import Monster
from random import randint

p1name = input("(P1) What is your name?\n>")
p2name = input("(P2) What is your name?\n>")

p1class = int(input("(P1) Please choose a class: (1.Archer 2.Swordsman 3.Magician)\n>"))
p2class = int(input("(P2) Please choose a class: (1.Archer 2.Swordsman 3.Magician)\n>"))

p1 = Novice(p1name)
p2 = Novice(p2name)

if p1class == 1:
    p1 = Archer(p1name)
elif p1class == 2:
    p1 = Swordsman(p1name)
elif p1class == 3:
    p1 = Magician(p1name)

if p2class == 1:
    p2 = Archer(p2name)
elif p2class == 2:
    p2 = Swordsman(p2name)
elif p2class == 3:
    p2 = Magician(p2name)



char1 = p1.__class__.__name__
char2 = p2.__class__.__name__
print(f'(P1) selected {char1}')
print(f'(P2) selected {char2}')

p1wins = 0
p2wins = 0
p1inithp = p1.getHp()
p2inithp = p2.getHp()
i=1
while i < 4:
    p1.setHp(p1inithp)
    p2.setHp(p2inithp)
    while p1.getHp()>0 and p2.getHp()>0:
        atk_p1 = 1
        atk_p2 = 1
        print(f"ROUND: {i}")
        blockrandomizer1 = randint(0, 100)
        blockrandomizer2 = randint(0, 100)
        p1choice = int(input("Please enter an attack (1.Attack/2.Block)"))
        p2choice = int(input("Please enter an attack (1.Attack/2.Block)"))

        if(p1choice==1):
            print(f'P1 {p1.getUsername()} TURN')
            if(atk_p2==1):
                if char1 == "Archer":
                    rskillarch = randint(0,1)
                    if rskillarch == 0:
                        p1.passive()
                        p1.rangedAttack(p2)
                    elif rskillarch == 1:
                        p1.passive()
                        p1.basicAttack(p2)
                elif char1 == "Swordsman":
                    rskillsword = randint(0, 1)
                    if rskillsword == 0:
                        p1.passive()
                        p1.slashAttack(p2)
                    elif rskillsword == 1:
                        p1.passive()
                        p1.basicAttack(p2)
                elif char1 == "Magician":
                    rskillmagic = randint(0, 1)
                    if rskillmagic == 0:
                        p1.passive(p2)
                        p1.magicAttack(p2)
                    elif rskillmagic == 1:
                        p1.passive(p2)
                        p1.basicAttack(p2)
                print(f'END OF P1 {p1.getUsername()} TURN')
                print(f'{p2.getUsername()} has {p2.getHp()} remaining health')
            elif(atk_p2==0):
                print(f'{p2.getUsername()} HAS BLOCKED YOUR ATTACK!')

        elif(p1choice==2):
            if blockrandomizer1 <= 20:
                #print(f'{p1.getUsername()} BLOCK SUCCESS')
                atk_p1 = 0
            else:
                #print(f'{p1.getUsername()} BLOCK FAILED')
                atk_p1 = 1

        if (p2choice == 1):
            print(f'P2 {p2.getUsername()} TURN')
            if atk_p1 == 1:
                if char2 == "Archer":
                    rskillarch1 = randint(0, 1)
                    if rskillarch1 == 0:
                        p2.passive()
                        p2.rangedAttack(p1)
                    elif rskillarch1 == 1:
                        p2.passive()
                        p2.basicAttack(p1)
                elif char2 == "Swordsman":
                    rskillsword1 = randint(0, 1)
                    if rskillsword1 == 0:
                        p2.passive()
                        p2.slashAttack(p1)
                    elif rskillsword1 == 1:
                        p2.passive()
                        p2.basicAttack(p1)
                elif char2 == "Magician":
                    rskillmagic1 = randint(0, 1)
                    if rskillmagic1 == 0:
                        p2.passive(p1)
                        p2.magicAttack(p1)
                    elif rskillmagic1 == 1:
                        p2.passive(p1)
                        p2.basicAttack(p1)
                print(f"END OF {p2.getUsername()} TURN")
                print(f'{p1.getUsername()} has {p1.getHp()} remaining health')
            elif atk_p1 == 0:
                print(f"{p1.getUsername()} HAS BLOCKED YOUR ATTACK!")
        elif (p2choice == 2):
            if blockrandomizer2 <= 20:
                #print("P2 Block Success")
                atk_p2 = 0
            else:
                #print("P2 Block Failed")
                atk_p2 = 1
        if(p1.getHp()<=0):
            print(f'{p2.getUsername()} wins!')
            p2wins = p2wins+1
        if (p2.getHp() <= 0):
            print(f'{p1.getUsername()} wins!')
            p1wins = p1wins + 1

    i = i+1

print("\nRESULTS:")
print(f'{p1.getUsername()} has won {p1wins} times')
print(f'{p2.getUsername()} has won {p2wins} times')


