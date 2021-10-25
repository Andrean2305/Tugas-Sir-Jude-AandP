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