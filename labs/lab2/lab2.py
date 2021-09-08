"""
Name: Tucker Kilcoyne
lab2.py
"""

import math

def sum_of_threes():
    bound = int(input("Enter an upper bound: "))
    acc = 0
    for i in range(0,bound+1,3):
        acc += i # this equals acc = acc + i
    print(acc)

def multiplication_table():
    for h in range(1,11):
        for l in range(1,11):
            print(h * l, end=" ")
        print()
    # /n represents the enter key

def triangle_area():
    a = float(input("Enter length of a: "))
    b = float(input("Enter length of b: "))
    c = float(input("Enter length of c: "))
    s = (a+b+c)/2
    x = s*(s-a)*(s-b)*(s-c)
    area = math.sqrt(x)
    print(round(area,2))

def sumSquares():
    start = int(input("Enter starting value: "))
    end = int(input("Enter ending value: "))
    acc = 0
    for i in range(start,end+1):
        acc += (i*i)
    print(acc)

def power():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    acc = 1
    for i in range(exponent):
        acc *= base
    print(acc)

#sum_of_threes()
#multiplication_table()
#triangle_area()
#sumSquares()
#power()