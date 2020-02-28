from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Novice import Novice


class Boss(Swordsman, Archer, Magician):
    def __init__(self,username):
        super().__init__(username)
        self.setStr(10)
        self.setVit(25)
        self.setHp(5)
        self.setHp(self.getHp()+self.getVit())

class Monster(Swordsman, Archer, Magician):
    def __init__(self,username):
        super().__init__(username)
        self.setStr(10)
        self.setVit(20)
        self.setHp(5)
        self.setHp(self.getHp() + self.getVit())