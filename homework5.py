"""
Author: Luke Monroe
Date: 4/3/2024
Purpose: This program will compute the summation of the square of two numbers
"""
import random

def main():
    num1=0
    num2=0
    total=0
    
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print("The first random number is: ", num1)
    print("The second random number is: ", num2)

    total = calculateSum(num1, num2)

    print("The sum of the squares of the random numbers is: ", total)

def calculateSum(num1, num2):
    total=0

    num1 = num1 * num1
    num2 = num2 * num2

    print("The square of the first random number is: ", num1)
    print("The square of the second random number is: ", num2)

    return num1 + num2

main()
