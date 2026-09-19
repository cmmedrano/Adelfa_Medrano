# =========================
# GRADE CHECKER
# DATE: SEPTEMBER 19, 2026
# =========================

# INPUT STAGE - ASK THE USER FOR THEIR GRADE
grade = float(input("Enter your grade: "))

# DECISION STAGE - CHECK IF THE GRADE THAT THE USER TYPED IN IS WITHIN THE RANGE
if 0 <= grade <= 100:
    print("Valid grade.")
else:
    print("Invalid grade. Grade must be between 0 and 100.")
