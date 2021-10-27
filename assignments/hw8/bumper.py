"""
Name: Tucker Kilcoyne
bumper.py
Certification of Authenticity
I certify that this assignment is entirely my own work
"""

from random import randint
from graphics import GraphWin, Circle, Point


def create_window():
    w = 500
    h = 500
    win = GraphWin("Bumpers", w, h)
    win.setBackground("light blue")
    return win


def bumpers():

    win = create_window()

    # Set up the window

    pt1 = Point(500/2, 500/2 + 50)
    pt2 = Point(500/2, 500/2 - 50)

    circle1 = Circle(pt1, 25)
    circle1.setFill("dark red")
    circle1.setOutline("red")
    circle2 = Circle(pt2, 25)
    circle2.setOutline("green")
    circle2.setFill("dark green")

    circle1.draw(win)
    circle2.draw(win)

    # create movement

    win.getMouse()
    win.close()


def main():
    bumpers()


if __name__ == '__main__':
    main()