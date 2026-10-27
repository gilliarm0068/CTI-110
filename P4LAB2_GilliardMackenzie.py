# Mackenzie Gilliard
# September 2025
# P4LAB2
# This program displays a multiplication table for a positive integer.
# The user can choose to run the program multiple times.

"""
PSEUDOCODE

1. Start program.
2. Set run_again equal to "yes".

3. While run_again is "yes":
    a. Ask the user to enter an integer.
    b. If the integer is greater than or equal to 0:
        i. Display the multiplication table from 1 through 12.
        ii. Use a for loop to calculate and display each result.
    c. Otherwise:
        i. Display a message that negative values are not accepted.
    d. Ask the user if they want to run the program again.
    e. Store the user's response in run_again.

4. If the user enters "no":
    a. Exit the loop.
    b. Display a goodbye message.

5. End program.
"""

run_again = "yes"

while run_again.lower() == "yes":

    number = int(input("Enter an integer: "))

    if number >= 0:
        print()

        for count in range(1, 13):
            print(f"{number} * {count} = {number * count}")

    else:
        print("This program does not handle negative values")

    print()
    run_again = input("Would you like to run again? (yes/no): ")

print("Exiting program...")
