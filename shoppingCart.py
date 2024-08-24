n = int(input("How many items?: "))
sum = 0
for i in range(n):
  item = input("What item would you like to buy? ")
  price = float(input(f"What is the cost of {item} in INR?: "))
  while True:
    try:
      quantity = int(input(f"How many units would you like to buy?: "))
      break
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
  
  
  total = price * quantity  
  sum = sum + total
  print(f"You have bought {quantity} {item}\s")
print(f"Total cost: INR {round(sum, 2)}")
  
