def CalculateTax(basePrice):
    return round((basePrice * .025), 2)

def CalculateTip(basePrice):
    tipDecimal = float(input("Enter Tip Percent: ")) / 100
    print()
    return round((tipDecimal * basePrice), 2)

# Start here :)
print("Restaurant Tip Calculator")
print()
basePrice = float(input("Base Price: "))
tax = CalculateTax(basePrice)
tip = CalculateTip(basePrice)

print("Receipt")
print("---")
print("Original Price: $", basePrice)
print("---")
print()
print("Tax: $", tax)
print("Tip: $", tip)
print()
print("---")
print("Total Price: $", round((basePrice + tax + tip), 2))
print("---")

