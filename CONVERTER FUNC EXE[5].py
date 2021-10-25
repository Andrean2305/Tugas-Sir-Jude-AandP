def convert_temp():
    a = eval(input("Enter a temperature in Fahrenheit: "))
    b,ze = celcius(a)
    print(f"The temperature in Fahrenheit is: {a}")
    print(f"The temperature in Celcius is: {b}")
    print(f"The temperature in Kelvin is: {ze}")
    
def celcius(x):
    c = 5/9*(x-32)
    g = kelvin(c)
    return c,g
def kelvin(y):
    cc = y + 273.15
    return cc

convert_temp()