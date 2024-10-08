#The Mac and Cheese Class, keeps tracks of the mac and cheese that the player makes
class MC():
    def __init__(self,person,boiled,cheese,topping,location,isBeingCreated):
        #person pasta is eing sold to
        self.person = person
        #boolean, is it boiled?
        self.boiled = boiled
        #type of cheese and topping
        self.cheese = cheese
        self.toppingListSize = topping
        self.toppingNumber = 0
        #sell Value based on allathat
        self.location = location
        self.sellValue = 0
        self.drawList = []
        self.isBeingCreated = isBeingCreated
        self.rating = 100
        self.toppingList = []
        self.money = 0
    def getPerson(self):
        return self.person
    def isBoiled(self):
        return self.boiled
    def getCheese(self):
        return self.cheese
    def getTopping(self):
        return self.topping
    def getLocation(self):
        return self.location
    #calculates the value of the mac and cheese, this is based on the amount of toppings
    def calculateValue(self):
        self.sellValue = 1
        self.sellValue += (.25 * self.toppingNumber)
        return self.sellValue