"""
Name: Tucker Kilcoyne
Partner: Landon Badgett
lab7.py
"""

import math


def cash_conversion():
    x = int(input("Enter an integer: "))
    y = ("{:.2f}".format(x))
    print("$"+y)


def encode(s, key):
    acc = ""
    for c in s:
        acc += chr((ord(c) - 97 + key) % 26 + 97)
    return acc


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4/3)*math.pi*(radius ** 3)
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc += i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc += i ** 3
    return acc


def encode_better(s, k):
    acc = ""
    for i in range(len(s)):
        c = ord(s[i])
        key = k[i]
        key = ord(key) - 97
        c = c + key
        new_c = chr(c)
        acc += new_c
    return acc


def main():
    cash_conversion()
    encode()
    print(
        sphere_area(5),
        sphere_volume(5),
        sum_n(5),
        sum_n_cubes(5)
    )
    encode_better()
    pass



main()
