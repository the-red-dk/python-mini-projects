#Python compound interest calculator

while True:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("Principle cant be less than 0")
  else:
    break
  
while True:
  rate = float(input("Enter the interest rate: "))
  if rate < 0:
    print("Rate cant be less than 0")
  else:
    break 
   
while True:
  time = int(input("Enter the time in years: "))
  if time < 0:
    print("Time cant be less than 0")
  else: 
    break 
   
total = principle * (1 + rate / 100) ** time
     
# print(principle)
# print(rate)
# print(time)

print(total)