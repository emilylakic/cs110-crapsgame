# Represents the craps table with two rolling dice
from tkinter import *
from RollingDie import *
from CrapsGame import *
from App import*

class CrapsTable(Frame):
    def __init__(self, parent, display):
        self.die1 = RollingDie()
        self.die2=RollingDie()
        self.delay = 20
        self.display = display
        #self.clock = App()
        self.game = CrapsGame()

    def CrapsTable(display):
        root = Tk()
        root.configure(background='green')
        widget.config(highlightbackground='Orange')
        
    # Rolls the dice (called when the "Roll" button is clicked)
    def rollDie(self):
        self.die1.setBounds(-3, 3, 3, -3)
        self.die2.setBounds(-3, 3, 3, -3)
        self.die1.roll()
        self.die2.roll()
        #self.clock.start()
        
    # Processes timer events
    def actionPerformed():
        if(isDiceRolling()):
            #if(not self.clock.isRunning()):
             #   self.clock.restart()
            if(self.die1.isRolling()):
                self.die1.avoidCollision(self.die2)
            elif(self.die2.isRolling()):
                self.die2.avoidCollision(self.die1)
            else:
              #  self.clock.stop()
                total = self.die1.getNumDots() + self.die2.getNumDots()
                result = self.game.processRoll(total)
                point = self.game.getPoint()
                self.display.update(result, point)
        repaint()
    # returns true if dice are still rolling; otherwise
    # returns false
    def isDiceRolling(self):
        return self.die1.isRolling() or self.die2.isRolling()

    def paintComponent():
        die1.draw(g);
        die2.draw(g);
