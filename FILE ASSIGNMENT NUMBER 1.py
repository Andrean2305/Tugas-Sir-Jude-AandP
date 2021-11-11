import os
os.chdir('C:/Users/Asus')
file1 = open("66684-0.txt","r") 
s = file1.read()
cc = s.lower()
dd = cc.replace(",",'')
gg = dd.replace(".",'')
hh = gg.replace("(",'')
ii = hh.replace(")",'')
def zeee(a):
    b = {}
    for c in a.split():          #Untuk menghitung banyaknya suatu kata
        b[c] = b.get(c , 0)+1
    return b

ze = zeee(ii)

baba = list(ze)

def pro(a) :
    list = []
    for i in a :
        ccc = (ze[i])
        if ccc == 1 :
         print(f"This is the hapax : {i} {ccc}")
         list.append(i)
    return list
     

aaa = [pro(baba)]
print(aaa)
#finally work sir im happy