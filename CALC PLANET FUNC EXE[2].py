def calc_weight_on_planet(a,b=23.1): #a = weight // b = gravity
    c = a/9.8 #c = mass
    print(f"THE WEIGHT = {a}, THE GRAVITY = {b}")
    print("Your weight in this planet = ",c * b)
    print("\n")

z = calc_weight_on_planet(120,9.8)
x = calc_weight_on_planet(120)
y = calc_weight_on_planet(120,23.1)
