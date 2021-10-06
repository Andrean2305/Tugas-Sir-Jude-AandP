a = eval(input("Enter the temperature in Farenheit: "))
while a<=-58 or a>=41 :
    print("Temperature must be between -58F and 41F")
    a = eval(input("Please re-enter the temperature in Fahrenheit: "))
b = eval(input("Enter the wind speed miles per hour: "))
while b<2 :
    print("Speed must be greater than or equal to 2")
    b = eval(input("Please re-enter the wind speed miles per hour: "))
bbb = 35.74 + (0.6215 * a) - (35.75 * b**0.16) + (0.4275 * a * b**0.16)
print("The wind chill index is {:.3f}".format(bbb))