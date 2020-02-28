from Novice import Novice
import random
from random import randint

class Archer(Novice):

    def __init__(self, username):
        super().__init__(username)
        self.setStr(5)
        self.setInt(5)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())

    def rangedAttack(self, character):
        chance = randint(1,100)
        if chance<=10:
            print('Miss')#10% miss chance
        elif chance>=95: #5% chance
            self.new_damage = self.getDamage()+random.randint(0,self.getInt())+(self.getDamage() + random.randint(0, self.getInt()) * .5)
            character.reduceHp(self.new_damage)
            print(f'{self.getUsername()} performed Super Effective Move (Ranged Attack)! -{self.new_damage}')
        else:
            self.new_damage = self.getDamage()+random.randint(0,self.getInt())
            character.reduceHp(self.new_damage)
            print(f'{self.getUsername()} performed Ranged Attack! -{self.new_damage}')

    def passive(self):
        self.setInt(self.getInt()+2)
        print(f'{self.getUsername()} has increased Int to {self.getInt()}')
