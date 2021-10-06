a = eval(input("Enter the number of packages purchased: "))
b = a*99
if 10 <= a <=19 :
    c = 10
elif 20 <= a <=49 :
    c = 20
elif 50 <= a <=99 :
    c = 30
elif 100 <= a :
    c = 40
else :
    c = 0
d = c/100 * b
d_ = "{:.2f}".format(d)
x = float(d_)
z = b - x
print(f"Discount Amount @ {c}% : ${d_}")
print("Total amount: $ {:.2f}".format(z))