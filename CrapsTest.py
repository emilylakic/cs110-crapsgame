import Die
import CrapsGame

def __init__(self):
	self.die1 = Die(6)
	self.die2 = Die(6)

def playGame(self):
	total = self.die1.roll() + self.die2.roll()

def main():
	game = CrapsGame.CrapsGame()
	print("Roll 7")
	print(game.processRoll(7))
	print(game.getPoint())
	print("Roll 2")
	print(game.processRoll(2))
	print(game.getPoint())
	print("Roll 9")
	print(game.processRoll(9))
	print(game.getPoint())
main()
