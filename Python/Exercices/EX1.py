#!/usr/bin/env python3
# coding: utf-8
try:
    print("Enter your name")
    name = str(input("-->"))

    print("Enter the price of an item")
    oneprice = float(input("-->"))

    print("Enter the quantity")
    quantity = int(input("-->"))

    print("Are you regular, member or vip?")
    member = str(input("-->"))

    final = oneprice * quantity
    if member == "vip":
        discount = final * 0.18
    elif member == "member":
        discount = final * 0.08
    elif member == "regular":
        discount = final * 0.00
    else:
        print("Enter in the last question either 'vip, member or regular'")
    finalprice = final - discount
    print(f"Hello {name}, the price before discount is {final} and your price after the discount is {finalprice}")
except ValueError:
    print("Enter Compatible answers on each field!")
