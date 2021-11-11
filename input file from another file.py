import os

os.chdir('C:/Users/Asus')

finput = open("TESTINGSIR.txt","r")         
output = open("pro.txt","w")

count = 0
for line in finput :
    count = count+1
    output.write ("{:2d} {}".format(count,line))