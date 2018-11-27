#threebuttonmonte.py
from graphics import *
from random import randrange


class Button:
    """A button is a labeled rectangle in a window. It is activate or deactivated with the activated() and deactivated() methods.
    The clicked(p) method returns true if the button is active and p is inside it."""


    def __init__(self, win, center, width, height, label):
        #Creates a rectangle button

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button is active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getlabel(self):
        "Returns the label string onf this button"
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets ths button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

def main():
    #create application graphics window
    win = GraphWin("Three Button Monte")
    win.setCoords(0, 0, 20, 10)
    win.setBackground("green")
    #Draw the interface
    Text(Point(10, 7), "Choose a door").draw(win)
    door1 = Button(win, Point(3, 5), 5, 2, "Door 1")
    door1.activate()
    door2 = Button(win, Point(10, 5), 5, 2, "Door 2")
    door2.activate()
    door3 = Button(win, Point(17, 5), 5, 2, "Door 3")
    door3.activate()
    qbutton = Button(win, Point(10, 1.5), 4, 1, "quit")


    pt = win.getMouse()

    #choose a random door

    door = randrange(1, 4)

    if door == 1 and door1.clicked(pt):
        text1 = Text(Point(10, 3), "You Win!")
        text1.draw(win)
    elif door == 2 and door2.clicked(pt):
        text2 = Text(Point(10, 3), "You Win!")
        text2.draw(win)
    elif door == 3 and door3.clicked(pt):
        text3 = Text(Point(10, 3), "You Win!")
        text3.draw(win)
        
    else:
       text4 = Text(Point(10, 3), "You Lose.")
       text4.draw(win)

    qbutton.activate()    
    win.getMouse()
    win.close()
main()
