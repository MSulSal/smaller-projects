import turtle
import math
from fractions import gcd

class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        
        self.step = 5
        self.drawingComplete = False
        self.setparams(xc, yc, col, R, r, l)
        self.restart()
        
    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        
        gcd_val = gcd(self.r, self.R)
        self.nRot = self.r // gcd_val
        self.k = r / float(R)
        
        self.t.color(*col)
        self.a = 0
        
    def restart(self):
        self.drawingComplete = False
        self.t.showturtle()
        self.t.up()
        
        R, k, l = self.R, self.k, self.l
        a = 0.0
        
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()
        