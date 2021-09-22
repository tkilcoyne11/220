"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a Rectangle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    # create graphical window
    win = GraphWin("Rectangle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.draw(win)
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    area = (length * width)
    perimeter = 2 * (length + width)

    area_text_pt = Point(400 / 2, 400 - 15)
    perimeter_text_pt = Point(400 / 2, 400 - 30)
    area_text = Text(area_text_pt, "The area of the rectangle is: "+str(area))
    area_text.draw(win)
    perimeter_text = Text(perimeter_text_pt, "The perimeter of the rectangle is: "+str(perimeter))
    perimeter_text.draw(win)

    win.getMouse()
    win.close()

def circle():

    # Create graphical window
    win = GraphWin("Circle", 400, 400)

    # Build circle
    p1 = win.getMouse()
    p2 = win.getMouse()

    # find radius from p1
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    r = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    c = Circle(p1, r)
    c.draw(win)

    inst_pt = Point(400 / 2, 400 - 10)
    instructions = Text(inst_pt, "Click anywhere to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()

def pi2():
    n = eval(input("Enter n: "))
    acc = 0
    for i in range(n):
        num = 4
        den = 1 + 2 * i
        frac = (num/den) * ((-1) ** i)
        acc += frac
    print(acc)
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()



