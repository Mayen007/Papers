import math

# QUESTION 2(a)
while True:
  try: 
    # prompt user radius of a circle 
    radius = float(input("Enter radius of a circle: "))
 
   # checks if the value entered is greater than 0
    if radius > 0:
      break

    else:
     print("Enter a positive radius.")

  except ValueError:
    print("Invalid input. Please enter a valid number.")


pi = 3.142

# calculates the area
area = pi * radius * radius
print("The area of the circle is: ", area)

# calculates the circumference
circumference = 2 * pi * radius

print("The circumference of the circle is: ", circumference)
