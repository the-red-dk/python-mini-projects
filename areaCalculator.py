import sys 
import math

def rect():
  length = float(input("Enter the length of the rectangle: "))
  height = float(input("Enter the height of the rectangle: "))
  print(f"The area of a rectangle is: {length * height} cm^2.")

def cuboid(): 
  length = float(input("Enter the length of the cuboid: "))
  height = float(input("Enter the height of the cuboid: "))
  width = float(input("Enter the width of the cuboid: "))
  print(f"The area of a cuboid is: {length * height * width} cm^3.")

def circle():
  radius = float(input("Enter the radius of the circle: "))
  print(f"The area of a circle is {math.pi * radius} sq units.")

def triangle():
  base = float(input("Enter the radius of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  print(f"The area of a triangle is: {(base * height) / 2} sq units.")

choice = int(input('''Enter which area to be found: 
                   1. Rectangle 
                   2. Circle 
                   3. Cuboid 
                   4. Triangle 
'''))

if choice > 4:
  sys.exit()

if choice == 1:
  rect()
elif choice == 2:
  circle()
elif choice == 3:
  cuboid()
elif choice == 4:
  triangle()
  
else:
  print("Invalid input")
  sys.exit()