import sys 
operator = input("Enter an operation to perform (+ - * / %): ")

a = float(input("Enter A: "))

b = float(input("Enter B: "))


if operator == "+":
  res = a + b
  print(f"The result is: {round(res, 3)}")

elif operator == "-":
  res = a - b 
  print(f"The result is: {round(res, 3)}")

elif operator == "*":
  res = a * b
  print(f"The result is: {round(res, 3)}")

elif operator == "/":
  res = a / b
  print(f"The result is: {round(res, 3)}")

elif operator == "%":
  res = a % b
  print(f"The result is: {round(res, 3)}")
  
else:
  print("Invalid operator")
  sys.exit()