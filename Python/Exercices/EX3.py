#!/usr/bin/env python3
# coding: utf-8
try:
    print("Enter your name")
    name = str(input("-->"))

    print("Enter the price of an item")
    oneprice = float(input("-->"))

    print("Enter the quantity")
    quantity = int(input("-->"))

    print("enter you level 'primary, secondary or university'")
    level = str(input("-->"))

    final = oneprice * quantity
    if  level    == "primary":
        discount = final * 0.05
    elif level  == "secondary":
        discount = final * 0.10
    elif level  == "university":
        discount = final * 0.20
    else:
        print("Enter in the last question either 'primary, secondary or university'")

    finalprice = final - discount
    print(f"Hello {name}, the price before discount is {final} and your price after the discount is {finalprice}")

except ValueError:
    print("Enter Compatible answers on each field!")
