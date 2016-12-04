from tkinter import *
from DisplayPanel import *
from CrapsTable import *
from ControlPanel import *

class Craps(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="green")
        self.parent = parent
        self.parent.title("Craps Game")
        self.pack(fill=BOTH, expand=True)

        self.display = DisplayPanel(self.parent)
        self.table = CrapsTable(self.parent, self.display)
        self.control = ControlPanel(self.parent,self.table)
        
        self.centerWindow()

    
    def centerWindow(self):
        w = 750
        h = 550

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Opens score window when game is exited
    def score(self):
        self.display.scoreWindow()
        self.parent.destroy()

def main():

    root = Tk()
    root.resizable(width=False, height=False)
    ex = Craps(root)
    root.protocol("WM_DELETE_WINDOW", ex.score)
    root.mainloop()

main()
