
numpad = ((1, 2, 3), 
          (4, 5, 6), 
          (7, 8, 9), 
          ("*", 0, "#"))

for num in numpad:
  # print(num)
  for item in num:
    print(item, end= " ")
  print()