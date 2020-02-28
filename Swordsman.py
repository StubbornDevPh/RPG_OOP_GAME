from Novice import Novice
from random import randint

class Swordsman(Novice):

    def __init__(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp()+self.getVit())

    def slashAttack(self, character):
        chance = randint(1,100)
        if chance<=10:
            print('Miss')#10% miss chance
        elif chance>=95: #5% chance
            self.new_damage = self.getDamage()+self.getStr()+((self.getDamage()+self.getStr())*.5)
            character.reduceHp(self.new_damage)
            print(f'{self.getUsername()} performed Super Effective Move (Slash Attack)! -{self.new_damage}')
        else:
            self.new_damage = self.getDamage()+self.getStr()
            character.reduceHp(self.new_damage)
            print(f'{self.getUsername()} performed Slash Attack! -{self.new_damage}')
    
    def passive(self):
        regen = self.getHp()+1
        self.setHp(regen)
        print(f'{self.getUsername()} regenerated hp +1 CurrentHealth={regen}')
