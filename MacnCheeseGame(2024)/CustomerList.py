from Customer import *
import random
"""
The CustomerList class takes from the Customer class to create the list of customers
the player will come across in a day 
"""
class CustomerList():
    def __init__(self):
        self.CustomerList = []
        self.closerList = []
        self.names = ["Annie","Bob","Jen","Troy","Sam","Taylor","Jeff","Lana"]
        self.closerNames = ["Thor","Anya","Yoda","Ego"]
        self.Closer = [True,False]
        self.greeting = ["Hi!", "How are you doing?", "Hi! :D","I LOVE CHEESE!","This place is cute!","HELLO!"]
        self.closerGreeting = ["Let the God of War out!\nLet me see him!","SO EXCITING","do or do not\nthere is no try","Hit me with your best shot!"]
        self.cheese = ["Cheddar","Parmesan","Gouda","Blue","Red Leligester","Mythic Cheese"]
        self.numOfToppings = [1,2,3,4,5]
        self.toppings = ["Pepper","Spring Onion","Jalepenos","Buffalo Sauce","Meatballs","Mythic Powder"]
        self.expectedTimeLow = 0
        self.expectedTimeHigh = 0
    #creates a list of customers depending on the day
    def createList(self,day):
        amountOfCustomer = 0
        amountOfCloser = 0
        #sets the amount of Customers and their potential wait times based on the day
        #the higher the day, the higher the amounts and the lower their wait times
        if (day > 0 and day <= 3):
            amountOfCustomer = 3
            self.expectedTimeLow = 250
            self.expectedTimeHigh = 350
        if(day > 3 and day <= 6):
            amountOfCustomer = 3
            amountOfCloser = 1
            self.expectedTimeLow = 200
            self.expectedTimeHigh = 350
        if(day >6 and day <= 10):
            amountOfCustomer = 4
            amountOfCloser = 1
            self.expectedTimeLow = 150
            self.expectedTimeHigh = 350
        if (day > 10 and day <= 15):
            amountOfCustomer = 4
            amountOfCloser = 2
            self.expectedTimeLow = 150
            self.expectedTimeHigh = 200
        if (day > 15 and day <= 20):
            amountOfCustomer = 5
            amountOfCloser = 3
            self.expectedTimeLow = 150
            self.expectedTimeHigh = 160
        if (day > 20):
            amountOfCustomer = 8
            amountOfCloser = 4
            self.expectedTimeLow = 100
            self.expectedTimeHigh = 150
        #makes a Customer from the Customer Class depending on the amount of customers
        for i in range(amountOfCustomer):
            randomNum1 = random.randrange(0, len(self.names))
            name = self.names[randomNum1]
            self.names.remove(self.names[randomNum1])
            greeting = self.greeting[random.randrange(0, len(self.greeting))]
            cheese = self.cheese[random.randrange(0, len(self.cheese))]
            numOfToppings = self.numOfToppings[random.randrange(1, len(self.numOfToppings))]
            toppings = []
            # randomly generates their toppings
            for i in range(numOfToppings):
                randomNumber = random.randrange(0, len(self.toppings))
                toppings.append(self.toppings[randomNumber])
                self.toppings.remove(self.toppings[randomNumber])
            newCustomer = Customer(name,False,greeting,cheese,numOfToppings,toppings)
            self.toppings = ["Pepper", "Spring Onion", "Jalepenos", "Meatballs", "Mythic Powder"]
            self.CustomerList.append(newCustomer)
        # makes a Closer using the Customer class, because Closers are more unquie, only their order is randomly generated
        for i in range(amountOfCloser):
            randomNum2 = random.randrange(0,len(self.closerNames))
            name = self.closerNames[randomNum2]
            self.closerNames.remove(name)

            greeting = self.closerGreeting[randomNum2]
            self.closerGreeting.remove(self.closerGreeting[randomNum2])
            cheese = self.cheese[random.randrange(0, len(self.cheese))]
            numOfToppings = self.numOfToppings[random.randrange(1, len(self.numOfToppings))]
            toppings = []
            #randomly generates their toppings
            for i in range(numOfToppings):
                randomNumber = random.randrange(0, len(self.toppings))
                toppings.append(self.toppings[randomNumber])
                self.toppings.remove(self.toppings[randomNumber])
            newCustomer = Customer(name, True, greeting, cheese, numOfToppings, toppings)
            self.toppings = ["Pepper", "Spring Onion", "Jalepenos", "Meatballs", "Mythic Powder"]
            self.CustomerList.append(newCustomer)
        # resets the lists since some items were deleted before
        self.names = ["Annie","Bob","Jen","Troy","Sam","Taylor","Jeff","Lana"]
        self.closerNames = ["Thor","Anya","Yoda","Ego"]
        self.closerGreeting = ["Let the God of War out!\nLet me see him!","SO EXCITING","do or do not\nthere is no try","Hit me with your best shot!"]
    #removes a person from the list
    def removePerson(self,name):
        list.remove(name);
    #clears the list
    def resetList(self):
        self.list.clear()
