"""
Name: Tucker Kilcoyne
bumper.py
Certification of Authenticity
I certify that this assignment is entirely my own work
"""

import math
import time
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb


def get_random(move_amount):
    return randint(-move_amount, +move_amount)


def did_collide(ball1, ball2):
    distance = math.sqrt((ball1.getCenter().getX() - ball2.getCenter().getX()) ** 2
                         + (ball1.getCenter().getY() - ball2.getCenter().getY()) ** 2)
    return bool(distance <= (ball1.getRadius() + ball2.getRadius()))


def hit_vertical(circle, win):
    top = circle.getCenter().getY() + circle.getRadius() >= float(win.getHeight())
    bottom = circle.getCenter().getY() - circle.getRadius() <= 0
    return bool(top or bottom)


def hit_horizontal(circle, win):
    left = circle.getCenter().getX() - circle.getRadius() <= 0
    right = circle.getCenter().getX() + circle.getRadius() >= float(win.getWidth())
    return bool(left or right)


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def bumper():
    width = 500
    height = 500
    win = GraphWin("bumper", width, height)

    circle1 = Circle(Point(width/2 - 50, height/2), 30)
    circle2 = Circle(Point(width/2 + 50, height/2), 30)
    circle1.setFill(get_random_color())
    circle2.setFill(get_random_color())
    circle1.draw(win)
    circle2.draw(win)

    dx1 = get_random(10)
    dy1 = get_random(10)
    dx2 = get_random(10)
    dy2 = get_random(10)

    done = False
    while not done:
        key = win.checkKey()
        if key == 'q':
            done = True
        circle1.move(dx1, dy1)
        circle2.move(dx2, dy2)
        if hit_horizontal(circle1, win):
            dx1 = -dx1
        elif hit_horizontal(circle2, win):
            dx2 = -dx2
        elif hit_vertical(circle1, win):
            dy1 = -dy1
        elif hit_vertical(circle2, win):
            dy2 = -dy2
        elif did_collide(circle1, circle2):
            dx1 = -dx1
            dy1 = -dy1
            dx2 = -dx2
            dy2 = -dy2
        time.sleep(0.01)


def main():
    bumper()


if __name__ == '__main__':
    main()
