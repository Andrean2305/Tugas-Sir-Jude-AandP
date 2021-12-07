class ShopAH :
    def __init__(self,name,food):
        self.__name = name              #The 4 hidden attributes : The name of the food
        self.__foodweight = food  #The weight of the food
        self.__price = self.__PricelistAH()   #Remember to self.method()         #The price of the food
        self.__total = self.TotalAH()       # Remember self.method()     #Total calculated price

    def __PricelistAH(self) :   #The menu
        if self.__name == "Dry Cured Iberian Ham" :
            self.__price = 177.80
        elif self.__name == "Wagyu Steaks" :
            self.__price = 450.00
        elif self.__name == "Matsutake Mushrooms" :
            self.__price = 272.00
        elif self.__name == "Kopi Luwak Coffee" :
            self.__price = 306.50
        elif self.__name == "Moose Cheese" :
            self.__price = 487.20
        elif self.__name == "White truffles" :
            self.__price = 3600.00
        elif self.__name == "Blue Fin Tuna" :
            self.__price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes" :
            self.__price = 270.81
        else :
            self.__price = 0.00
        return self.__price #Will return 0 if the writting of the menu name is wrong

    def TotalAH(self) :
        self.__total = self.__price * self.__foodweight
        return self.__total     #The total price of the food(not all of the order)

    def getNameAH(self) :
        return self.__name  #Getter of the 4 att.

    def getFoodweightAH(self) :
        return self.__foodweight

    def getPriceAH(self) :
        return self.__price

    def getTotalAH(self) :
        return self.__total