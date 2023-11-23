# Python Program to print Strong Numbers from 1 to N
import math

maximum = int(input(" Please Enter the Maximum Value: "))

for Number in range(1, maximum):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10
    
    if (Sum == Number):
        print(" %d is a Strong Number" %Number)