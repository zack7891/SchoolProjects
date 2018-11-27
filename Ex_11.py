#Gives access to graphics.py
from graphics import *

def main():
    win = GraphWin("house.py", 500, 500)
    win.setCoords(0,0, 4,4)

    p1 = win.getMouse()

    x = p1.getX()
    y = p1.getY()
    p6=Point(x+0.05,y+0.05)
    Pt = Oval(p1,p6)
    Pt.setFill(color_rgb(255,255,0))
    Pt.setOutline(color_rgb(255,255,0))
    Pt.draw(win)

    p2 = win.getMouse()

    x=p2.getX()
    y=p2.getY()
    p6=Point(x+0.05,y+0.05)
    Pt = Oval(p2,p6)
    Pt.setFill(color_rgb(255,255,0))
    Pt.setOutline(color_rgb(255,255,0))
    Pt.draw(win)

    p3 = win.getMouse()

    x=p3.getX()
    y=p3.getY()
    p6=Point(x+0.05,y+0.05)
    Pt = Oval(p3,p6)
    Pt.setFill(color_rgb(255,255,0))
    Pt.setOutline(color_rgb(255,255,0))
    Pt.draw(win)


    p4 = win.getMouse()

    x=p4.getX()
    y=p4.getY()
    p6=Point(x+0.05,y+0.05)
    Pt = Oval(p4,p6)
    Pt.setFill(color_rgb(255,255,0))
    Pt.setOutline(color_rgb(255,255,0))
    Pt.draw(win)


    p5 = win.getMouse()

    x=p5.getX()
    y=p5.getY()
    p6=Point(x+0.05,y+0.05)
    Pt = Oval(p5,p6)
    Pt.setFill(color_rgb(255,255,0))
    Pt.setOutline(color_rgb(255,255,0))
    Pt.draw(win)


    p7=Point(p2.getX(),p1.getY())

    house = Rectangle(p1, p2)
    house.setFill("Red")
    house.draw(win)

    roof = Polygon(p1, p7, p3)
    roof.setFill("Black")
    roof.draw(win)

    p8=Point(p4.getX()+0.5,p2.getY())

    door = Rectangle(p4,p8)
    door.setFill("Brown")
    door.draw(win)

    p9=Point(p5.getX()+0.25,p5.getY()-0.25)
    window = Rectangle(p5,p9)
    window.setFill("White")
    window.draw(win)

    win.getMouse()
    win.close()
main()
