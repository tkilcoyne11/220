"""
Name: Tucker Kilcoyne
vigenere.py
"""

from graphics import GraphWin, Point, Text, Entry, Rectangle


def code(message, keyword):

    window_width = 500
    window_height = 400
    win = GraphWin("Vigenere", window_width, window_height)
    win.setCoords(0, 0, 50, 40)

    # Message
    message_text_pt = Point(10, 35)
    message_text = Text(message_text_pt, "Message to code: ")
    message_text.setSize(20)
    message_text.setStyle("bold")
    message_text.setFace("times roman")
    message_text.draw(win)

    # Text box for message
    message_text_box = Entry(Point(message_text_pt.getX() + 22, message_text_pt.getY()), 45)
    message_text_box.draw(win)

    # Keyword text
    keyword_text_pt = message_text_pt.clone()
    keyword_text_pt.move(1, -5)
    keyword_text = Text(keyword_text_pt, "Enter Keyword: ")
    keyword_text.setSize(15)
    keyword_text.setStyle("bold")
    keyword_text.setFace("times roman")
    keyword_text.draw(win)

    # Text box for keyword
    keyword_text_box = Entry(Point(keyword_text_pt.getX() + 15, keyword_text_pt.getY()), 25)
    keyword_text_box.draw(win)

    # Encode Button
    r = Rectangle(Point(20, 25), Point(30, 20))
    r.setOutline("grey")
    r.draw(win)

    # Encode Text
    encode_text = Text(Point(25, 22.5), "Encode")
    encode_text.draw(win)

    win.getMouse()
    win.close()


def main():
    code("hello", "abc")


if __name__ == '__main__':
    main()
