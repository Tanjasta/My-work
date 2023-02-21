# div.py
# Author: Tatjana Staunton
# This program reads in two numbers and divides the first one by the second
# Outputs the int answer and remainder

x = int (input ("Enter first number"))
y = int (input ("Enter the number you want to divide by: "))
answer = int (x//y) #// gives the int division
reminder = x % y    # % gives the reminder
print (" {} divided by {} is {} with reminder {}" .format (x, y, answer, reminder))
