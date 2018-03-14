import random as dot
import math as m

# Total number of random points.
total = 1000000
# Points contained in the circle.
inside = 0

#Main loop
for i in range(0, total):
# Place random dots in unit square
    x2 = dot.random()**2
    y2 = dot.random()**2
    # Check if inside circle,
    # increment counter if inside
    if m.sqrt(x2 + y2) < 1.0:
        inside += 1

# We're only doing positive x/y coords,
# so multiply by four.
pi = (float(inside) / total) * 4

# Print result
print(pi)
# Print difference
difference = m.fabs(pi - m.pi)
print(difference)
