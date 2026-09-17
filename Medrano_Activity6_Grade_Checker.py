# ACTIVITY 6: PAYMENT METHOD CHECKER
# AUTHOR: CHRIZZIA JILLIAN M. MEDRANO
# DATE: 09/17/2026

# ---ASSIGN ACCEPTABLE VALUES FOR PAYMENT METHOD---
valid_payment_method = ["GCash", "Cash", "Maya"]
# ---INPUT STAGE---
# Ask for the person's payment method
payment_method = str(input("Select payment method: "))
# ---DECISION STAGE---
# Determines if the payment method  is allowed
if payment_method in valid_payment_method:
    print("Valid payment method.")

else:
    print("Invalid payment method.")
