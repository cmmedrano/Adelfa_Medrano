# ACTIVITY 3: FIND THE HYPOTENUSE
# -------------------------------
# IMPORT MATH LIBRARY FOR THE SQUARE ROOT AND POWER FUNCTION
# -------------------------------
import math
# INPUT NEEDED FOR THE LENGTHS OF THE TRIANGLE, IT NEEDS TO BE A FLOAT
# -------------------------------
length_a = float(input("Enter the length of the shorter side: "))
length_b = float(input("Enter the length of the second shorter side: "))
# COMPUTATION OF THE TRIANGLE'S HYPOTENUSE AFTER TYPING IN THE LENGTHS
# -------------------------------
hypotenuse = math.sqrt(pow(length_a,2 ) + pow(length_b,2))
# ANSWER AFTER COMPUTING THE TRIANGLE'S HYPOTENUSE
# -------------------------------
print(f"The hypotenuse is {hypotenuse:.2f}")