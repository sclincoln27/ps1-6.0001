#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:33:14 2018

@author: sclincoln27
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of you salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0.00
r = 0.04
monthly_salary = annual_salary / 12
months = 0

while (current_savings < total_cost * portion_down_payment):    
    current_savings = current_savings + current_savings * r / 12 + monthly_salary * portion_saved
    months = months + 1
    
print("\nNumber of months: " + str(months))