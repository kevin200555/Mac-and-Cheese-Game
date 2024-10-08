import random
#MacNCheeseGame.py
#A game where you make Mac and Cheese for Customers
#make money and use them to buy upgrades
#Date      Name     Notes
#8/14/2024 Kevin Li End Date(subject to change)
#8/05/2024 Kevin Li Start Date
"""
List of py files (6):
button.py, Customer.py, CustomerList.py, MacNCheeseGame.py, MCclass.py, Player.py

*All Sprites are PNGs*
List of Background Sprites (10):
Gamestate1, Gamestate2, Gamestate3, Gamestate4, Gamestate5, Gamestate6,
Gamestate7, Gamestate8, help Background, shop Background:

List of Cat Sprites (15):
Annie, Anya, baseCat, Bob, Ego, Jeff, Jen, Lana, MCcat, PetCat, Sam, Taylor, Thor, Troy, Yoda

List of Cheese Sprites (6):
BlueCheese, Cheddar, Gouda, MythicCheese, Parmesan, RedLeligester

List of Other Sprites (5):
BoilingPot, BoilingPotGold, BoilingPotRed, CookedPasta, RawPasta

List of Toppings Sprites (6):
"""


from graphics import *
from button import Button
from MCclass import MC
from time import *
from Customer import *
from CustomerList import *
from Player import Player

#activates all buttons in a list of buttons
def activateList(buttonList):
    try:
        for i in buttonList:
            i.activate()
    except:
        pass
#calculates the rating of a certain mac and cheese order
def calculateRating(customer,macNCheese,timer,expectedTime):
    rating = 100
    #minus 50 if player gets cheese wrong
    if(customer.cheese != macNCheese.cheese):
        rating -= 50
    ListA = customer.toppingList
    ListB = macNCheese.toppingList
    ListA.sort()
    ListB.sort()
    # minus 50 if player gets the toppings wrong
    if (ListA != ListB):
        rating -= 50
    # minus a certain amount if player takes too long
    if ( timer > expectedTime):
        rating = rating - ((timer - expectedTime)/5)
    #sets the rating to zero if it ever becomes negative
    if (rating < 0):
        rating = 0
    #returns the rounded rating
    return round(rating)
#function for if the players pressed one of the six buttons in gamestate 5
def cheeseButtonFunction(win,order,png,nameOf,deactList):
    #adds the name of the cheese to the mac and cheese class
    order.cheese = nameOf
    #deactivates the all of the six buttons
    deactivateList(deactList)
    #adds cheese to the list of items the game has to draw
    order.drawList.insert(0,png)
    png.draw(win)
#this function compacts the creation of all of the sprites relating to mac and cheese
#this includes the pasta, cheese, and toppings
#I could do something similar for every button and object in main(), but I feel it is a choice of main
#being clogged or my functions being clogged.
#I think having main() being clogged is a tad more organized
def createMacNCheeseSprites(otherPath,cheesePath,toppingPath):
    rawPasta = Image(Point(400,150),otherPath + "RawPasta.png")
    cookedPasta = Image(Point(400,150),otherPath + "CookedPasta.png")
    boilingPot = Image(Point(400,150),otherPath + "BoilingPot.png")
    #Cheese sprites
    cheddar = Image(Point(400,150),cheesePath + "Cheddar.png")
    parmesan = Image(Point(400,150),cheesePath + "Parmesan.png")
    gouda = Image(Point(400,150),cheesePath + "Gouda.png")
    blue = Image(Point(400,150),cheesePath + "BlueCheese.png")
    redLeligester = Image(Point(400,150),cheesePath + "RedLeligester.png")
    mythicCheese = Image(Point(400,150),cheesePath + "MythicCheese.png")
    #Topping sprites
    pepper = Image(Point(400,150),toppingPath + "Pepper.png")
    springOnion = Image(Point(400,150),toppingPath + "SpringOnion.png")
    buffaloSauce = Image(Point(400,150),toppingPath + "BuffaloSauce.png")
    jalepenos = Image(Point(400,150),toppingPath + "Jalepenos.png")
    meatballs = Image(Point(400,150),toppingPath + "Meatballs.png")
    mythicPowder = Image(Point(400,150),toppingPath + "MythicPowder.png")
    return rawPasta,cookedPasta,boilingPot,cheddar,parmesan,gouda,blue,redLeligester,mythicCheese,pepper,springOnion,buffaloSauce,jalepenos,meatballs,mythicPowder
#the text that the customers will say when judging your order, changes based on the order rating
def customerJudgement(rating):
    if (rating > 90):
        return "SO PURFECT!!!!"
    elif (rating > 70):
        return "mmmmm nice"
    elif(rating > 40):
        return "hmmmmmm"
    elif (rating > 20):
        return "bad :("
    else:
        return "*sad meow*"
#deactivates a list of buttons
def deactivateList(buttonList):
    try:
        for i in buttonList:
            i.deactivate()
    except:
        pass
#draws a list of graphic class stuff (and buttons)
def drawList(win,itemList):
    try:
        for i in itemList:
            i.draw(win)
    except:
        pass
#draws the UI for the load menu, also returns mutable objects in this menu
def drawLoadFile(loadMenu):
    statusText = Text(Point(150,20),"Enter name of file and press Enter: ")
    loadEntry = Entry(Point(150,45),25)
    enterButton = Button(loadMenu,Point(150,75),175,25,"Enter")
    exitButton = Button(loadMenu,Point(285,185),30,25,"quit")
    str = "List of File Names: "
    fileText = Text(Point(150, 142), str)
    exitButton.activate()
    enterButton.activate()
    for i in os.listdir("Files"):
        str += "\n"+i
    str = str.replace(".txt","")
    fileText.setText(str)
    loadEntry.draw(loadMenu)
    statusText.draw(loadMenu)
    fileText.draw(loadMenu)
    return statusText,loadEntry,enterButton,exitButton
