# =========================
# PAYMENT METHOD CHECKER
# DATE: SEPTEMBER 19, 2026
# =========================

# ACCEPTED PAYMENT METHODS
valid_payment_method = ["GCash", "Cash", "Maya"]

# INPUT STAGE - ASK THE PERSON WHICH PAYMENT METHOD WILL THEY USE
payment_method = input("Enter payment method: ")

# DECISION STAGE - CHECK IF THE PAYMENT METHOD OF THE CUSTOMER IS IN THE CHOICES
if payment_method in valid_payment_method:
    print("Valid payment method.")
else:
    print("Invalid payment method.")
