"""
Name: Tucker Kilcoyne
interest.py

Problem: calculate monthly interest expense on credit card debt

Certificate of Authenticity
I certify that this assignment is entirely my own work
"""

def main():
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    days_in_billing_cycle = eval(input("Enter number of days in the billing cycle: "))
    previous_net_balance = eval(input("Enter the previous net balance: "))
    payment_amount = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day in which the payment was made: "))
    step1 = previous_net_balance * days_in_billing_cycle
    step2 = payment_amount * (days_in_billing_cycle - payment_day)
    step3 = step1 - step2
    step4 = step3 / days_in_billing_cycle # this is the average annual balance
    monthly_interest_rate = ((annual_interest_rate/100) / 12)
    monthly_interest_charge = step4 * monthly_interest_rate
    answer = round(monthly_interest_charge, 2)
    print(answer)
if __name__ == '__main__':
    main()
