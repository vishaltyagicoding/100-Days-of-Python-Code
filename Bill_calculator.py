# Welcome to 'Bill' calculator.
# What was the total bill?
# How many peoples to split this bill?
# do you want to give tip? Type 'yes' or no
# What percentage would you like to give? 10, 12, or 15?
# each person should pay:
# Thanks for visit in restaurant
import math

print("Welcome to 'Bill' calculator.")

total_bill = int(input("What was the total bill? "))

split_in_each_person = int(input("How many peoples to split this bill? "))

each_person = total_bill / split_in_each_person

user_input = input("do you want to give tip? Type 'yes' or no ")
tip_calculate = 0
if user_input == 'yes':
    tip = int(input("What percentage would you like to give? 10, 12, or 15? "))

    tip_calculate = each_person / 100 * tip

each_person_pay = each_person + tip_calculate

print(f"each person should pay: {math.floor(each_person_pay)}")






