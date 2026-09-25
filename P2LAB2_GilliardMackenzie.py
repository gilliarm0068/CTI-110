# Mackenzie Gilliard
# 09/25/2026
# P2LAB2
# This program stores vehicle MPG values in a dictionary,
# allows the user to select a vehicle, enter miles,
# and calculates the gallons of gas needed.

# ---------------- PSEUDOCODE ----------------
# 1. Create dictionary with vehicle: MPG pairs
# 2. Store dictionary keys in a variable
# 3. Print available vehicle options
# 4. Ask user to enter a vehicle (must match dictionary key)
# 5. Display MPG for selected vehicle
# 6. Ask user for miles they will drive
# 7. Calculate gallons needed = miles / MPG
# 8. Display gallons needed rounded to 2 decimals using f-string
# --------------------------------------------

# Step 1: Create dictionary
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Step 2: Store keys
keys = cars.keys()

# Step 3: Display keys
print("Available vehicles:")
print(keys)

# Step 4: Ask user for vehicle
vehicle = input("\nEnter a vehicle from the list above: ")

# Step 5: Display MPG
mpg = cars[vehicle]
print(f"\nThe {vehicle} gets {mpg} MPG.")

# Step 6: Ask user for miles
miles = float(input("Enter the number of miles you will drive: "))

# Step 7: Calculate gallons needed
gallons_needed = miles / mpg

# Step 8: Display result
print(f"\nGallons of gas needed: {gallons_needed:.2f}")
