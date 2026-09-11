# Mackenzie Gilliard
# 09/11/2026
# P1HW2
# This program asks the user for their trip budget and expenses,
# calculates total expenses, subtracts them from the budget,
# and displays the results.

# ---------------- PSEUDOCODE ----------------
# Ask user for their total budget
# Ask user for travel destination
# Ask user for gas cost
# Ask user for accommodation cost
# Ask user for food cost
# Add all expenses together
# Subtract total expenses from budget
# Display destination, expenses, and remaining balance
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
print("Travel Destination:", destination)
print("Budget:", budget)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)
print("--------------------------------------")
