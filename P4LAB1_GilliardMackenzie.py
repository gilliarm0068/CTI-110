# Mackenzie Gilliard
# 10/26/2026
# P4LAB1
# This program draws a house using turtle graphics.
# It uses BOTH a for loop (square) and a while loop (triangle).
# Background and turtle colors are changed.

import turtle

# --- Setup ---
wn = turtle.Screen()
wn.bgcolor("lightblue")       # background color

t = turtle.Turtle()
t.color("darkred")            # turtle drawing color
t.pensize(3)
t.speed(3)

# --- Pseudocode ---
# 1. Draw a square using a for loop
# 2. Move turtle to top of square
# 3. Draw a triangle roof using a while loop
# 4. End program

# --- Draw Square (for loop) ---
for i in range(4):
    t.forward(100)
    t.left(90)

# --- Move to top of square ---
t.left(90)
t.forward(100)
t.right(90)

# --- Draw Triangle (while loop) ---
count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

# --- Finish ---
t.hideturtle()
wn.mainloop()
