#Implements the game of Craps logic
class CrapsGame:
	def __init__(self):
		self.point = 0
		self.result = None

	def processRoll(self, total):
		self.result = 0
		if(self.point == 0):
			if(total == 7 or total == 11):
				self.result = 1
				self.point = 0
			elif(total == 2 or total == 3 or total == 12):
				self.result = -1
				self.point = 0
			else:
				self.result = 0
				self.point = total
		elif(total == point):
			self.result = 1
			self.point = 0
		elif(total == 7):
			self.result = -1
			self.point = 0
		else:
			self.result = 0
		return self.result

	#Returns the saved point
	def getPoint(self):
		return self.point
