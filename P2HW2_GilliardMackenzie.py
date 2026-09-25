# Mackenzie Gilliard
# 09/25/2026
# P2HW2
# This program asks the user for six module grades,
# stores them in a list, and displays the lowest grade,
# highest grade, sum, and average with proper formatting.

"""
PSEUDOCODE:
1. Ask user for Module 1–6 grades using separate input statements
2. Convert each input to float
3. Store all six grades in a descriptive list
4. Use built-in functions:
    - min() to find lowest grade
    - max() to find highest grade
    - sum() to find total of grades
    - average = sum / number of grades
5. Display results formatted exactly like assignment example
6. Average must show two decimal places
"""

# Step 1: Prompt for grades
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Step 2: Store grades in a list
grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Step 3: Calculate results
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 4: Display formatted output
print("\n------------ Results ------------")
print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")
print("---------------------------------")
