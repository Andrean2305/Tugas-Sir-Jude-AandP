import os
os.chdir('C:/Users/Asus')   #This is my directory(pls change as to yours)
from PRICELISTAH import ShopAH #Taking the class from the imported file

def listAH():
    x = []
    y = 0
    while y <= 0 :
        y = int(input("How many items will you order today? "))
        if y <= 0 :
            print("Numbers of items must be at least 1.") #Looping till inputted numbers greater then 1
    for i in range(y) :
        print(f"Item #{i+1}-")
        a = str(input("Enter food: ")) # the way for input w specific data type is a = dataType(input("Input: "))
        z = 0
        while z <= 0 :
            z = float(input("Enter amount of pounds: ")) #Taking the amount of weight of the foods
            if z <= 0 :
                print("Amount of pounds must be greater than 0.") #Will looping untill the weight is greater then 0
        item = ShopAH(a,z)
        x.append(item) #Append objects to the list
        print("")

    print ("Here's a summary of the items purchased:")
    print ("----------------------------------------")
    return x #return a list 


def ContentAH(list_of_item) :
    for i in range(len(list_of_item)):
        print (f"Item: {list_of_item[i].getNameAH()}") # to access the get name, remember to have the obejctName.method()
        print (f"Amount ordered: {list_of_item[i].getFoodweightAH()} pounds")
        print ("Price per pound: ${:.2f}".format(list_of_item[i].getPriceAH()))
        print ("Price of order : ${:.2f}".format(list_of_item[i].getTotalAH()))
        print("")

def CalculateAH(list_of_item) : #Fuction to total the cost of all the orders
    cost_item = 0
    for i in range(len(list_of_item)):
        cost_item = cost_item + list_of_item[i].getTotalAH()
    return cost_item

def mainAH():         #Call of the fuction
    aa = listAH()
    ContentAH(aa)
    cc = CalculateAH(aa)
    print(f"Total cost: ${cc}")

mainAH() #Call the main function which call 3 other functions