import random
class Die:
    def roll(self):
        self.rollNum = random.randint(1,self.sides)
        return self.rollNum
