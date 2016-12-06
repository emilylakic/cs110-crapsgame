from CrapsGame import *
from Tkinter import *
import random
import time

def main():
	game = CrapsGame()
	main = Tk()
	main.wm_title("   |=-+-==-+-==-+-==-+-==-+-==-+-==-+-= Welcome to Craps! =-+-==-+-==-+-==-+-==-+-==-+-==-+-=|")
	file1 = PhotoImage(file = "Dice 1.gif")
	file2 = PhotoImage(file = "Dice 2.gif")
	file3 = PhotoImage(file = "Dice 3.gif")
	file4 = PhotoImage(file = "Dice 4.gif")
	file5 = PhotoImage(file = "Dice 5.gif")
	file6 = PhotoImage(file = "Dice 6.gif")
	won = [0]
	lost = [0]
	point = [0]

	canvas = Canvas(main, bg="Dark Green", height=750, width=750, highlightbackground='orange', highlightthickness = 10)

	def callback():
		rollNum1 = random.randint(1,6)
		rollNum2 = random.randint(1,6)
		print(rollNum1)
		print(rollNum2)
		if(rollNum1 == 1):
			image1a = canvas.create_image(275,300,image=file1)
		elif(rollNum1 == 2):
			image1a = canvas.create_image(275,300,image=file2)
		elif(rollNum1 == 3):
			image1a = canvas.create_image(275,300,image=file3)
		elif(rollNum1 == 4):
			image1a = canvas.create_image(275,300,image=file4)
		elif(rollNum1 == 5):
			image1a = canvas.create_image(275,300,image=file5)
		elif(rollNum1 == 6):
			image1a = canvas.create_image(275,300,image=file6)

		if(rollNum2 == 1):
			image1b = canvas.create_image(475,300,image=file1)
		elif(rollNum2 == 2):
			image1b = canvas.create_image(475,300,image=file2)
		elif(rollNum2 == 3):
			image1b = canvas.create_image(475,300,image=file3)
		elif(rollNum2 == 4):
			image1b = canvas.create_image(475,300,image=file4)
		elif(rollNum2 == 5):
			image1b = canvas.create_image(475,300,image=file5)
		elif(rollNum2 == 6):
			image1b = canvas.create_image(475,300,image=file6)
		r = game.processRoll(rollNum1+rollNum2)
		if(r == 1):
			won[0] += 1
			wonLabel = Label(main,text="Won:  \n"+str(won[0]),font=labelfont)
			wonLabel.pack(side=LEFT)
		elif(r == 0):
			lost[0] += 1
			lostLabel = Label(main,text="Lost:  \n"+str(lost[0]),font=labelfont)
			lostLabel.pack(side=RIGHT)
		elif(r == -1):
			point[0] = game.getPoint()
			Instruction = Label(main, text=point)

	roll = Button(main, text="Roll", width=15, command=callback)

	labelfont = ('Palatino', 15, 'bold')

	wonLabel = Label(main,text="Won:  \n"+str(won[0]),font=labelfont)
	wonLabel.pack(side=LEFT)

	lostLabel = Label(main,text="Lost:  \n"+str(lost[0]),font=labelfont)
	lostLabel.pack(side=RIGHT)

	pointLabel = Label(main,text="Point:  \n",font=labelfont)
	pointLabel.pack(side=BOTTOM)

	roll.pack()
	canvas.pack()
	main.mainloop()
main()
