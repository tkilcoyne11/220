"""
Name: Tucker Kilcoyne
mean.py

Problem: Given data points find the 3 means.

Certificate of Authenticity
I certify that this assignment is entirely my own work
"""
# 1. The program will take an input of data and solve for the RMS,
# Harmonic mean and Geometric mean
# 2. The inputs will be data points (numbers whole or decimals)
# and the output will be the three means defined
# 3. The step by step:
#       First the user will input their given data points
#       Next the algorithm will compute each of the means one at a time
#       Last it will print the solutions to the screen

import math

def main():
    inputs = []
    geometric = 1
    data = int(input("Enter number of elements: "))
    for i in range(0,data):
        ele = int(input(i))
        inputs.append(ele)

    squared_inputs = [number ** 2 for number in inputs]
    rms_average = math.sqrt(sum(squared_inputs)/len(squared_inputs))

    harmonic = [1 / number for number in inputs]
    harmonic_mean = len(inputs)/sum(harmonic)

    for item in inputs:
        geometric *= item
    geometric_mean = geometric ** (1/len(inputs))

    print(round(rms_average,3))
    print(round(harmonic_mean,3))
    print(round(geometric_mean,3))

if __name__ == '__main__':
    main()
