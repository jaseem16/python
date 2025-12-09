rates = {
    "INR": 1,
    "USD": 83,
    "AED": 22.6
}

amount = float(input("Amount: "))
from_curr = input("From (INR/USD/AED): ")
to_curr = input("To (INR/USD/AED): ")

converted = amount * (rates[from_curr] / rates[to_curr])
print("Converted Amount:", converted)
