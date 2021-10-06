a = float(input("Enter the subtotal: $ "))
b = float(input("Enter tip amount(as a%): "))
d = float(b/100*a)
e = a + d
print("Subtotal: ${:.2f}".format(a))
print("Tip: ${:.2f}".format(d))
print("Total: ${:.2f}".format(e))