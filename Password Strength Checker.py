import re

password = input("Enter password: ")

strength = 0
if len(password) >= 8: strength += 1
if re.search(r"[A-Z]", password): strength += 1
if re.search(r"[a-z]", password): strength += 1
if re.search(r"\d", password): strength += 1
if re.search(r"[!@#$%^&*]", password): strength += 1

print("Strength:", ["Weak", "Medium", "Strong", "Very Strong"][strength-1])
