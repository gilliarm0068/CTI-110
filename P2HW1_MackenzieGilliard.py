# Mackenzie Gilliard
# 09/24/2026
# P2HW1
# This program asks the user for their trip budget and expenses,
# calculates total expenses and remaining balance,
# and displays the results in a neatly formatted table.

# ---------------- PSEUDOCODE ----------------
# Ask user for their total budget
# Ask user for travel destination
# Ask user for gas cost
# Ask user for accommodation cost
# Ask user for food cost
# Add all expenses together
# Subtract total expenses from budget
# Display destination and money values in aligned columns
# --------------------------------------------

# Ask user for budget
budget = float(input("Enter your budget: "))

# Ask user for travel destination
destination = input("Enter your travel destination: ")

# Ask user for gas cost
gas = float(input("Enter amount you will spend on gas: "))

# Ask user for accommodation cost
accommodation = float(input("Enter amount you will spend on accommodation: "))

# Ask user for food cost
food = float(input("Enter amount you will spend on food: "))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining_balance = budget - total_expenses

# Display results
print("\n------------ Trip Summary ------------")
print(f"{'Destination:':<20}{destination}")
print(f"{'Budget:':<20}${budget:,.2f}")
print(f"{'Gas:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("--------------------------------------")
print(f"{'Total Expenses:':<20}${total_expenses:,.2f}")
print(f"{'Remaining Balance:':<20}${remaining_balance:,.2f}")
print("--------------------------------------")
