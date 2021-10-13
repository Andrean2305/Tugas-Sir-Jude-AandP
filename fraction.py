import math

a = eval(input("Enter a numerator: Value must be greater than 0: "))
while a <= 0 :
    a = eval(input("Please re-enter the numerator. Value must be greater than 0: "))
b = eval(input("Enter a denominator. Value must be greater than 0: "))
while b <= 0 :
    b = eval(input("Please re-enter the denominator. Value must be greater than 0:"))
z = a//b
c = math.gcd(a,b)
d = int(a/c)
e = int(b/c)
if a > b :
    print(f"{a}/{b} is an improper fraction")
    
elif a < b :
    print(f"{a}/{b} is a proper fraction")
    if c != 1 :
     print(f"This proper fraction can be reduced to : {d}/{e}")
    else :
        print("This proper fraction cannot be reduced any further")


if a > b and c != 1:
    print(f"This proper fraction can be reduced to : {d}/{e}")
    baba = d-(z*e)
    if e == 1 :
        print(f"The whole number is {z}")
    else:
        print(f"The mixed number is {z} and {baba}/{e}")
g = a - (b*z)
if a > b and c == 1 :
    print("This improper fraction cannot be reduced any further")
    if b == 1 :
        print(f"The whole number is {a}")
    else :
        print(f"The mixed number is {z} and {g}/{b}")