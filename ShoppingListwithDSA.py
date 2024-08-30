#Shopping List with Python DSA

foods = []
prices = []
total = 0 

while True:
  food = input("Enter a food to buy (q to exit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter the price of {food} INR: "))
    foods.append(food)
    prices.append(price)
    
    
print("Your Cart".center(30, "-"))

for food in foods:
  print(food)
  
for price in prices:
  total += price 
  
print(f"Your Total is: {total} INR")