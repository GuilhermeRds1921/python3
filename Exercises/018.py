# Create a program that reads any angle and
# displays the sine, cosine, and tangent of that angle.

import math

angle = float(input("Enter the Angle: "))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print("The Sine of this angle is {:.2f}".format(sine))
print("The Cosine of this angle is {:.2f}".format(cosine))
print("The Tangent of this angle is {:.2f}".format(tangent))
