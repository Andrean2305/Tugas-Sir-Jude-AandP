a = eval(input("Enter the plane's take off speed in m/s: "))
b = eval(input("Enter the plane's acceleration in m/s**2: "))
c = a**2/(2*b)
g = "{:.4f}".format(c)
print(f"The minimum runway length needed for this airplane is {g} meters.")