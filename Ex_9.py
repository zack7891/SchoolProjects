#Gives access to graphics.py
from graphics import *

def main():
    #creates a window
    win = GraphWin("Draw a Rectangle", 500, 500)
    text = Text(Point(250, 25), "Make a Rectangle with two points")
    text.draw(win)

    #Tells user how to close program
    text = Text(Point(250, 450), "Click the 'X' to close or click the screen")
    text.draw(win)
    
    #Creates points from mouse clicks
    p1 = win.getMouse()
    p2 = win.getMouse()

    #creates and draws rectangle from mouse clicks 
    rect = Rectangle(p1,p2)
    rect.setFill('white')
    rect.setOutline('Blue')
    rect.draw(win)

    #Formulas to calculate the area and perimeter
    length = abs(p1.x -p2.x)
    width  = abs(p1.x- p2.x)
    area = length * width
    perimeter = 2 * (length + width)

    #prints both calculations out for the user to see
    print(perimeter)
    print(area)

    #Alternative way to close program
    win.getMouse()
    win.close()
    
main()

