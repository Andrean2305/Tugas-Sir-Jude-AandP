import math
a = eval(input("Enter the mass of the cart(in kg): "))
b = eval(input("Enter the force to push the cart(in N): "))
g = 9.8
c = b/a/g
z = math.asin(c)
d = math.degrees(z)
print ("The angle of the ramp is {:.1f} degrees".format(d))