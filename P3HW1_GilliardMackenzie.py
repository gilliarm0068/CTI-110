# Mackenzie Gilliard
# 10/06/2026
# P3HW1 – Debugging & Completing a Grade Program
# This program asks the user for six module grades, stores them in a list,
# calculates the lowest, highest, sum, and average, and then displays the
# correct letter grade based on the average.

"""
PSEUDOCODE:
1. Create an empty list for grades
2. Ask user for 6 grades, convert each to float, append to list
3. Calculate:
    - lowest grade using min()
    - highest grade using max()
    - sum of grades using sum()
    - average = sum / number of grades
4. Display results in formatted style
5. Determine letter grade:
    A = 90+
    B = 80–89
    C = 70–79
    D = 60–69
    F = below 60
6. Display letter grade
"""

# Step 1: Collect grades
grades = []

for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)

# Step 2: Calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 3: Display results
print("\n------------ Results ------------")
print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")

# Step 4: Determine letter grade
if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Letter Grade:      {letter}")
print("---------------------------------")
