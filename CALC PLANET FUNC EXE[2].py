def calc_weight_on_planet(a,b=23.1): #a = weight // b = gravity
    c = a/9.8 #c = mass
    print(f"Your weight on earth = {a}, The gravity of the planet = {b}")
    print("Your weight in other planet = ",c * b)
    print("\n")

z = calc_weight_on_planet(120,9.8)
x = calc_weight_on_planet(120)
y = calc_weight_on_planet(120,23.1)
#If you want to input with your number
zze = eval(input("Your weight: "))
zzee = eval(input("The planet gravity(Type None to get default 23.1 m/s^2 gravity): "))
if zzee == None:
    zzzz = calc_weight_on_planet(zze)
else:
    zzzz = calc_weight_on_planet(zze,zzee)
    #and then zzzzzzz = calc_weight_on_planet(zze,zzee)
#or
zeeeeee = calc_weight_on_planet(a=eval(input("Your weight: ")),b=eval(input("The planet gravity: ")))