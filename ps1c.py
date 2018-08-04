#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:03:05 2018

@author: sclincoln27
"""



annual_salary = float(input("Enter your starting salary: "))

total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0.00
months = 0
epsilon = 100
low = 0
high = 10000
portion_saved = ((low + high) // 2) / 10000
steps = 1
u_broke = False
weird = False

def calc_savings(portion_saved, current_savings, annual_salary, months):
    """Input: savings rate as decimal
       Output: savings after 36 months"""
    semi_annual_raise = .07
    r = 0.04
    for i in range(36):
        monthly_salary = annual_salary / 12
        current_savings = current_savings + current_savings * r / 12 + monthly_salary * portion_saved
        months = months + 1
        if (months % 6 == 0):
            annual_salary = annual_salary * (1 + semi_annual_raise)
    return current_savings

savings = calc_savings(portion_saved, current_savings, annual_salary, months)
down_payment = total_cost * portion_down_payment

while(abs(savings - down_payment) > epsilon):
    steps += 1
    if steps > 14:
        weird = True
        break
    if savings < down_payment:
        low = int(portion_saved * 10000)
    else:
        high = int(portion_saved * 10000)
    portion_saved = ((low + high) // 2) / 10000
    savings = calc_savings(portion_saved, current_savings, annual_salary, months)
    
if weird:
    if calc_savings(1.0, current_savings, annual_salary, months) < down_payment:
        print("It is not possible to pay the down payment in three years.")
    else:
        print("Congrats! you broke it")
else:
    print("Best savings rate: " + str(portion_saved))
    print("Steps in bisection search: " + str(steps))

