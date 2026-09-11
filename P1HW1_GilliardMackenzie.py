# Mackenzie Gilliard
# 09/11/2026
# P1HW1
# This program asks the user for a base and exponent, calculates the result,
# then asks for three integers, adds the first two, subtracts the third,
# and displays all results to the user.

# --- Exponent Section ---
base = int(input("Enter an integer for the base value: "))
exponent = int(input("Enter an integer for the exponent: "))

result = base ** exponent

print("\n------------------------------")
print(base, "raised to the power of", exponent, "is", result, "!!!")
print("------------------------------\n")

# --- Add/Subtract Section ---
print("Now enter three integers.")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_result = num1 + num2
final_result = sum_result - num3

print("\n------------------------------")
print(num1, "+", num2, "=", sum_result)
print(sum_result, "-", num3, "=", final_result)
print("------------------------------")
