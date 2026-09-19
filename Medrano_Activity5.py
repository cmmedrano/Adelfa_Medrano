# =========================
# STUDENT SCORE ENTRY
# DATE: SEPTEMBER 19, 2026
# =========================

# USE "try" AND "except" TO ENSURE THAT THE STUDENT ENTERS A NUMBER
try:
    score = float(input("Enter examination score: "))
    if 0 <= score <= 100: # THIS IS THE RANGE OF THE SCORE MUST BE IN
        print("Valid score.")
    else:
        print("Invalid score. Please enter a number within the range.")
except ValueError: # THIS OCCURS IF THE STUDENT ENTERS SOMETHING ELSE THAN A DIGIT
    print("Invalid input. Please enter a number.")
