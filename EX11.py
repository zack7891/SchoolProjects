from graphics import *
#Create graphic window
#This program is intended to draw a house with 5 mouse clicks

win = GraphWin("house.py", 500, 500)
win.setCoords(0,0, 4,4)

def main():
    #House-Upper Right Point
    p1 = win.getMouse()

    x = p1.getX()
    y = p1.getY()
    p6 = Point(x + 0.05,
               y + 0.05)
    
    Pt = Oval(p1,
              p6)
    
    Pt.setFill("red")
    Pt.setOutline("black")
    Pt.draw(win)

    #House-Lower Left Point
    p2 = win.getMouse()

    x = p2.getX()
    y = p2.getY()
    p6 = Point(x + 0.05,
               y + 0.05)
    Pt = Oval(p2,
              p6)
    Pt.setFill("red")
    Pt.setOutline("black")
    Pt.draw(win)
    #Roof-Upper Point
    p3 = win.getMouse()

    x = p3.getX()
    y = p3.getY()
    p6 = Point(x + 0.05,
               y + 0.05)
    Pt = Oval(p3,
              p6)
    
    Pt.setFill("brown")
    Pt.setOutline("black")
    Pt.draw(win)

    #Door Point
    p4 = win.getMouse()

    x = p4.getX()
    y = p4.getY()
    p6 = Point(x + 0.05,
               y + 0.05)
    
    Pt = Oval(p4,
              p6)
    
    Pt.setFill("black")
    Pt.setOutline("black")
    Pt.draw(win)

    #Window Point
    p5 = win.getMouse()

    x = p5.getX()
    y = p5.getY()
    
    p6 = Point( x + 0.05,
                y + 0.05)
    Pt = Oval(p5,
              p6)
    
    Pt.setFill("green")
    Pt.setOutline("black")
    Pt.draw(win)

    #Draws House
    p7=Point(p2.getX(),
             p1.getY())

    house = Rectangle(p1,
                      p2)
    
    house.setFill("Red")
    house.draw(win)

    #Draws rood
    roof = Polygon(p1,
                   p7,
                   p3)
    
    roof.setFill("black")
    roof.draw(win)

    #Draws Door
    p8=Point( p4.getX()+ 0.5,
             p2.getY())
    
    door = Rectangle(p4,
                     p8
                     )
    door.setFill("brown")
    door.draw(win)

    #Draws window
    p9 = Point(p5.getX()+ 0.25,
               p5.getY() - 0.25)
    window = Rectangle(p5,
                       p9)
    
    window.setFill("Black")
    window.draw(win)
    #Waits for mouse click
    win.getMouse()
    #Closes window
    win.close()

main()
