def calc_new_height():
    a = eval(input("Enter the current width: "))
    b = eval(input("Enter the current height: "))
    c = eval(input("Enter the desired width: "))
    d = c/a*b
    print("\n")
    print(f"The corresponding height is: {d}")
    return d

z = calc_new_height()       
print(z)