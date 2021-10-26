def num_atom(a,b=196.97):
    c = b/a
    d = 6.022e+23/c
    print(d)
    return d

z = num_atom(10)
x = num_atom(10, 12.001)
y = num_atom(10, 1.008)
print("\n")
print(z,x,y)
#if you want to input by yourself

baaaaaaz = num_atom(a = eval(input("Weight in gram: ")),b = eval(input("Atomic weight in grams/mole: ")))
zze = eval(input("Weight in gram: "))
zzee = eval(input("Atomic weight in grams/mole[Type None to get default Aurum atomic weight]: "))
if zzee == None:
    zzzz = num_atom(zze)
else:
    zzzz = num_atom(zze,zzee)