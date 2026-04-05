#!/usr/bin/env python3
# coding: utf-8
try:
    print("Enter your name")
    name = str(input("-->"))

    print("Enter the meal's price")
    price = float(input("-->"))

    print("Enter the quality")
    quality = str(input("-->"))

    if quality == "bad":
        tip = price * 0.00
    elif quality == "normal":
        tip = price * 0.10
    elif quality == "excellent":
        tip = price * 0.20
    else:
        print("Enter in the last question either 'bad, normal or excellent'")

    total = price + tip
    print(f"Hello {name}, the tip is {tip} and the total bill is {total}")
except ValueError:
    print("Enter Compatible answers on each field!")
