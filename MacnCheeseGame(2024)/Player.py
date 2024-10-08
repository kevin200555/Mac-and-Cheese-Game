#This is a class that keeps tracks of certain vairables for the player
#This includes money, name, day, and any upgrades they may have purchased
class Player():
    def __init__(self,name,day,money,hasWF,hasFB,hasEFB,hasSID,hasPC,hasMC):
        self.name = name
        self.day = day
        self.money = money
        self.hasWF = hasWF
        self.hasFB = hasFB
        self.hasEFB = hasEFB
        self.hasSID = hasSID
        self.hasPC = hasPC
        self.hasMC = hasMC
    def getName(self):
        return self.name
    def getday(self):
        return self.day
    def getmoney(self):
        return self.money
    #this function is for the save button, this compacts all the data so it can be written to a file
    """
    it looks something like:
    Player
    1
    0
    False
    False
    False
    False
    False
    False
    """
    def save(self):
        string = str(self.name) + "\n" + str(self.day) + "\n" + str(self.money) + "\n" + str(self.hasWF) + "\n" + str(self.hasFB) + "\n" + str(self.hasEFB) + "\n" + str(self.hasSID) + "\n" + str(self.hasPC) + "\n" +str(self.hasMC)
        return string

