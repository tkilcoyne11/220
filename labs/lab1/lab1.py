"""
Name: Tucker Kilcoyne
lab1.py
"""

def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("area = ", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("volume = ", volume)

def shooting_percentage():
    shots_made = eval(input("Enter the player's shots made: "))
    total_shots = eval(input("Enter the player's total shots: "))
    percentage = (shots_made / total_shots) * 100
    print("Shooting percentage = ", percentage,"%")

def coffee():
    coffee_costs = 10.50
    shipping_costs = 0.86
    overhead_cost = 1.50
    number_of_pounds = eval(input("Enter the number of pounds of coffee purchased: "))
    total_cost = (number_of_pounds * (coffee_costs + shipping_costs)) + overhead_cost
    print("Total cost of coffee = $",total_cost)

def kilometers_to_miles():
    number_of_kilometers = eval(input("Enter the number of kilometers: "))
    miles_conversion = 1.61
    number_of_miles = number_of_kilometers / miles_conversion
    print("Total number of miles traveled = ",number_of_miles,"mi")

#calc_area()
#calc_volume()
#shooting_percentage()
#coffee()
#kilometers_to_miles()
