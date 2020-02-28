from Novice import Novice
from random import randint

class Magician(Novice):

    def __init__(self, username):
        super().__init__(username)
        self.setInt(10)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())

    def heal(self):
        self.addHp(self.getInt())
        print(f'{self.getUsername()} performed Heal! +{self.getInt()}')

    def magicAttack(self, character):
        chance = randint(1,100)
        if chance<=10:
            print('Miss')#10% miss chance
        elif chance>=95: #5% chance
            self.new_damage = (self.getDamage()+self.getInt()+((self.getDamage()+self.getInt())*.5))
            character.reduceHp(self.new_damage)
            print(f'{self.getUsername()} performed Super Effective Move (Magic Attack)! -{self.new_damage}')
        else:
            self.new_damage = self.getDamage()+self.getInt()
            character.reduceHp(self.new_damage)
            print(f'{self.getUsername()} performed Magic Attack! -{self.new_damage}')
    
    def passive(self, character):
        character.reduceHp(1)
        print(f'Life drain dealt -1 to {character.getUsername()} {character.getHp()}')