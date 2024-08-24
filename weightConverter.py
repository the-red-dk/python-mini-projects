#Python Weight Converter 
import sys 

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
  weight *= 2.205
  unit = "Lbs."
  
elif unit == "L":
  weight /= 2.205
  unit = "Kgs."

else:
  print(f"{unit} is not a valid unit")
  sys.exit()
    
print(f"Your weight is: {round(weight, 2)} {unit}")