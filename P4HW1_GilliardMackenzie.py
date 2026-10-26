# Mackenzie Gilliard
# 10/26/2026
# P4HW1
# This program collects a number of scores from the user, validates each score,
# drops the lowest score, calculates the average of the remaining scores,
# and displays the correct letter grade.

"""
PSEUDOCODE:
1. Ask user how many scores they want to enter
2. Create an empty list to store scores
3. Loop for the number of scores:
      a. Ask user for a score
      b. While score is invalid (not 0–100):
             - Tell user it's invalid
             - Ask again
      c. Add valid score to list
4. After loop ends:
      a. Find lowest score
      b. Remove lowest score from list
      c. Calculate average of remaining scores
      d. Determine letter grade:
            A = 90+
            B = 80–89
            C = 70–79
            D = 60–69
            F = below 60
5. Display results to user
"""

# Step 1: Ask for number of scores
num_scores = int(input("How many scores would you like to enter? "))

# Step 2: Create list
scores = []

# Step 3: Loop to collect scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i+1}: "))

    # Validate score
    while score < 0 or score > 100:
        print("INVALID score entered! Score must be between 0 and 100.")
        score = float(input(f"Re-enter score #{i+1}: "))

    scores.append(score)

# Step 4: Process scores
lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

# Determine letter grade
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

# Step 5: Display results
print("\n---------- Results ----------")
print(f"Lowest score: {lowest}")
print(f"Modified score list: {scores}")
print(f"Average of scores: {average:.2f}")
print(f"Letter grade: {letter}")
print("-----------------------------")
