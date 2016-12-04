from Tkinter import Tk, Frame, BOTH
import DisplayPanel
import ControlPanel
import CrapsTable

class Craps(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="green")

        self.parent = parent
        self.parent.title("Craps Game")
        self.pack(fill=BOTH, expand=True)

        DisplayPanel = Frame(self, width=500, height=100, borderwidth=1, background="red")
        frame1.pack(side='top', fill=BOTH, expand=True)

        CrapsTable = Frame(self, width=500, height=350, borderwidth=1, background="blue")
        frame2.pack(side='top', fill=BOTH, expand=True)

        ControlPanel = Frame(self, width=500, height=100, borderwidth=1, background="yellow")
        frame3.pack(side='bottom', fill=BOTH, expand=True)

        self.centerWindow()

    def centerWindow(self):
        w = 750
        h = 550

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():

    root = Tk()
    root.resizable(width=False, height=False)
    ex = Craps(root)
    root.mainloop()

main()
