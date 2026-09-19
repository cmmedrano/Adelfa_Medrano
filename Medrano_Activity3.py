# =========================
# STUDENT ID CHECKER
# DATE: SEPTEMBER 19, 2026
# =========================

# IMPORT RE SO "re.fullmatch(x, y)" WILL WORK
import re

# INPUT STAGE - ASK THE STUDENT'S ID
id_number = input("Enter Student ID: ")

# PATTERN - THE PATTERN MUST BE USED TO MAKE THE STUDENT ID VALID
pattern = r"\d{4}-\d{4}"

# DECISION STAGE - DECIDE IF THE STUDENT ID IS VALID OR INVALID
if re.fullmatch(pattern, id_number):
    print("Valid Student ID.")
else:
    print("Invalid Student ID.")
