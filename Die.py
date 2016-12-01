import random

class Die:
	def __init__(self, sides):
		self.sides = sides
		self.rollNum = None
	def roll(self):
		self.rollNum = random.randint(1,self.sides)
		return self.rollNum
