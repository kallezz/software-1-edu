import math


def calculate_unit_price(diameter_cm2, price):
    area_m2 = math.pi * ((diameter_cm2 / 2) ** 2) / 10000
    price_per_m2 = price / area_m2

    return price_per_m2


diam_input1 = float(input("Enter the diameter of the first pizza (cm): "))
price_input1 = float(input("Enter the price of the first pizza (euros): "))
diam_input2 = float(input("Enter the diameter of the second pizza (cm): "))
price_input2 = float(input("Enter the price of the second pizza (euros): "))
unit_price1 = calculate_unit_price(diam_input1, price_input1)
unit_price2 = calculate_unit_price(diam_input2, price_input2)

print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")
