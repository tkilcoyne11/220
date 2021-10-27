"""
Name: Tucker Kilcoyne
weighted_average.py
Certification of Authenticity
I certify that this assignment is entirely my own work
"""


def weighted_average(in_file_name, out_file_name):

    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    for i in in_file:
        split = i.split(":")
        full_name = split[0]
        grade = split[1]
        grades = grade.split()

        weight_sum = 0
        for j in range(0, len(grades), 2):
            weight = int(grades[j])
            weight_sum += weight

        s_weight = 0
        for k in range(0, len(grades) - 1, 2):
            g = k + 1
            weighted_grade = (int(grades[g]) * int(grades[k])) / 100
            s_weight += weighted_grade

        if weight_sum == 100:
            out_file.write(full_name + "'s average: " + str(round(s_weight, 1)) + '\n')

        elif weight_sum > 100:
            out_file.write(full_name + "'s average: " + "Error: The weights are more than 100." + "\n")

        else:
            out_file.write(full_name + "'s average: " + "Error: The weights are less than 100. " + "\n")

    in_file.close()
    out_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()
