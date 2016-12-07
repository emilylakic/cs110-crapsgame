from tkinter import *
from RollingDie import *
from CrapsGame import *
import pyaudio
import wave

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
        CrapsTable.playSound()
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

    def playSound():
        chunk = 1024
        f = wave.open("roll.wav", "rb")
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),rate = f.getframerate(),output = True)
        data = f.readframes(chunk)
        while len(data)>0:
            stream.write(data)
            data = f.readframes(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()
