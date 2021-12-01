"""
Name: Tucker Kilcoyne
lab13.py
"""


def is_in_binary(value, values):
    mid_value = values[len(values) // 2]
    while mid_value != value and len(values) != 1:
        if mid_value > value:
            values = values[:len(values) // 2]
        if mid_value < value:
            values = values[len(values) // 2 + 1:]
        mid_value = values[len(values) // 2]
    if mid_value == value:
        return True
    return False


def selection_search(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
            pos = lowest
        values[i], values[pos] = values[pos], values[i]


def get_area(rect):
    P1 = rect.getP1()
    P2 = rect.getP2()
    w = abs(P1.getX() - P2.getY())
    h = abs(P1.getY() - P2.getY())
    return w * h


def rectangles(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_search(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]
    print(areas)


def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    acc = 0
    for i in range(len(data)):
        acc += 1
        if int(data[i]) >= 830:
            print("Alert! At", acc, "seconds the trading volume exceeded 830")
        elif int(data[i]) >= 500:
            print("Caution! At", acc, "seconds the trading volume exceeded 500")


def main():
    print(is_in_binary(3, [1, 2, 3]))
    print(trade_alert("trades.txt"))


if __name__ == '__main__':
    main()
