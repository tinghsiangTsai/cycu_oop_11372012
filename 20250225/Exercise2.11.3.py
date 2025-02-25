import math
radius = 5
volume = (4/3) * math.pi * radius**3
print(f"The volume of the sphere with radius {radius} cm is {volume} cubic centimeters.")

import math

# Define the value of x in degrees
x = 42

# Convert degrees to radians (because math.sin and math.cos expect radians)
radians = math.radians(x)

# Compute the sine and cosine of x
sin_x = math.sin(radians)
cos_x = math.cos(radians)

# Compute the sum of the squares of sine and cosine
sum_of_squares = sin_x**2 + cos_x**2

# Display the result
print(f"The sum of the squares of sin({x}) and cos({x}) is approximately {sum_of_squares}.")

import math

# Using math.e and the exponentiation operator (**)
result1 = math.e**2

# Using math.pow to raise math.e to the power of 2
result2 = math.pow(math.e, 2)

# Using math.exp to compute e raised to the power of 2
result3 = math.exp(2)

# Display the results
print(f"Using math.e and exponentiation: {result1}")
print(f"Using math.pow: {result2}")
print(f"Using math.exp: {result3}")
