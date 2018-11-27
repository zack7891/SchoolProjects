#This program is for the user to determine whether
#or not a horizontal line falls on the given circle
from graphics import *
import math
#Sets up the graphic window 
win = GraphWin("Draw a Line", 500,500)
win.setCoords(-10.0,-10.0,10.0,10.0)
win.setBackground('white')

#sets all text to black
def message(msg):
    message = Text(Point(0, -9), msg)
    message.setFill('black')
    message.draw(win)
#main function 
def main():
    #basic instructions for user
    instructions = Text(Point(0, 9), 'Click on two points to draw a horizontal line.')
    instructions.setFill('red')
    instructions.draw(win)

    #Set the radius to 5 since trying to get an input kept giving me an error
    circle = Circle(Point(0,0), 5) 
    circle.setOutline('black')
    circle.setWidth('2')
    circle.setFill('white')
    circle.draw(win)
 
    #draws the first point
    p = win.getMouse()
    x1 = p.getX()
    y = p.getY()
    c = Circle(Point(x1,y),0.1)
    c.setFill('black')
    c.draw(win)
    txt = Text(Point(x1+1,y+.5),'')
    txt.setText('%0.2f, %0.2f' %(x1,y))
    txt.draw(win)
 
    #draws the second point
    p2 = win.getMouse()
    x2 = p2.getX()
    c = Circle(Point(x2,y),0.1)
    c.setFill('black')
    c.draw(win)
    txt = Text(Point(x2+1,y+.5),'')
    txt.setText('%0.2f, %0.2f' %(x2,y))
    txt.draw(win)
 
    line = Line(Point(x1,y), Point(x2,y))
    line.setOutline('black')
    line.setWidth('3')
    line.draw(win)
 
    #if/else statement to determine whether or not the line falls on the cirlce 
    if  y >5 or y< -5 :
        Txt = 'Line does not intersect Circle.'
        message(Txt)
 
    else:
        Txt =  'Line intersects Circle.'
        message(Txt)
 
        #draw intersect points
        x  = math.sqrt(25 - y**2)
        for i in range(2):
            pt = Circle(Point(x, y),0.15)
            pt.setFill('red')
            pt.draw(win)
            x = -x
    #closes window with mouse click do not use 'X' to close window error will be given 
    win.getMouse()
    win.close()
#executes all of the code found in it 
if __name__ == '__main__':
    main()
