from tkinter import *
from RollingDie import *
from CrapsGame import *

class CrapsTable(Frame):
    def __init__(self, parent, display,canvas):
        self.die1 = RollingDie(canvas)
        self.die2 = RollingDie(canvas)
        self.delay = 20
        self.display = display
        self.game = CrapsGame()
        self.die1.draw();
        self.die2.draw();

    def CrapsTable(display):
        root = Tk()
        root.configure(background="Dark Green")
        widget.config(highlightbackground="Orange")

    def rollDie(self):
        self.die1.setBounds(25, 375, 25, 350)
        self.die2.setBounds(25, 675, 25, 350)
        self.die1.roll()
        self.die2.roll()
        self.die1.draw()
        self.die2.draw()
        self.actionPerformed()

    def actionPerformed(self):
        self.die1.avoidCollision(self.die2)
        self.die2.avoidCollision(self.die1)
        total = self.die1.getNumDots() + self.die2.getNumDots()
        result = self.game.processRoll(total)
        point = self.game.getPoint()
        self.display.update(result, point)
        self.paintComponent()

    def isDiceRolling(self):
        return self.die1.isRolling() or self.die2.isRolling()

    def paintComponent(self):
        self.die1.clearCanvas()
        self.die1.draw();
        self.die2.draw();
