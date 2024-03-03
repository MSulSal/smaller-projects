import turtle
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
        self.R = R
        self.r = r
        self.l = l
        self.col = col
        
        gcd_val = gcd(self.r, self.R)
        self.nRot = self.r // gcd_val
        self.k = r / float(R)
        
        self.t.color(*col)
        self.a = 0
        