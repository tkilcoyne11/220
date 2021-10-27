"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import GraphWin, Point, Circle, Text
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
    pass


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    pass


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
    pass


def writeSumOfSquares():
    ifn = input("Enter the input file: ")
    infile = open(ifn, "r")
    outfile = open("output.txt", "w")
    for i in infile:
        numbers = i.split()
        toNumbers(numbers)
        squareEach(numbers)
        total_sum = sumList(numbers)
        outfile.write("Sum of squares= " + str(total_sum) + "\n")


def starter():
    weight = float(input("Enter the weight: "))
    wins = float(input("Enter the number of wins: "))
    if 150 <= weight <= 160 and wins >= 5:
        print("The player would be a starter")
    elif weight > 199 or wins > 20:
        print("The player would be a starter")
    else:
        print("The player would not be a starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")


def circleOverlap():
    w = 500
    h = 500
    win = GraphWin("Circle Overlap", w, h)
    text_pt = Point(w / 2, h - 50)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle1 = Circle(p1, r1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, r2)
    circle2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    if distance < (r1 + r2):
        text1 = Text(text_pt, "The circles overlap.")
        text1.draw(win)

    else:
        text2 = Text(text_pt, "The circles do not overlap.")
        text2.draw(win)

    win.getMouse()
    win.close()


def main():
    nums = [1, 2, 3]
    strList = ["3", "5.7", "2"]
    year = 2100
    # addTen(nums)
    # squareEach(nums)
    # sumList(nums)
    # toNumbers(strList)
    # writeSumOfSquares()
    # starter()
    # leapYear(year)
    # circleOverlap()
    print(nums)
    print(strList)
    print(year)

    pass


main()