#draws the UI for the save menu, also returns mutable objects in this menu
def drawSaveFile(saveMenu):
    statusText = Text(Point(150, 40), "Enter the name of a file\npress new to save a new file\npress delete to delete an \nalrady existing one: ")
    saveEntry = Entry(Point(150, 100), 25)
    newButton = Button(saveMenu, Point(100, 125), 50, 25, "New")
    deleteButton = Button(saveMenu, Point(200, 125), 50, 25, "Delete")
    exitButton = Button(saveMenu, Point(285, 290), 30, 25, "quit")
    str = "List of File Names: "
    fileText = Text(Point(150, 200), str)
    exitButton.activate()
    newButton.activate()
    deleteButton.activate()
    for i in os.listdir("Files"):
        str += "\n" + i
    str = str.replace(".txt", "")
    fileText.setText(str)
    saveEntry.draw(saveMenu)
    statusText.draw(saveMenu)
    fileText.draw(saveMenu)
    return statusText, saveEntry, newButton, deleteButton, exitButton, fileText
#draws the UI for the shop menu, also returns mutable objects in this menu
def drawShop(shopMenu):
    shopBackground = Image(Point(200,300),"Backgrounds//shop background.png")
    shopBackground.draw(shopMenu)
    exitButton = Button(shopMenu,Point(375,575),50,25,"quit")
    walkFasterButton = Button(shopMenu,Point(200,400),175,25,"Walk Faster!!!! - $15")
    fasterBoilButton = Button(shopMenu, Point(200, 425), 175, 25, "Faster Boil - $30")
    evenFasterBoilButton = Button(shopMenu, Point(200, 450), 175, 25, "Even Faster Boil - $100")
    slowItDownButton = Button(shopMenu, Point(200, 475), 175, 25, "Slow it Down - $500")
    petCatButton = Button(shopMenu, Point(200, 500), 175, 25, "Assistant Cat - $1000")
    michelinChefButton =  Button(shopMenu, Point(200, 525), 175, 25, "Michelin Star - $2000")
    shopButtonList = [walkFasterButton,fasterBoilButton,evenFasterBoilButton,slowItDownButton,
                      petCatButton,michelinChefButton]
    moneyDisplay = Text(Point(200,565),"Your Money: $")
    moneyDisplay.setSize(15)
    moneyDisplay.draw(shopMenu)
    exitButton.activate()
    activateList(shopButtonList)
    return exitButton,walkFasterButton, fasterBoilButton, evenFasterBoilButton, slowItDownButton, petCatButton, michelinChefButton, shopButtonList,moneyDisplay

#finds the tip Multiplier based on the rating, closer status, and day number
def findTipMultiplier(rating,isCloser,day,tipUpgrades):
    tipMultiplier = 1
    if(isCloser):
        tipMultiplier += 1
    tipMultiplier *= (rating * 0.02)
    tipMultiplier *= ( 1 + (day * .1))
    return tipMultiplier * tipUpgrades
#This is for gamestate 7, this returns a list of booleans used in ratingDetailsText()
#these booleans are whether the player got the correct cheese, correct toppings, and if they hit the timing requirement
def ratingDetailsBoolean(customer,macNCheese,timer,expectedTime):
    correctCheese = True
    correctToppings = True
    correcttimer = True
    if (customer.cheese != macNCheese.cheese):
        correctCheese = False
    ListA = customer.toppingList
    ListB = macNCheese.toppingList
    ListA.sort()
    ListB.sort()
    if (ListA != ListB):
        correctToppings = False
    if (timer > expectedTime):
        correcttimer = False
    return correctCheese,correctToppings,correcttimer
#This is for gamestate 7, this creates the string that gives the player more info on what they did
#right and what they did wrong
def ratingDetailsText(correctCheese,correctToppings,timer):
    cheeseText = "Correct Cheese\n"
    toppingsText = "Correct Toppings\n"
    timeText = "Fast Service\n"
    if(not correctCheese):
        cheeseText = "Incorrect Cheese\n"
    if(not correctToppings):
        toppingsText = "Incorrect Toppings\n"
    if(not timer):
        timeText = "Slow Service\n"
    return cheeseText + toppingsText + timeText
#undraws a background and draws a new one
def setBackground(win,oldBackgrounds,newBackground):
    undrawList(oldBackgrounds)
    try:
        newBackground.draw(win)
    except:
        pass
#function for if the players pressed one of the six buttons in gamestate 6
#same as cheeseButtonFunction(), but presses one of the buttons disables only that button, and not all of the six buttons
#this lets the user add more toppings
def toppingButtonFunction(win,order,png,nameOf,button):
    order.topping = nameOf
    order.drawList.append(png)
    order.toppingNumber += 1
    button.deactivate()
    order.toppingList.insert(0,nameOf)
    png.draw(win)
#undraws a list of graphics class objects (and buttons)
def undrawList(itemList):
    for i in itemList:
        i.undraw()
