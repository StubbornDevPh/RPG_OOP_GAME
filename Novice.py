from Character import Character
from random import randint

class Novice(Character):

    def basicAttack(self, character):
        chance = randint(1,100)
        if chance<=15:
            if self.__class__.__name__ == "Archer" and character.__class__.__name__ == "Swordsman":
                character.reduceHp(self.getDamage()*3+((self.getDamage()*3)*.10))
                print(f'{self.getUsername()} performed Critical Boosted Basic Attack! -{(self.getDamage()*3+((self.getDamage()*3)*.10))}')

            elif self.__class__.__name__ == "Magician" and character.__class__.__name__ == "Archer":
                character.reduceHp(self.getDamage()*3+((self.getDamage()*3)*.10))
                print(f'{self.getUsername()} performed Critical Boosted Basic Attack! -{(self.getDamage()*3+((self.getDamage()*3)*.10))}')

            elif self.__class__.__name__ == "Swordsman" and character.__class__.__name__ == "Magician":
                character.reduceHp(self.getDamage()*3+((self.getDamage()*3)*.10))
                print(f'{self.getUsername()} performed Critical Boosted Basic Attack! -{(self.getDamage()*3+((self.getDamage()*3)*.10))}')

            elif self.__class__.__name__ == "Novice":
                character.reduceHp(self.getDamage()*3)
                print(f'{self.getUsername()} performed Critical Basic Attack! -{(self.getDamage()*3)}')

            else:
                character.reduceHp(self.getDamage() * 3)
                print(f'{self.getUsername()} performed Critical Basic Attack! -{(self.getDamage() * 3)}')

        else:

            if self.__class__.__name__ == "Archer" and character.__class__.__name__ == "Swordsman":
                character.reduceHp(self.getDamage() + ((self.getDamage()) * .10))
                print(f'{self.getUsername()} performed Boosted Basic Attack! -{(self.getDamage() + self.getDamage()* .10)}')

            elif self.__class__.__name__ == "Magician" and character.__class__.__name__ == "Archer":
                character.reduceHp(self.getDamage() + ((self.getDamage()) * .10))
                print(f'{self.getUsername()} performed Boosted Basic Attack! -{(self.getDamage() + self.getDamage()* .10)}')

            elif self.__class__.__name__ == "Swordsman" and character.__class__.__name__ == "Magician":
                character.reduceHp(self.getDamage()+ ((self.getDamage()) * .10))
                print(f'{self.getUsername()} performed Boosted Basic Attack! -{(self.getDamage() + self.getDamage()* .10)}')

            elif self.__class__.__name__ == "Novice":
                character.reduceHp(self.getDamage())
                print(f'{self.getUsername()} performed Basic Attack! -{self.getDamage()}')

            else:
                character.reduceHp(self.getDamage())
                print(f'{self.getUsername()} performed Basic Attack! -{self.getDamage()}')