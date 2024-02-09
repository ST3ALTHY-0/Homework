"""
Author: Luke Monroe
Date: 1/22/2024
Description: This program will calculate and display the subtotal, sales tax, and total of four items.
"""

#input
priceOne = float(input("Enter the price of the first item: "))
priceTwo = float(input("Enter the price of the second item: "))
priceThree = float(input("Enter the price of the third item: "))
priceFour = float(input("Enter the price of the fourth item: "))

#process
subtotal = priceOne + priceTwo + priceThree + priceFour
Salestax = subtotal * 0.06
total = subtotal + Salestax

#output
print("The subtotal is $", round(subtotal, 2))
print("The sales tax is $", round(Salestax, 2))
print("The total is $", round(total, 2))
