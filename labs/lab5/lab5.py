"""
Name: Tucker Kilcoyne
lab5.py
"""

import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    t = Polygon(p1, p2, p3)
    t.draw(win)

    # and display its area in the graphics window.
    s1 = math.sqrt(abs(p1.getX() - p2.getX()) ** 2 + abs(p1.getY() - p2.getY()) ** 2)
    s2 = math.sqrt(abs(p2.getX() - p3.getX()) ** 2 + abs(p2.getY() - p3.getY()) ** 2)
    s3 = math.sqrt(abs(p3.getX() - p1.getX()) ** 2 + abs(p3.getY() - p1.getY()) ** 2)
    perimeter = s1 + s2 + s3
    s = int(perimeter / 2)
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    print(area)
    print(perimeter)
    area_text_pt = Point(500 / 2, 500 - 25)
    perimeter_text_pt = Point(500 / 2, 500 - 50)
    area_text = Text(area_text_pt, "The area of the Triangle is: "+str(area))
    perimeter_text = Text(perimeter_text_pt, "The perimeter of the Triangle is: "+str(perimeter))
    area_text.draw(win)
    perimeter_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(red_text_pt.getX() + 40, red_text_pt.getY()), 5)
    green_box = Entry(Point(green_text_pt.getX() + 40, green_text_pt.getY()), 5)
    blue_box = Entry(Point(blue_text_pt.getX() + 40, blue_text_pt.getY()), 5)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    s = str(input("Enter a string: "))
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0]+s[-1])
    for i in range(10):
        print(s[:3])
    for j in range(len(s)):
        print(s[j])
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    x = int(input("Enter the number of terms: "))
    acc = 0
    for i in range(x):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc += y
    print("")
    print("sum = " + str(acc))

def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
