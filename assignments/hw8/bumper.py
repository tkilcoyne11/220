"""
Tucker Kilcoyne
bumper.py
"""

from random import randint
from graphics import GraphWin, Circle, Point, color_rgb


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball1, ball2):
    x_collide = abs(ball1.getCenter().getX() - ball2.getCenter().getX())
    y_collide = abs(ball1.getCenter().getY() - ball2.getCenter().getY())
    radius1 = ball1.getRadius()
    return bool(x_collide <= radius1 and y_collide <= radius1)


def hit_horizontal(ball, win):
    top = ball.getCenter().getY() - ball.getRadius() <= 0
    bottom = ball.getCenter().getY() + ball.getRadius() >= win.getHeight()
    return bool(top or bottom)


def hit_vertical(ball, win):
    left = ball.getCenter().getX() + ball.getRadius() >= win.getWidth()
    right = ball.getCenter().getX() - ball.getRadius() <= 0
    return bool(left or right)


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def bumper():
    win = GraphWin("Bumper", 600, 600)

    circle1 = Circle(Point(100, 200), 30)
    circle1.setFill(get_random_color())
    circle2 = Circle(Point(400, 500), 30)
    circle2.setFill(get_random_color())

    circle1.draw(win)
    circle2.draw(win)

    movement1 = [get_random(9), get_random(9)]
    movement2 = [get_random(9), get_random(9)]

    while True:

        if did_collide(circle1, circle2):
            movement1[0] = -movement1[0]
            movement1[1] = -movement1[1]
            movement2[0] = -movement2[0]
            movement2[1] = -movement2[1]

        if hit_vertical(circle1, win):
            movement1[0] = -movement1[0]
        if hit_horizontal(circle1, win):
            movement1[1] = -movement1[1]

        if hit_vertical(circle2, win):
            movement2[0] = -movement2[0]
        if hit_horizontal(circle2, win):
            movement2[1] = -movement2[1]

        circle1.move(movement1[0], movement1[1])
        circle2.move(movement2[0], movement2[1])


def main():
    bumper()



if __name__ == '__main__':
    main()
