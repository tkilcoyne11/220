"""
Name: Tucker Kilcoyne
traffic.py

Problem:

Certification of Authenticity
I certify that this assignment is entirely my own work
"""


def main():
    acc = 0
    inputs = []
    outputs = []
    data = int(input("How many roads were surveyed? "))
    for i in range(0, data):
        ele = int(input("How many days was road " + str(i + 1) + " surveyed? "))
        inputs.append(ele)
        for j in range(0, ele):
            cars = int(input("How many cars traveled on day " + str(j + 1) + "? "))
            outputs.append(cars)
        average1 = sum(outputs) / len(outputs)
        acc += sum(outputs)
        outputs.clear()
        print("Road " + str(i + 1) + " average vehicles per day: " + str(round(average1, 2)))
    average2 = acc / data
    print("Total number of vehicles traveled on all road: " + str(acc))
    print("Average number of vehicles per road: " + str(round(average2, 2)))


if __name__ == '__main__':
    main()