#main method
def main():
    #create game window
    win = GraphWin("Mac and Cheese Game", 800, 600)
    #Title Text
    welcomeText = Text(Point(400,100),"Mac N Cheese")
    welcomeText.setSize(35)
    #paths to the location of sprites in the folders
    catPath = "Cat\\"
    cheesePath = "Cheese\\"
    toppingPath = "Toppings\\"
    backgroundPath ="Backgrounds\\"
    otherPath = "Other\\"
    #background
    gamestate1Back = Image(Point(400,300),backgroundPath + "Gamestate1.png")
    gamestate2Back = Image(Point(400, 300), backgroundPath + "Gamestate2.png")
    gamestate3Back = Image(Point(400, 300), backgroundPath + "Gamestate3.png")
    gamestate4Back = Image(Point(400, 300), backgroundPath + "Gamestate4.png")
    gamestate5Back = Image(Point(400, 300), backgroundPath + "Gamestate5.png")
    gamestate6Back = Image(Point(400, 300), backgroundPath + "Gamestate6.png")
    gamestate7Back = Image(Point(400, 300), backgroundPath + "Gamestate7.png")
    gamestate8Back = Image(Point(400, 300), backgroundPath + "Gamestate8.png")
    gamestate1Back.draw(win)
    backgrounds = [gamestate1Back,gamestate2Back,gamestate3Back,gamestate4Back,
                   gamestate5Back,gamestate6Back,gamestate7Back,gamestate8Back,]
    #universal stuff
    quitButton = Button(win,Point(775,590),50,25,"Quit")
    quitButton.activate()
    helpButton = Button(win,Point(775,565),50,25,"?")
    helpButton.activate()
    playerText = Text(Point(725,30),"Player")
    playerText.draw(win)
    playerDay = Text(Point(725,50),"Day 1")
    playerDay.draw(win)
    playerMoney = Text(Point(725,70),"$00.00")
    playerMoney.draw(win)
    #creates all sprites relating to mac and cheese
    rawPasta, cookedPasta, boilingPot, cheddar, parmesan, gouda, blue, redLeligester, mythicCheese,pepper, springOnion, buffaloSauce, jalepenos, meatballs, mythicPowder = createMacNCheeseSprites(otherPath, cheesePath, toppingPath)
    #Player sprites
    you = Image(Point(615,255),catPath+"baseCat.png")
    petCat = Rectangle(Point(0,0),Point(0,0))
    #Customer sprites and Other customer related things
    customer = Image(Point(0,300),catPath+"Anya.png")
    customerText = Text(Point(0,150),"Hiiii! :D")
    customerText.setSize(20)
    #gamestate 1 stuff, gamestate 1 is the home menu, this is where the player can load and create save files
    playButton = Button(win,Point(400,300),100,100,"Play")
    playButton.activate()
    loadButton = Button(win,Point(25,590),50,25,"Load")
    loadButton.activate()
    saveButton = Button(win, Point(25, 565), 50, 25, "Save")
    saveButton.activate()
    #gamestate 2 stuff, gamestate 2 is the precursor to the game, it just tells the player their
    #current progress before letting them play.  Also is where the shop menu is
    startDayButton = Button(win,Point(400,300),100,100,"Start Day")
    dayText = Text(Point(400,100),"Day 1")
    dayText.setSize(35)
    storeButton = Button(win, Point(400,500),100,100,"Store")
    backToMenuButton = Button(win,Point(25,590),50,25,"Back")
    #station buttons, These buttons are in most gamestates, they allow the player to go to different
    #gamestates
    orderButton = Button(win,Point(175,550),100,50,"Order")
    boilerButton = Button(win, Point(325, 550), 100, 50, "Boiler")
    cheeseButton = Button(win, Point(475,550),100,50,"Cheese")
    toppingButton = Button(win, Point(625, 550), 100, 50, "Toppings")
    #These buttons are on the right side of the screen during gameplay
    #They let the player send orders to the next station and delete orders if they mess up
    sendtoNextButton = Button(win, Point(750, 300), 100, 50, "send to\nnext station")
    deleteOrderButton = Button(win, Point(750,250),100,50,"delete order")
    #gamestate 3 stuff, gamestate 3 has mulitple components, these components are 3A and 3B,
    #gamestate 3 is the player waiting for the customer to appear and the period after the customer has ordered
    #gamesetate 3A is the customer's animation of walking to the "cash register"
    #gamestate 3B is where the option appears for the player to take and read the customer's order
    takeOrderButton = Button(win,Point(475,200),50,50,"take\norder")
    orderText = Text(Point(475,100,),"")
    #gamestate 4 stuff, this gamestate also has multiple components, 4A and 4B
    #4A is after the player boils the pasta and has to wait for it to boil before doing anything else
    #4B is the period after the player sends the pasta to the next station
    makeOrderButton = Button(win,Point(400,400),100,50,"make pasta")
    boiler1Button = Button(win,Point(400,300),100,50,"boil")
    #gamestate 5 and 6 stuff, these gamestates are where the player adds the cheese and toppings, respectivly
    #the cheese and toppings appear on the screen in real time
    Button1 = Button(win,Point(300,350),100,50,"")
    Button2 = Button(win, Point(400, 350), 100, 50, "")
    Button3 = Button(win, Point(500, 350), 100, 50, "")
    Button4 = Button(win, Point(300, 400), 100, 50, "")
    Button5 = Button(win, Point(400, 400), 100, 50, "")
    Button6 = Button(win, Point(500, 400), 100, 50, "")
    #gamestate 7 stuff, this is where the customer judges how well the player performed in creating the mac and cheese
    howYouDidTitle = Text(Point(100,100),"How you did: ")
    howYouDid = Text(Point(100,175),"")
    ratingTitle = Text(Point(100,200),"Rating: ")
    ratingText = Text(Point(100,250),"100")
    ratingText.setSize(30)
    backButton = Button(win,Point(400,450,),100,100,"Back")
    tipsTitle = Text(Point(200,350),"Tips: ")
    tipsAmount = Text(Point(200,400),"")
    tipsTitle.setSize(20)
    #gamestate 8 stuff, this is the period when the day is over and no more customers are left to serve
    #the total amount of money earned is shown on screen and many variables are reset for the next day
    goodbye = Text(Point(400,100),"End of Day 1")
    totalTips = Text(Point(400,200),"Total Tips:")
    goodbye.setSize(35)
    totalTips.setSize(20)
    #This is a bar that shows the player on screen how long they have to serve the customer before
    #they start losing rating points
    timeBarGreen = Rectangle(Point(0,0),Point(200,50))
    timeBarRed = Rectangle(Point(0, 0), Point(200, 50))
    timeBarGreen.setFill("green")
    timeBarRed.setFill("red")
    #These are list, but only for buttons, these are used with functions deactivateList() and activateList()
    #because different gamestates let different buttons be pressed
    sixButtons = [Button1,Button2,Button3,Button4,Button5,Button6]
    stationButtons = [orderButton,boilerButton,cheeseButton,toppingButton]
    boilButtons = [boiler1Button,makeOrderButton]
    rightSideButtons = [deleteOrderButton,sendtoNextButton]
    everyButton = [startDayButton,storeButton,orderButton,boilerButton,cheeseButton,
                   toppingButton,sendtoNextButton,deleteOrderButton,takeOrderButton,
                   makeOrderButton,boiler1Button,Button1,Button2,Button3,Button4,Button5,Button6,
                   backButton]
    #List of gamestates and their items, these are used with drawList() and undrawList() in order
    #to change gamestates
    allDraws = [welcomeText,quitButton,helpButton,playerText,playerDay,playerMoney,
                rawPasta,cookedPasta,boilingPot,
                cheddar,parmesan,gouda,blue,redLeligester,mythicCheese,
                pepper,springOnion,buffaloSauce,jalepenos,meatballs,mythicPowder,
                customer,customerText,playButton,loadButton,startDayButton,storeButton,
                dayText,orderButton,boilerButton,cheeseButton,toppingButton,
                sendtoNextButton,deleteOrderButton,takeOrderButton,orderText,makeOrderButton,
                boiler1Button,Button1,Button2,Button3,Button4,Button5,Button6,howYouDidTitle,
                howYouDid,ratingTitle,ratingText,backButton,tipsTitle,tipsAmount,
                goodbye,totalTips,saveButton,backToMenuButton]
    universal = [helpButton,quitButton,playerText,playerDay,playerMoney]
    gamestate1 = [playButton,loadButton,quitButton,helpButton,welcomeText,saveButton] + universal
    gamestate2 = [startDayButton,storeButton,dayText,backToMenuButton] + universal

    gamestate3 = [orderButton,boilerButton,cheeseButton,toppingButton] + universal
    gamestate4 = [makeOrderButton,boiler1Button,sendtoNextButton,deleteOrderButton] + universal
    gamestate7 = [orderButton,boilerButton,cheeseButton,toppingButton,customerText,
                  howYouDidTitle,howYouDid,ratingTitle,
                  ratingText,backButton,tipsTitle,tipsAmount] + universal
    gamestate8 = [goodbye,backButton,totalTips]

    #these are list only for the cheese and topping sprites
    cheeseList = [cheddar,parmesan,gouda,blue,redLeligester,mythicCheese]
    toppingList = [pepper,springOnion,buffaloSauce,jalepenos,meatballs,mythicPowder]

    #startUp Functions (This is needed to disable and undraw all buttons as they are drawn by default)
    undrawList(everyButton)
    # tick speed
    tick = 0.05
    #time that the player needs to get under in order to satisfy the customer fully
    expectedTime = 0
    extraTime = 0
    #variables that control certain speeds on animations
    walkTick = 0.25
    boilspeed = 5
    customerSpeed = 40
    # various timers for different animations and such
    boilTimer = 0
    catMovingTimer = 0
    orderRatingTimer = 0
    #Other game variables
    fileName = "Autosave"
    gamestate = "1"
    tipUpgrades = 1
    totalDistance = 0 #used for the timer bar
    totalDayTips = 0 #used for gamestate 8
    #booleans that act as flag variables as this is stuff that should only be one once
    startOfDayStuffDone = False
    isEverythingDrawn = False
    customerPresent = False
    #game class objects
    newOrder = MC("", False, "", 0, "", False)
    newCustomer = Customer("NPC", False, "HI!", "Parmesan", 3, ["Meatballs"])
    newCustomerList = CustomerList()
    newPlayer = Player(fileName,1,0,False,False,False,False,False,False)

    #the main game loop
    while(True):
        #when the gamplay part starts, this creates the list of customers that will appear
        #and sets the correct player information on screen
        #it will also check to see if the player already has some upgrades, and give the player those upgrades
        if (startOfDayStuffDone == False and gamestate == "3"):
            newCustomerList.createList(newPlayer.day)
            playerText.setText(newPlayer.name)
            dayText.setText("Day " + str(newPlayer.day))
            playerDay.setText("Day " + str(newPlayer.day))
            playerMoney.setText("$" + str(round(newPlayer.money,2)))
            #makes customers walk faster
            if (newPlayer.hasWF):
                customerSpeed = 160
            #changes the boiling pot to red, and makes pasta boil faster
            if (newPlayer.hasFB):
                boilingPot.undraw()
                boilingPot = Image(Point(400, 150), otherPath + "BoilingPotRed.png")
                boilspeed = 10
                # changes the boiling pot to gold, makes pasta boil faster, and gives x2 tips
            if (newPlayer.hasEFB):
                boilingPot.undraw()
                boilingPot = Image(Point(400, 150), otherPath + "BoilingPotGold.png")
                boilspeed = 40
                if tipUpgrades < 2:
                    tipUpgrades = 2
            # changes the timebar to blue, gives player more time to make pasta, and gives x3 tips
            if (newPlayer.hasSID):
                extraTime = 200
                timeBarGreen.setFill("blue")
                if tipUpgrades < 3:
                    tipUpgrades = 3
            # adds a pet cat, gives x5 tips
            if (newPlayer.hasPC):
                petCat = Image(Point(750, 235), catPath + "PetCat.png")
                if tipUpgrades < 5:
                    tipUpgrades = 5
            #gives player spirte a hat, gives x10 tips
            if (newPlayer.hasMC):
                you = Image(Point(615, 255), catPath + "MCcat.png")
                tipUpgrades = 10
            startOfDayStuffDone = True
        #this allows customers to walk in only if gamestate is 3, and there are customers in the list
        if (len(newCustomerList.CustomerList) != 0 and gamestate == "3"):
            newCustomer = newCustomerList.CustomerList[0]
            newCustomerList.CustomerList.remove(newCustomer)
            expectedTime = extraTime + random.randrange(newCustomerList.expectedTimeLow,newCustomerList.expectedTimeHigh)
            customer = Image(Point(0, 300), catPath + newCustomer.name +".png")
            gamestate = "3A"
            customerText.setText(newCustomer.greeting)
            customer.draw(win)
            customerText.draw(win)
            you.draw(win)
            petCat.draw(win)
            customerPresent = True
        #This controls the orderRatingTimer for the customer, and shows it onscreen too on the timerBars
        if ((gamestate == "3B" or gamestate == "4" or gamestate == "4A" or gamestate == "4B" or gamestate == "5" or gamestate == "6")):
            sleep(tick)
            timeBarGreen.move(-(200/expectedTime),0)
            totalDistance += (200/expectedTime)
            orderRatingTimer += 1
        #check for a mouse click
        pClick = win.checkMouse()
        #big loop for a lot of buttons
        #one day, I will learn a more efficient way to do this
        #if there is a mouse click
        if pClick is not None:
            #close window if quit button pressed
            if (quitButton.clicked(pClick)):
                #saves information to the file name the player is playing on
                #saves to autosave file if no file name is given
                try:
                    newFile = open(f"Files\\{fileName}.txt", "w")
                    newFile.write(newPlayer.save())
                except:
                    pass
                win.close()
            #brings up a help menu that explains how the game works
            if (helpButton.clicked(pClick)):
                helpMenu = GraphWin("Help Menu",600,600)
                helpBackground = Image(Point(300,300),backgroundPath+"help Background.png")
                exitButton = Button(helpMenu, Point(570, 570), 30, 30,"exit")
                helpBackground.draw(helpMenu)
                exitButton.activate()
                #check for click
                while (True):
                    hClick = helpMenu.checkMouse()
                    if hClick is not None:
                        #exits help menu if exit button clicked
                        if(exitButton.clicked(hClick)):
                            helpMenu.close()
                            break
            #go to gamestate 2 if play button pressed
            elif(playButton.clicked(pClick)):
                isEverythingDrawn = False
                gamestate = "2"
            #brings up the load menu, a seperate game menu
            elif(loadButton.clicked(pClick)):
                loadMenu = GraphWin("Load File",300,200)
                statusText,loadEntry,enterButton,exitButton = drawLoadFile(loadMenu)
                while(True):
                    lClick = loadMenu.checkMouse()
                    if lClick is not None:
                        #closes load menu
                        if exitButton.clicked(lClick):
                            loadMenu.close()
                            break
                        #if player entered a name in the entry box, the information on the file will be loaded
                        #and the player can continue to play on their previous saved file
                        # this menu will be closed shortly after pressing this button too
                        if enterButton.clicked(lClick):
                            while(True):
                                fileName = loadEntry.getText()
                                info = []
                                try:
                                    file = open(f"Files\\{fileName}.txt", "r")
                                    for line in file:
                                        line.replace("\n", "")
                                        info.append(line.replace("\n", ""))
                                    newPlayer = Player(info[0], int(info[1]),float(info[2]),bool(info[3]),bool(info[4])
                                                    ,bool(info[5]),bool(info[6]),bool(info[7]),bool(info[8]))
                                    statusText.setText("File sucessfully loaded")
                                    sleep(2)
                                    loadMenu.close()
                                    break
                                except:
                                    statusText.setText("File not found")
                                    sleep(1)
                                    loadMenu.close()
                                    break
                            break
            # brings up the save menu, the buttons save and load are exclusive to the homescreen btw
            elif(saveButton.clicked(pClick)):
                saveMenu = GraphWin("Load File", 300, 300)
                statusText, saveEntry, newButton, deleteButton, exitButton, fileText = drawSaveFile(saveMenu)
                while(True):
                    aClick = saveMenu.checkMouse()
                    #closes save Menu
                    if aClick is not None:
                        if(exitButton.clicked(aClick)):
                            saveMenu.close()
                            break
                        #if new button is clicked, a new file will be created of that name taken from the entry box
                        #this new file will be empty (gameplay wise)
                        # this menu will be closed shortly after pressing this button too
                        if(newButton.clicked(aClick) and len(os.listdir("Files")) < 5):
                            try:
                                fileName = saveEntry.getText()
                                newPlayer.name = saveEntry.getText()
                                newFile = open(f"Files\\{fileName}.txt", "w")
                                newFile.write(newPlayer.name + "\n1\n0\nFalse\nFalse\nFalse\nFalse\nFalse\nFalse")
                                newPlayer = Player(newPlayer.name,1,0,False,False,False,False,False,False)
                                statusText.setText("File successfully saved")
                                sleep(2)
                                saveMenu.close()
                                break
                            # if that file doesn't exist, the game will let the player know
                            except:
                                statusText.setText("Enter a Valid File Name")
                                sleep(1)
                                saveMenu.close()
                                break
                        #if the player already has 5 saved files, they will be unable to make a new one
                        else:
                            statusText.setText("Too many Files! Can't make a new one")
                        #if this button is pressed, the file name will be taken from the entry box and that
                        #file will be deleted.
                        #this menu will be closed shortly after pressing this button too
                        if(deleteButton.clicked(aClick)):
                            try:
                                fileName = saveEntry.getText()
                                os.remove(f"Files\\{fileName}.txt")
                                statusText.setText("File deleted saved")
                                sleep(2)
                                saveMenu.close()
                                break
                            #if that file doesn't exist, the game will let the player know
                            except:
                                statusText.setText(f"File {fileName} not found")
                                sleep(1)
                                saveMenu.close()
                                break
            #go to gamestate 3 if start button pressed
            elif(startDayButton.clicked(pClick)):
                startOfDayStuffDone = False
                isEverythingDrawn = False
                gamestate = "3"
            #takes player back to gamestate1
            elif (backToMenuButton.clicked(pClick)):
                isEverythingDrawn = False
                gamestate = "1"
            #brings up the store menu
            elif (storeButton.clicked((pClick))):
                shopMenu = GraphWin("Shop!",400,600)
                quitButton, walkFasterButton, fasterBoilButton, evenFasterBoilButton, slowItDownButton, petCatButton, michelinChefButton, shopButtonList,moneyDisplay = drawShop(shopMenu)
                #for these if statements, these check if the player has previous upgrades, and disables the corresponding buttons,
                #stopping the player from buying things twice
                if(newPlayer.hasWF):
                    walkFasterButton.deactivate()
                if(newPlayer.hasFB):
                    fasterBoilButton.deactivate()
                if(newPlayer.hasEFB):
                    fasterBoilButton.deactivate()
                    evenFasterBoilButton.deactivate()
                if(newPlayer.hasSID):
                    slowItDownButton.deactivate()
                if(newPlayer.hasPC):
                    petCatButton.deactivate()
                if(newPlayer.hasMC):
                    michelinChefButton.deactivate()

                while True:
                    sClick = shopMenu.checkMouse()
                    moneyDisplay.setText("Your Money: $" + str(round(newPlayer.money)))
                    if sClick is not None:
                        #closes the shop menu, updates the playerMoney text
                        if quitButton.clicked(sClick):
                            shopMenu.close()
                            playerMoney.setText("$" + str(round(newPlayer.money, 2)))
                            break
                        #I already explained what each shop upgrade does previously, but I'll add here
                        #that purchasing an upgrade will disable the button for that upgrade
                        #I also made it so that if a player buys the gold boiling pot, they can't buy the red one
                        #this way, they won't downgrade
                        elif walkFasterButton.clicked(sClick) and newPlayer.money >= 15:
                            walkFasterButton.deactivate()
                            customerSpeed = 160
                            newPlayer.hasWF = True
                            newPlayer.money -= 15
                        elif fasterBoilButton.clicked(sClick) and newPlayer.money >= 30:
                            fasterBoilButton.deactivate()
                            boilingPot.undraw()
                            boilingPot = Image(Point(400,150),otherPath + "BoilingPotRed.png")
                            boilspeed = 10
                            newPlayer.hasFB = True
                            newPlayer.money -= 30
                        elif evenFasterBoilButton.clicked(sClick) and newPlayer.money >= 100:
                            fasterBoilButton.deactivate()
                            evenFasterBoilButton.deactivate()
                            boilingPot.undraw()
                            boilingPot = Image(Point(400, 150), otherPath + "BoilingPotGold.png")
                            boilspeed = 40
                            if tipUpgrades < 2:
                                tipUpgrades = 2
                            newPlayer.hasEFB = True
                            newPlayer.money -= 100
                        elif slowItDownButton.clicked(sClick) and newPlayer.money >= 500:
                            slowItDownButton.deactivate()
                            timeBarGreen.setFill("blue")
                            extraTime = 200
                            if tipUpgrades < 3:
                                tipUpgrades = 3
                            newPlayer.hasSID = True
                            newPlayer.money -= 500
                        elif petCatButton.clicked(sClick) and newPlayer.money >= 1000:
                            petCatButton.deactivate()
                            petCat = Image(Point(750,235),catPath+"PetCat.png")
                            if tipUpgrades < 5:
                                tipUpgrades = 5
                            newPlayer.hasPC = True
                            newPlayer.money -= 1000
                        elif michelinChefButton.clicked(sClick) and newPlayer.money >= 2000:
                            tipUpgrades = 10
                            michelinChefButton.deactivate()
                            you = Image(Point(615,255),catPath+"MCcat.png")
                            newPlayer.hasMC = True
                            newPlayer.money -= 2000


            #this button doesn't really have purpose and is more for visuals
            elif(orderButton.clicked(pClick)):
                isEverythingDrawn = False
                gamestate = "3"
            #Customer speaks order after this button pressed
            elif(takeOrderButton.clicked(pClick)):
                takeOrderButton.undraw()
                customerText.draw(win)
                customerText.setSize(10)
                customerText.setText(newCustomer.getOrderText())
                boilerButton.activate()
            #go to gamestate 4 if boil button pressed
            elif(boilerButton.clicked(pClick)):
                isEverythingDrawn = False
                gamestate = "4"
            #this button deletes the order and sends the player back to gamestate 4
            elif(deleteOrderButton.clicked(pClick) and newOrder.isBeingCreated):
                undrawList(allDraws)
                undrawList(toppingList)
                undrawList(cheeseList)
                drawList(win,gamestate4)
                gamestate = "4"
                boilTimer = 0
                isEverythingDrawn = False
                newOrder = MC("", False, "", 0, "", False)
            #go to gamestate 5 if cheese button pressed
            elif(cheeseButton.clicked(pClick)):
                isEverythingDrawn = False
                gamestate = "5"
            #go to gamestate 6 if topping button pressed
            elif(toppingButton.clicked(pClick)):
                isEverythingDrawn = False
                gamestate = "6"
            #gamestate 4 button, this creates the raw pasta
            elif(makeOrderButton.clicked(pClick)):
                newOrder = MC("NPC",False,"None",6,"4",True)
                rawPasta.draw(win)
                makeOrderButton.deactivate()
            # gamestate 4 button, this creates boils the raw pasta and gamestate becoms 4A
            elif (boiler1Button.clicked(pClick) and newOrder.isBeingCreated == True):
                gamestate = "4A"
            #add cheese station buttons, calls cheeseButtonFunction()
            elif (Button1.clicked(pClick) and gamestate == "5" and newOrder.location == "5"):
                cheeseButtonFunction(win, newOrder, cheddar, "Cheddar", sixButtons)
            elif (Button2.clicked(pClick) and gamestate == "5" and newOrder.location == "5"):
                cheeseButtonFunction(win,newOrder,parmesan,"Parmesan",sixButtons)
            elif (Button3.clicked(pClick) and gamestate == "5" and newOrder.location == "5"):
                cheeseButtonFunction(win, newOrder, gouda, "Gouda", sixButtons)
            elif (Button4.clicked(pClick) and gamestate == "5" and newOrder.location == "5"):
                cheeseButtonFunction(win, newOrder, blue, "Blue", sixButtons)
            elif (Button5.clicked(pClick) and gamestate == "5" and newOrder.location == "5"):
                cheeseButtonFunction(win, newOrder, redLeligester, "Red Leligester", sixButtons)
            elif (Button6.clicked(pClick) and gamestate == "5" and newOrder.location == "5"):
                cheeseButtonFunction(win, newOrder, mythicCheese, "Mythic Cheese", sixButtons)
            #add toppings station button, calls toppingButtonFunction()
            elif (Button1.clicked(pClick) and gamestate == "6" and newOrder.location == "6"):
                toppingButtonFunction(win, newOrder, pepper, "Pepper", Button1)
            elif (Button2.clicked(pClick) and gamestate == "6" and newOrder.location == "6"):
                toppingButtonFunction(win, newOrder, springOnion, "Spring Onion", Button2)
            elif (Button3.clicked(pClick) and gamestate == "6" and newOrder.location == "6"):
                toppingButtonFunction(win, newOrder, buffaloSauce, "Buffalo Sauce", Button3)
            elif (Button4.clicked(pClick) and gamestate == "6" and newOrder.location == "6"):
                toppingButtonFunction(win, newOrder, jalepenos, "Jalepenos", Button4)
            elif (Button5.clicked(pClick) and gamestate == "6" and newOrder.location == "6"):
                toppingButtonFunction(win, newOrder, meatballs, "Meatballs", Button5)
            elif (Button6.clicked(pClick) and gamestate == "6" and newOrder.location == "6"):
                toppingButtonFunction(win, newOrder, mythicPowder, "Mythic Powder", Button6)
            #send to next button, sends order to next station, but doesn't move the player's location
            elif (sendtoNextButton.clicked(pClick) and newOrder.location == "4B" and gamestate == "4B"):
                cookedPasta.undraw()
                newOrder.location = "5"
                cheeseButton.activate()
            elif (sendtoNextButton.clicked(pClick) and newOrder.location == "5" and gamestate == "5"):
                cookedPasta.undraw()
                undrawList(cheeseList)
                toppingButton.activate()
                newOrder.location = "6"
            #sends player to gamestate 7 from gamestate 6 for the pasta to be rated
            elif (sendtoNextButton.clicked(pClick) and newOrder.location == "6" and gamestate == "6"):
                gamestate = "7"
                isEverythingDrawn = False
            #back button that takes player from gamestate 8 to 2, lets the player stat a new day
            elif (backButton.clicked(pClick) and gamestate == "8"):
                gamestate = "2"
                isEverythingDrawn = False
            #back button that takes the player from gamestate 7 to 8 to show them their results of that day
            #only for if there are no more customers to serve
            elif (backButton.clicked(pClick) and len(newCustomerList.CustomerList) == 0):
                gamestate = "8"
                customer.undraw()
                customer.move(-400, -50)
                customerText.move(-400, -150)
                timeBarGreen.move(totalDistance, 0)
                customerText.setSize(20)
                customerPresent = False
                isEverythingDrawn = False
                boilTimer = 0
                catMovingTimer = 0
                orderRatingTimer = 0
                totalDayTips = 0
                totalDistance = 0
                newOrder = MC("", False, "", 0, "", False)
                newCustomer = Customer("", False, "HI!", "", 0, [])
            #button that takes the player from gamestate 7 to 3, lets them serve another customer
            #resets a bunch of variables and locations of objects
            elif(backButton.clicked(pClick)):
                gamestate = "3"
                customer.undraw()
                customer.move(-400, -50)
                customerText.move(-400, -150)
                timeBarGreen.move(totalDistance, 0)
                customerText.setSize(20)
                customerPresent = False
                isEverythingDrawn = False
                totalDistance = 0
                boilTimer = 0
                catMovingTimer = 0
                orderRatingTimer = 0
                totalDayTips = 0
                newOrder = MC("", False, "", 0, "", False)
                newCustomer = Customer("", False, "HI!", "", 0, [])

        #check and update objects according to gamestate
        #again, I'll get better at this I hope
        if (gamestate == "1" and isEverythingDrawn == False):
            setBackground(win,backgrounds,gamestate1Back)
            undrawList(allDraws)
            drawList(win,gamestate1)
            isEverythingDrawn = True
        #sets the player information to the correct information and draws everything in gamestate 2
        if (gamestate == "2" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate2Back)
            undrawList(allDraws)
            drawList(win,universal)
            playerText.setText(newPlayer.name)
            dayText.setText("Day " + str(newPlayer.day))
            playerDay.setText("Day " + str(newPlayer.day))
            playerMoney.setText("$" + str(round(newPlayer.money,2)))
            drawList(win,gamestate2)
            isEverythingDrawn = True
        #Draws everything in gamestate 3
        elif(gamestate == "3" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate3Back)
            undrawList(allDraws)
            drawList(win,gamestate3)
            sendtoNextButton.label.setText("send to\nnext station")
            deactivateList(stationButtons)
            isEverythingDrawn = True
        #Draws the customer and makes them walk up towards the register
        elif(gamestate == "3A"):
            #default speed, dx = 20, catMovingTimer += 1
            customer.move(customerSpeed,0)
            customerText.move(customerSpeed,0)
            sleep(walkTick)
            catMovingTimer += (customerSpeed/20)
            #stops the customer from walking too far
            if (catMovingTimer == 24):
                gamestate = "3B"
                catMovingTimer = 0
            isEverythingDrawn = False
        #This is where the orderRatingTimer starts, the customer gives there order, and the gameplay starts
        elif(gamestate == "3B" and isEverythingDrawn == False):
            takeOrderButton.draw(win)
            customerText.undraw()
            timeBarRed.draw(win)
            timeBarGreen.draw(win)
            isEverythingDrawn = True
        #draws everything in gamestate 4 and disables buttons
        elif (gamestate == "4" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate4Back)
            undrawList(allDraws)
            you.undraw()
            customer.undraw()
            petCat.undraw()
            drawList(win,gamestate4 + stationButtons)
            deactivateList(stationButtons)
            isEverythingDrawn = True
        #puts the player into (basically) a cutscene where they have to wait for the pasta to boil
        elif (gamestate == "4A"):
            deactivateList(stationButtons + boilButtons + rightSideButtons)
            try:
                rawPasta.undraw()
                boilingPot.draw(win)
            except:
                pass
            sleep(tick)
            boilTimer += boilspeed
            #controls how long the pasta boils before it becomes cooked
            if (boilTimer >= 150):
                activateList(rightSideButtons)
                boilingPot.undraw()
                gamestate = "4B"
                newOrder.location = "4B"
                cookedPasta.draw(win)
                newOrder.boiled == True
                newOrder.drawList.append(cookedPasta)
                activateList(stationButtons)
                deactivateList(boilButtons)
        #activates the cheese button to let the player go to gamestate 5 after they've sent the cooked pasta to the boil station
        elif (gamestate == "4B" and newOrder.location == "5"):
            cheeseButton.activate()
        #stops the player from going to Other stations if they haen't sent their pasta their
        elif (gamestate == "4B"):
            deactivateList(stationButtons)
        #draws everything in gamestate 5, changes labels of text, de/activate buttons
        elif (gamestate == "5" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate5Back)
            undrawList(allDraws)
            playerText.draw(win)
            playerDay.draw(win)
            playerMoney.draw(win)
            drawList(win, stationButtons + sixButtons + rightSideButtons)
            deactivateList(stationButtons)
            Button1.label.setText("Cheddar")
            Button2.label.setText("Parmesan")
            Button3.label.setText("Gouda")
            Button4.label.setText("Blue")
            Button5.label.setText("Red\nLeligester")
            Button6.label.setText("Mythic\nCheese")
            isEverythingDrawn = True
        # draws everything in gamestate 6, which is pretty much the same as gamestate 5
        # but certain buttons hae different text
        elif (gamestate == "6" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate6Back)
            undrawList(allDraws)
            playerText.draw(win)
            playerDay.draw(win)
            playerMoney.draw(win)
            drawList(win, stationButtons + sixButtons + rightSideButtons)
            deactivateList(stationButtons)
            Button1.label.setText("Pepper")
            Button2.label.setText("Spring Onion")
            Button3.label.setText("Buffalo Sauce")
            Button4.label.setText("Jalepenos")
            Button5.label.setText("Meatballs")
            Button6.label.setText("Mythic\nPowder")
            sendtoNextButton.label.setText("finish")
            isEverythingDrawn = True
        # draws everything in gamestate 7
        # resets the postions of the customer back to how it was in gamestate 3
        elif (gamestate == "7" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate7Back)
            undrawList(allDraws)
            drawList(win,gamestate7)
            drawList(win,newOrder.drawList)
            timeBarGreen.undraw()
            timeBarRed.undraw()
            customer.draw(win)
            customer.move(-80, 50)
            customerText.move(-80, 150)
            rating = calculateRating(newCustomer,newOrder,orderRatingTimer,expectedTime)
            newPlayer.money += (newOrder.calculateValue() * findTipMultiplier(rating,newCustomer.isCloser,newPlayer.day,tipUpgrades))
            totalDayTips += (newOrder.calculateValue() * findTipMultiplier(rating,newCustomer.isCloser,newPlayer.day,tipUpgrades))
            tipsAmount.setText(round((newOrder.calculateValue()*findTipMultiplier(rating,newCustomer.isCloser,newPlayer.day,tipUpgrades)),2) )
            playerMoney.setText("$" + str(round(newPlayer.money,2)))
            tempCheese, tempTopping, tempTime = ratingDetailsBoolean(newCustomer, newOrder, orderRatingTimer, expectedTime)
            howYouDid.setText(ratingDetailsText(tempCheese,tempTopping,tempTime))
            customerText.setText(customerJudgement(calculateRating(newCustomer,newOrder,orderRatingTimer,expectedTime)))
            ratingText.setText(int(rating))
            deactivateList(stationButtons)
            isEverythingDrawn = True
        #draws everything in gamestate 8
        #updates day counter and shows the player progress
        elif (gamestate == "8" and isEverythingDrawn == False):
            setBackground(win, backgrounds, gamestate8Back)
            undrawList(allDraws)
            goodbye.setText("End of Day " + str(newPlayer.day))
            totalTips.setText("Total Tips:\n" + str(round(totalDayTips,2)))
            totalDayTips = 0
            newPlayer.day += 1
            drawList(win,gamestate8)
            isEverythingDrawn = True
        #draws the mac and cheese (cheese and toppings included) only if the user and the pasta are in the
        #same location
        #mainly for consistancy since the sendToNextButton messes that up a bit
        if (newOrder.location == gamestate and len(newOrder.drawList) != 0):
            #makes sure that the mac and cheese is drawing in the correct order
            #ex: if the toppings are drawn before the cheese, the player wo't be able to see the toppings
            if(newOrder.drawList[len(newOrder.drawList)-1] == cookedPasta):
                newOrder.drawList.reverse()
                drawList(win,newOrder.drawList)
            else:
                drawList(win,newOrder.drawList)
#calls main
main()