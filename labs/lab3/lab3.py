"""
Name: Tucker Kilcoyne
lab3.py
"""

def average():
    inputs = []
    data = int(input("Enter the number of grades to input: "))
    for i in range(0,data):
        ele = float(input("Enter your grade on HW "+str(i+1)+" "))
        inputs.append(ele)
    average = sum(inputs) / len(inputs)
    print(round(average,2))

def tip_jar():
    acc = 0
    for i in range(5):
        donation = float(input("Enter how much you are donating? "))
        acc += donation
    print(acc)

def newton():
    x = int(input("Enter what the number x is: "))
    refine = int(input("Enter how many times to improve the approximation: "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)

def sequence():
    x = int(input("Enter how many terms in a series: "))
    for i in range(1, x+1):
        y = 1 + (i // 2 * 2)
        print(y)
    # // - integer division ex: 5//2 = 2
    # % - remainder division ex: 5%2 = 1

def pi():
    n = int(input("Enter the number of terms in the series: "))
    acc = 1
    for i in range(n):
        num = 2 + (i // 2 * 2)
        demon = 1 + ((i+1) // 2 * 2)
        acc *= (num/demon)
    print(acc * 2)

#average()
#tip_jar()
#newton()
#sequence()
#pi()