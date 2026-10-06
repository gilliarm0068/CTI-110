# Mackenzie Gilliard
# 10/06/2026
# P3LAB – Change Calculator
# This program takes a money amount and calculates the most efficient
# number of dollars, quarters, dimes, nickels, and pennies needed.

# --- Pseudocode ---
# 1. Ask user for a money amount (float)
# 2. Convert to cents by multiplying by 100 and casting to int
# 3. Use floor division (//) to find each coin
# 4. Subtract the value from the total each time
# 5. Only display coins that are needed
# 6. Use singular/plural correctly

amount = float(input("Enter amount of money: "))

# Convert to cents
cents = int(amount * 100)

# Calculate coins
dollars = cents // 100
cents -= dollars * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

# Output
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
D