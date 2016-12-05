import Die

class RollingDie:
    slowdown = 0.97
    speedFactor = 0.04
    speedLimit = 2.0
    dieSize = 24

    #Sets the table boundaries
    def setBounds(left, right, top, bottom):
        tableLeft = left
        tableRight = right
        tableTop = top
        tableBottom = bottom

    #Sets this die off the table
    def __init__(self):
        xCenter = -1
        yCenter = -1

    #Starts this die rolling
    def roll():
        super().roll()
        width = tableRight - tableLeft
        height = tableBottom - tableTop
        xCenter = tableLeft / 2
        yCenter = tableTop + height / 2
        xSpeed = width * (Random.randrange(0.0,1.0)+1) * speedFactor
        ySpeed = height * (Random.randrange(0.0,1.0)-.5) * 2.0 * speedFactor

    #Returns true if this die is rolling, otherwise returns false
    def isRolling():
        return xSpeed > speedLimit or xSpeed < -speedLimit or ySpeed > speedLimit or ySpeed < -speedLimit

    #Keeps moving this die as long as it overlaps with other
    def avoidCollision(other):
        if(other == self):
            return
        while(abs(xCenter - other.xCenter) < dieSize and abs(yCenter - other.yCenter) < dieSize):
            move()

    #Moves this dice on the table and bounces off the edges when necessary
    def move():
        xCenter = xSpeed
        yCenter = ySpeed
        radius = dieSize / 2
        if(xCenter < tableLeft + radius):
            xCenter = tableLeft + radius
            xSpeed = -xSpeed
        if(xCenter > tableRight - radius):
            xCenter = tableRight - radius
            xSpeed = -xSpeed
        if(yCenter < tableTop + radius):
            yCenter = tableTop + radius
            ySpeed = -ySpeed

    #Draws this die, rolling or stopped; also moves this die, when rolling
    def draw(self):
        if(xCenter < 0 or yCenter < 0):
            return
        elif(isRolling()):
            move()
            drawRolling(self)
            xSpeed *= slowdown
            ySpeed *= slowdown
        else:
            drawStopped(self)

    def drawDie(self, x1, y1, x2, y2, r):
        self.create_arc(x1, y1, x1+r, y1+r, start=90, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_arc(x2-r, y1, x2, y1+r, start=0, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_arc(x1, y2-r, x1+r, y2, start=180, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_arc(x2-r, y2-r, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill = "red")
        self.create_rectangle(x1+r/2, y1-r/2, x2-r/2, y2+r/2, fill = "red")
        self.create_rectangle(x1, y1, x2, y2, fill="red")

    #Draws this die when rolling with a random number of dots
    def drawRolling():
        x = xCenter - dieSize/2 + int(Random.randrange(0,3))
        y = yCenter - dieSize/2 + int(Random.randrange(0,3))
        if(x%2 != 0):
            drawDie(self,x,y,x+dieSize,y+dieSize, dieSize)
        else:
            oval = canvas.create_oval(x-2,y-2,x+dieSize+4,y+dieSize+4)
        die = Die.Die();
        die.roll()
        drawDots(self, x, y, Die.getNumDots())

    #Draws this die when stopped
    def drawStopped():
        x = xCenter - dieSize/2
        y = yCenter - dieSize/2
        drawDie(self, x, y, x+dieSize, y+dieSize)
        drawDots(self, x, y, getNumDots())

    #Draws a given number of dots on this die
    def drawDots(self, x, y, numDots):
        self.setFill("White")
        dotSize = dieSize/4
        step = dieSize/8
        x1 = x + step - 1
        x2 = x + 3*step
        x3 = x + 5*step + 1
        y1 = y + step - 1
        y2 = y + 3*step
        y3 = y + 5*step + 1

        #Insert a replacement for a switch
        v = numDots
        for case in switch(v):
            if case(1):
                #Make 1 Dot
                oval1 = canvas.create_oval(x2, y2, x2+dotSize, y2+dotSize)
                break
            if case(2):
                #Make 2 Dots
                oval1 = canvas.create_oval(x1, y1, x1+dotSize, y1+dotSize)
                oval2 = canvas.create_oval(x3, y3, x3+dotSize, y3+dotSize)
                break
            if case(3):
                #Make 3 Dots
                oval1 = canvas.create_oval(x1, y3, x1+dotSize, y3+dotSize)
                oval2 = canvas.create_oval(x2, y2, x2+dotSize, y2+dotSize)
                oval3 = canvas.create_oval(x3, y1, x3+dotSize, y1+dotSize)
                break
            if case(4):
                #Make 4 Dots
                oval1 = canvas.create_oval(x1, y1, x1+dotSize, y1+dotSize)
                oval2 = canvas.create_oval(x3, y1, x3+dotSize, y1+dotSize)
                oval3 = canvas.create_oval(x1, y3, x1+dotSize, y3+dotSize)
                oval4 = canvas.create_oval(x3, y3, x3+dotSize, y3+dotSize)
                break
            if case(5):
                #Make 5 Dots
                oval1 = canvas.create_oval(x1, y1, x1+dotSize, y1+dotSize)
                oval2 = canvas.create_oval(x3, y1, x3+dotSize, y1+dotSize)
                oval3 = canvas.create_oval(x2, y2, x2+dotSize, y2+dotSize)
                oval4 = canvas.create_oval(x1, y3, x1+dotSize, y3+dotSize)
                oval5 = canvas.create_oval(x3, y3, x3+dotSize, y3+dotSize)
                break
            if case(6):
                #Make 6 Dots
                oval1 = canvas.create_oval(x1, y1, x1+dotSize, y1+dotSize)
                oval2 = canvas.create_oval(x3, y1, x3+dotSize, y1+dotSize)
                oval3 = canvas.create_oval(x1, y2, x1+dotSize, y2+dotSize)
                oval4 = canvas.create_oval(x3, y2, x3+dotSize, y2+dotSize)
                oval5 = canvas.create_oval(x1, y3, x1+dotSize, y3+dotSize)
                oval6 = canvas.create_oval(x3, y3, x3+dotSize, y3+dotSize)
                break
