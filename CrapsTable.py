# Represents the craps table with two rolling dice
from tkinter import *
from RollingDie import *
from CrapsGame import *

class CrapsTable(Frame):
    def __init__(self, parent, display, canvas):
        self.die1 = RollingDie(canvas)
        self.die2 = RollingDie(canvas)
        self.delay = 20
        self.display = display
        self.game = CrapsGame()
        self.die1.draw(); 
        self.die2.draw();
        
    def CrapsTable(display): 
        root = Tk()
        root.configure(background = 'Dark Green')
        widget.config(highlightbackground = 'Orange')
        
    # Rolls the dice (called when the "Roll" button is clicked)
    def rollDie(self):
        #print("Rolling Die.....") - used to debug previously
        self.die1.setBounds(25, 675, 25, 445) #changed previous boundaries
        self.die2.setBounds(25, 675, 25, 445)
        self.die1.roll()
        self.die2.roll()
        #insert clear canvas
        self.die1.clearCanvas()
        self.die2.clearCanvas()
        self.die1.draw()
        self.die2.draw()
        self.actionPerformed()
        
    # Processes timer events
    def actionPerformed(self):
        while(self.isDiceRolling()):
            if(self.die1.isRolling()):
                self.die1.avoidCollision(self.die2)
            elif(self.die2.isRolling()):
                self.die2.avoidCollision(self.die1)
        total = self.die1.getNumDots() + self.die2.getNumDots()
        result = self.game.processRoll(total)
        point = self.game.getPoint()
        self.display.update(result, point)
        self.paintComponent()
        
    # returns true if dice are still rolling; otherwise
    # returns false
    def isDiceRolling(self):
        return self.die1.isRolling() or self.die2.isRolling()

    def paintComponent(self):
        self.die1.clearCanvas() #clears the canvas
        #self.die2.clearCanvas() #clears the canvas, not needed
        self.die1.draw(); #previously used g's only for graphics in Java
        self.die2.draw();
