# Mackenzie Lastname
# 10/07/2026
# P3HW2 – Pay Calculator
# This program asks for employee info, calculates overtime, regular pay,
# and gross pay using if/else logic.

"""
PSEUDOCODE:
1. Ask user for employee name
2. Ask for hours worked
3. Ask for pay rate
4. If hours > 40:
       overtime_hours = hours - 40
       overtime_pay = overtime_hours * (pay_rate * 1.5)
       regular_pay = 40 * pay_rate
   Else:
       overtime_hours = 0
       overtime_pay = 0
       regular_pay = hours * pay_rate
5. gross_pay = regular_pay + overtime_pay
6. Display all values formatted like the example
"""

# Step 1: Inputs
emp_name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Step 2: Calculations
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours * pay_rate

gross_pay = regular_pay + overtime_pay

# Step 3: Output
print("----------------------------------------")
print(f"Employee Name: {emp_name}")
print()
print(f"Hours Worked:     {hours:10.2f}")
print(f"Pay Rate:         {pay_rate:10.2f}")
print(f"Overtime Hours:   {overtime_hours:10.2f}")
print(f"Overtime Pay:     {overtime_pay:10.2f}")
print(f"Regular Pay:      {regular_pay:10.2f}")
print("----------------------------------------")
print(f"Gross Pay:        {gross_pay:10.2f}")
