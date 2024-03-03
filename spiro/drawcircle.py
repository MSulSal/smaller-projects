import math
import turtle

def dx(r, theta):
    return r * math.cos(theta)

def dy(r, theta):
    return r * math.sin(theta)

def rotate(x0, y0, r, angle):
    theta = math.radians(angle)
    turtle.setpos(x0 + dx(r, theta), y0 + dy(r, theta))

# draw the circle using turtle
def drawCircleTurtle(x0, y0, r, delta):
    # move to the start of circle
    turtle.up()
    turtle.setpos(x0 + r, y0)
    turtle.down()
    
    
    # draw the circle
    for i in range(0, 361, delta):
        rotate(x0, y0, r, i)
        
drawCircleTurtle(0, 0, 50, 90)
turtle.mainloop()