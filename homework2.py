"""
Author: Luke Monroe
Date: 1/30/2024
Purpose: This program will ask the user to enter the weight of a package and then displays the shipping charges.
"""

packageWeight = float(input("Enter the weight of the package you want to ship: "))

if packageWeight <= 2:
    shippingCharge = packageWeight * 1.10
elif packageWeight > 2 and packageWeight <= 6:
    shippingCharge = packageWeight * 2.20
elif packageWeight > 6 and packageWeight <= 10:
    shippingCharge = packageWeight * 3.70
else:
    shippingCharge = packageWeight * 3.80

print("The shipping charge for your package is $", round(shippingCharge, 2))

"""
Sudocode:
Declare Real packageWeight, shippingCharge

Display "Enter the weight of the package you want to ship: "
Input packageWeight

If packageWeight <= 2 Then
    shippingCharge = packageWeight * 1.10
Else If packageWeight > 2 and packageWeight <= 6 Then
    shippingCharge = packageWeight * 2.20
Else If packageWeight > 6 and packageWeight <= 10 Then
    shippingCharge = packageWeight * 3.70
Else
    shippingCharge = packageWeight * 3.80
End If

Display "The shipping charge for your package is $", shippingCharge


Process: Declare Real packageWeight, shippingCharge

Output: "Enter the weight of the package you want to ship: "
Input: packageWeight

Process: If packageWeight <= 2 Then
Process:    shippingCharge = packageWeight * 1.10
Process: Else If packageWeight > 2 and packageWeight <= 6 Then
Process:     shippingCharge = packageWeight * 2.20
Process: Else If packageWeight > 6 and packageWeight <= 10 Then
Process:     shippingCharge = packageWeight * 3.70
Process: Else
Process:     shippingCharge = packageWeight * 3.80
Process: End If

Output: "The shipping charge for your package is $", shippingCharge
"""
