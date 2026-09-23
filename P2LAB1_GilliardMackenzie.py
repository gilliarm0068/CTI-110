# Mackenzie Gilliard
# 09/23/2026
# P2LAB1
# This program asks the user for the radius of a circle, then calculates
# the diameter, circumference, and area. It displays each value with the
# required formatting.

# Pseudocode:
# 1. Ask user for radius (float)
# 2. Calculate diameter = 2 * radius
# 3. Calculate circumference = 2 * pi * radius
# 4. Calculate area = pi * radius^2
# 5. Display results with correct decimal formatting

import math

# Get radius from user
radius = float(input("Enter the radius: "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display results with required formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
