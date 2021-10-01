"""
Name: Tucker Kilcoyne
greeting.py
Problem: Create a graphical greeting card
Certificate of Authenticity
I certify that this assignment is entirely my own work
"""
import time
from graphics import GraphWin, Rectangle, Point, Text, Image, Line

# needed to create function create_window inorder to conform to length of statements and variables test


def create_window():

    # Set up the window
    width = 500
    height = 600
    win = GraphWin("Greeting Card", width, height)
    win.setBackground("#CBC3E3")
    win.setCoords(0, 0, 50, 60)

    # Box for Text
    greet_box = Rectangle(Point(7, 55), Point(43, 45))
    greet_box.setFill("#FFC0CB")
    greet_box.setOutline("white")
    greet_box.draw(win)
    return win

# This is main function


def main():

    # Create the window
    win = create_window()

    # Greeting text
    greet = Text(Point(25, 50), "Happy Valentine's Day!")
    greet.setTextColor("white")
    greet.setSize(32)
    greet.setStyle("bold")
    greet.setFace("times roman")
    greet.draw(win)

    # Add the image for a heart
    heart = Image(Point(25, 30), "heart.gif")
    heart.draw(win)

    # Draw the arrow
    line = Line(Point(-13, 30), Point(2, 30))
    line.setArrow("last")
    line.setFill("white")
    line.setOutline("white")
    line.setWidth(3)
    line.draw(win)

    # Move the arrow
    for i in range(0, 7):
        line.move(i, 0)
        time.sleep(0.15)

    # Pause before animation
    time.sleep(0.05)

    # Heart Animation
    heart.undraw()
    line.undraw()

    for i in range(1, 7):
        img = Image(Point(25, 30), "img" + str(i) + ".gif")
        img.draw(win)
        time.sleep(0.15)
        img.undraw()

    Image(Point(25, 30), "img7.gif").draw(win)
    time.sleep(0.25)

    # Box for message
    message_text_box = Rectangle(Point(15, 32), Point(35, 28))
    message_text_box.setFill("#FFC0CB")
    message_text_box.setOutline("white")
    message_text_box.draw(win)

    # Message for person
    message = Text(Point(25, 30), "Someone Loves You")
    message.setTextColor("white")
    message.setSize(20)
    message.setStyle("italic")
    message.setFace("times roman")
    message.draw(win)
    time.sleep(0.75)

    # Box for Close Text
    close_text_box = Rectangle(Point(12, 13), Point(38, 7))
    close_text_box.setFill("#FFC0CB")
    close_text_box.setOutline("white")
    close_text_box.draw(win)

    # Close text
    close_text = Text(Point(25, 10), "Click Anywhere to Close")
    close_text.setTextColor("white")
    close_text.setSize(20)
    close_text.setStyle("bold")
    close_text.setFace("times roman")
    close_text.draw(win)

    # Pause and wait for mouse click before close
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
