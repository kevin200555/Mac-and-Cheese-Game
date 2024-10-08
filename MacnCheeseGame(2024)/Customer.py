"""
The Customer class stores everything about the customer
this includes their order, their name, whether or not they're a special character, and their dialogue
"""
class Customer():
    def __init__(self,name,isCloser,greeting,cheese,numOfToppings,toppingList,):
        self.name = name
        self.isCloser = isCloser
        self.greeting = greeting
        self.cheese = cheese
        self.numOfToppings = numOfToppings
        self.toppingList = toppingList
        self.waitTime = 300
        self.tipMultiplier = 1
    def getName(self):
        return self.name
    def getIsCloser(self):
        return self.isCloser
    def getIsCloser(self):
        return self.greeting
    #the string the customer says when ordering
    def getOrderText(self):
        A = "Let me get a Mac N Cheese\n"
        B = f"with {self.cheese} cheese\n"
        C = "and topped with\n"
        D = ""
        for i in range(self.numOfToppings-1):
            D = D + self.toppingList[i] + ",\n"
        D = D + "and " + self.toppingList[self.numOfToppings-1]
        return A + B + C + D
    #prints information about a customer, developer only function
    def printInformation(self):
        A = "name:" + self.name + "\n"
        B = "isCloser: " + str(self.isCloser) + "\n"
        C = "greeting: " + str(self.greeting) + "\n"
        D = "cheese: " + str(self.cheese) + "\n"
        E = "topping num: " + str(self.numOfToppings) + "\n"
        F = self.toppingList
        return  A+B+C+D+E+str(F)
    #customers tip more if they are a special customer
    def getTipMultiplier(self):
        if(self.isCloser):
            self.tipMultiplier = 3
        else:
            self.tipMultiplier = 1
        return self.tipMultiplier