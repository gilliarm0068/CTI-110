# Mackenzie Gilliard
# September 2025
# P4HW2
# This program calculates pay for multiple employees, including
# overtime pay, regular pay, and gross pay. It also displays
# totals for all employees entered.

"""
PSEUDOCODE

1. Initialize totals:
   - total_overtime_pay = 0
   - total_regular_pay = 0
   - total_gross_pay = 0
   - employee_count = 0

2. Ask user for employee name.

3. While employee name is not "Done":
   a. Ask for hours worked.
   b. Ask for pay rate.

   c. If hours worked is greater than 40:
      - Calculate overtime hours.
      - Calculate regular pay.
      - Calculate overtime pay.
   d. Otherwise:
      - Set overtime pay to 0.
      - Calculate regular pay.

   e. Calculate gross pay.

   f. Display employee pay information.

   g. Add values to running totals.
   h. Increase employee count by 1.

   i. Ask for next employee name.

4. When user enters "Done":
   - Display total overtime pay.
   - Display total regular pay.
   - Display total gross pay.
   - Display total number of employees.

5. End program.
"""

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# First employee name
employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":

    hours_worked = float(input("How many hours did " + employee_name + " work? "))
    pay_rate = float(input("What is " + employee_name + "'s pay rate? "))

    # Pay calculations
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40

        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)

    else:
        overtime_hours = 0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0

    gross_pay = regular_pay + overtime_pay

    # Display employee information
    print()
    print("----------------------------------------")
    print("Employee name:", employee_name)
    print()
    print("Hours Worked    Pay Rate    OverTime")
    print("----------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<10.1f}")
    print()
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Regular Pay:  ${regular_pay:.2f}")
    print(f"Gross Pay:    ${gross_pay:.2f}")
    print()

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Next employee
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

# Final totals
print("\nTotal number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")