"""
Tucker Kilcoyne
button.py
"""


class Button:
    """
    Button Class for the Three Door Game
    """

    def __int__(self, shape, label):
        """
        Constructor: shape of the button, label on the button
        """
        self.shape = shape
        self.label = label


    def get_label(self):
        return self.label


    def draw(self, win):
        return self.draw(win)


    def undraw(self):
        return self.undraw()


    def is_clicked(self, point):
        if point == self.label:
            return True
        return False


    def color_button(self, color):



    def set_label(self, label):
        self.label = label