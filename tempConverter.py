#Temperature converter 

import sys 

unit = input("Enter what to convert: Celsius or Farenheit: (C or F) ")

temp = float(input(f"Enter the degree {unit}: "))

if unit == "C" or unit == "Celsius" or unit == "Celcius":
  converted = round((temp * 9/5) + 32, 2)
  newunit = "F"
  print(f"The {unit} after converting is: {converted} °{newunit}")
  
elif unit == "F" or unit == "Fahrenheit" or unit == "Farenheit":
  converted = round((temp - 32) * 5/9, 2)
  newunit = "C"
  print(f"The {unit} after converting is: {converted} °{newunit}")

else: 
  print("Invalid unit")
  sys.exit()
  
