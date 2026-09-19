# =========================
# PIN VALIDATOR
# DATE: SEPTEMBER 19, 2026
# =========================

# USE "try" AND "except" TO ENSURE THAT THE PIN IS ONLY DIGITS
try:
    pin = input("Create a 6-digit PIN: ")
    if len(pin) == 6 and pin.isdigit(): # THIS LINE DECIDES IF THE PIN'S LENGTH IS ONLY SIX AND IF THEY ARE ALL DIGITS
        print("Valid PIN.")
    else:
        print("Invalid PIN. Enter exactly 6 digits.")

except ValueError: # THIS HAPPENS IF THE USER TYPES SOMETHING ELSE THAN A DIGIT
    print("Invalid PIN. Enter exactly 6 digits")
