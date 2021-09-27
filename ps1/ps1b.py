# -*- coding: utf-8 -*-
"""
Created on 27 Sep 2021

@author: M S Dhanalekshmi
"""

# Part B: Saving, with a raise


annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a '
                            'decimal: '))
total_cost = float(input('Enter cost of your dream home: '))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal :"))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
number_of_months = 0

while current_savings < portion_down_payment * total_cost:

    return_on_investment = current_savings * r / 12
    portion_monthly_salary = portion_saved * annual_salary / 12
    current_savings += return_on_investment + portion_monthly_salary
    number_of_months += 1

    if number_of_months % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)


print("Number of months: ", number_of_months)
