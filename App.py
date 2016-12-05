from tkinter import *
import time
class App:
    def __init__(self):
        self.root = Tk()
        self.label = Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
