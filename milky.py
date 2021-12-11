#Milk's Way. In this story based adventure game, a cat, named Milky, tries to find his beloved toy, a ribbon, out in the streets, in transportation, in many places.


#Functions, Environments:

from random import random, randint
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

class Scenes:
    ClassName = ""
    CameFromSeashore = False
    SecondVisit = False

    def ContinueLoop():
        while 1 == 1:
            print("")
            x = input("Please press Enter to continue episode in..." + Scenes.ClassName)
            print("")
            if x == "":
                print("")
                for i in tqdm (range (101),  
                    desc=Fore.YELLOW + "Loading. . .",  
                    ascii=False, ncols=75): 
                    time.sleep(0.01)             
                #the Fore.GREEN adds colour to the loading bar
                #print(Fore.YELLOW + "Next episode...") 
                #time.sleep(2) 
                #this will clear the terminal
                os.system('cls' if os.name == 'nt' else 'clear')
                break  
        


    def Seashore():
        Scenes.ClassName = "Seashore"
        if Scenes.SecondVisit == False:
            print("")
            print("***** Seashore ****")
            Scenes.ContinueLoop()

            print("")
            print("***** Seashore ****")
            print("\r\n He goes to the seashore and searches everywhere. Even under the rocks, he looked.\r\n \r\n")
            print("\r\n He asked the flower lady if she might have seen his ribbon. \r\n She answers, yes, she saw the ribbon but she would tell only under one condition.\r\n \r\n If he buys all of her flowers...\r\n \r\n")
            print("")

            time.sleep(7)

            print("")
            print("Milky, then, desperately buys all the flowers she sells, \r\n \r\nwith the last penny he owns and asks immidiately, where the ribbon is.\r\n Flower lady smiled unpleasingly and said that she tricked him into buying all the flowers \r\n \r\n and has no idea where the \"ribbon\" is. So, here our friend Milky might need our help. \r\n \r\n We have two options... \r\n \r\n ")
            time.sleep(7)

            print("1. Milky, scracthes the woman and run away to home.") 
            print("")
            print("2. Milky, scracthes the woman and go to the port nearby to take a ferry to ISLAND...") 
            print("")

            while 1 == 1:
                print("")
                x = input("Please write \"1\" to select the first option or write \"2\" to select the second and then press Enter...")
                print("")
                if x == "1":
                    print("")
                    Scenes.CameFromSeashore = True
                    cls()
                    Scenes.Home_I()
                    break

                elif x == "2":
                    print("")
                    cls()
                    Scenes.Port()
                    break
        elif Scenes.SecondVisit:
            print(" \r\n Which way should we pick now? City or the port? \r\n \r\n Write 1 for the city and 2 for the port and then please press Enter... \r\n ")

            while 1 == 1:
                x = input("\r\n \r\n Please write 1 or 2 to select the new destionation and then press Enter...")
                print("")

                if x == "1":
                    print("\r\n We are heading into Smalltown! \r\n")
                    cls()
                    Scenes.Smalltown()
                    break 
                elif x== "2":
                    print("\r\n We are heading into Port to take a ferry to the Island! \r\n")
                    cls()
                    Scenes.Island()
                    break

                
    def Port():
        Scenes.ClassName = "Port"

        Scenes.ContinueLoop()
        print("")
        print("***** Port ****")
        print("")
        print("After reaching the port, Milky searched the ways he could enter the ferry without getting caught by security guard. \r\n \r\n There seem to be 3 paths: 1. From enterance door by leaking into the crowd walking in and carefully getting into the boat. \r\n \r\n 2. Climbing to safety fences outside and then jumping into the boat. \r\n \r\n  3. Leaking from exit door when a new ferry comes and people start going out... ")
        print("")
        
        print("")
        a = random()
        b = randint(1, 3)
        b = str(b)

        while 1 == 1:
            x = input("\r\n \r\n Please write \"1\" to select the first option, write \"2\" to select the second or \"3\" \r\n \r\n for the third and then press Enter...")
            print("")

            if x == b:
                cls()
                if x == "1":
                    print("\r\n \r\n Soo we picked the option Enterance Door, ")
                elif x == "2":
                    print("\r\n \r\n Soo we picked the option Safety Fences, ")
                else:
                    print("\r\n \r\n Soo we picked the option Exit Door, \r\n \r\n ")                   
                print("\r\n \r\n Well done, my friend! Milky listened to you, and got into the boat without any problem!\r\n \r\n")
                time.sleep(5)
              
                Scenes.Island()
                break
            else:
                cls()
                if x == "1":
                    print("\r\n \r\n Soo we picked the option Enterance Door but, ")
                elif x == "2":
                    print("\r\n \r\n Soo we picked the option Safety Fences but, ")
                else:
                    print("\r\n \r\n Soo we picked the option Exit Door but, ") 

                print("\r\n \r\n well, it's bad news. Milky got caught by security guard and missed the ferry. Select again how to continue... \r\n \r\n Again like previous options, select 1, 2, or 3 and press Enter... Hopefully Milky will make it this time!")


    def Home_I():
        Scenes.ClassName = "Home"

        print("")
        print("***** At home again... ****")
        print("")
        if Scenes.CameFromSeashore == True:
            print("Milky got rest a bit at home but still so impatient, so he is going back to the Seashore... \r\n")
            Scenes.SecondVisit = True
            Scenes.ContinueLoop()
            Scenes.Seashore()

        else:
            input("\r\n Going back from Copper...\r\n Ribbon was not found. \r\n But wait... Isn't it this ribbon we have been searching for, \r\n his sister playing with iy right now!!!")
            time.sleep(2)

            while 1 == 1:
                print("Thank you for helping out Milky, he is so exhausted but so thankful to you...\r\n \r\n")
                print("")
                x = input("Please press Enter to quit. Bye.")
                print("")
                
                if x == "":
                    cls()
                    break


    def Island():
        Scenes.ClassName = "Island"
        print("")

        Scenes.ContinueLoop()

        print("***** Island ****")
        print("\r\n Our friend could make it to the island. He has been searching for the ribbon for a while. \r\n \r\n He is talking with the local people and asking for the lost ribbon...\r\n")
        time.sleep(2)
        print("\r\n During Milky's search, he came accross a stranger, who told him that \r\n there are competition games on the island, where he can get a ribbon as a prize. \r\n")
        time.sleep(2)
        print("\r\n Milky found this idea reasonable, since his Ribbon was lost, and might not be back again. But he would get a new one for free... \r\n")
        time.sleep(2)
        print("\r\n Why not...\r\n ")
        time.sleep(2)
        print("\r\n After some search, he found the competition area, \r\n \r\n ... there is also a game where he can get a ribbon as a prize. \r\n ")
        time.sleep(2)
        print("\r\n The game is basically a card game, \r\n \r\n ... Stage Owner: \"The rules are simple. We get 5 cards in the beginning. We pick one of them and compare with the opponent... The bigger number wins... \r\n ")        
        time.sleep(2)
        print("\r\n If you get more scores than i get, \r\n you get the ribbon my friend! Or else, you lose the game and walk away.\" \r\n ")
        print("")
        print("\r\n Let's help Milky to win the game! \r\n ")

        Scenes.CardGame()

        
    def CardGame():
        import random
        Scenes.ContinueLoop()

        # to generate card list
        ten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        card_list_milky = random.sample(ten_list, 5)
        card_list_owner = random.sample(ten_list, 5)
        milky_points = 0
        owner_points = 0
        rounds = 1
        

        while milky_points + owner_points < 5:
            print ("\r\n \r\n Milky's cards : " +  str(card_list_milky))
            m = input("\r\n \r\n Your cards are shown in the above list, please pick one of them to start the " + str(rounds) + ". Round... \r\n \r\n ")
            print("")
            m = int(m)
            o = random.choice(card_list_owner)
                
            
            if m not in card_list_milky:
                time.sleep(2)
                print("\r\n Card is not in your list... \r\n")
                time.sleep(2)
            else:
                card_list_owner.remove(o)
                card_list_milky.remove(m)
                time.sleep(3)
                cls()
                if m > o:
                    print("\r\n \r\n Soo, you picked the card " + str(m))
                    print("\r\n \r\n And it is bigger than opponent's card!         " + str(o) + "        Nice! ")
                    milky_points += 1
                    rounds += 1

                    print("\r\n \r\n Scoreboard: Milky:    " + str(milky_points) + "     Opponent:        " + str(owner_points))
                    time.sleep(2)
                elif m < o:
                    print("\r\n \r\n Soo, you picked the card          " + str(m))
                    print("\r\n \r\n But your card value was smaller than the opponent's card           " + str(o))
                    owner_points += 1
                    rounds += 1
                    print("\r\n \r\n Scoreboard: Milky:    " + str(milky_points) + "     Opponent:        " + str(owner_points))

                    time.sleep(2)

                elif m == o:
                    print("\r\n \r\n Soo, you picked the card          " + str(m))
                    print("\r\n \r\n But your card value was also           " + str(o))
                    print("\r\n \r\n It's a tie!")

                    print("\r\n \r\n Scoreboard: Milky:    " + str(milky_points) + "     Opponent:        " + str(owner_points))

                    time.sleep(2)            


        print("\r\n \r\n Thank you for playing the Card Game")
        time.sleep(2)
        if milky_points > owner_points:
            print("\r\n \r\n Milky got the game by the help of you!")
            time.sleep(2)
        elif milky_points < owner_points:
            print("\r\n \r\n Unfortunately Milky lost the game!")
            time.sleep(2)
        Scenes.Smalltown()


    def Smalltown():
        Scenes.ClassName = "Smalltown"
        print("")
        print("")
        Scenes.ContinueLoop()

        print("***** Smalltown City... ****")
        print("It's not here too.\r\n A friend of Milky called, he says ribbon was seen in Copper City. \r\n So he is heading there now.")

        Scenes.CopperWalley()

    def CopperWalley():
        Scenes.ClassName = "CopperWalley"
        print("")
        Scenes.ContinueLoop()
    
        print("***** Copperwalley City... ****")
        print("")

        print("It's not here too.\r\n Going back to home. Milky is so upset and tired as well. Friend will drop him to home.")

        Scenes.Seashore = False
        Scenes.Home_I()


    def HomeFinal():
        pass

#Home: Where it all begins, and it all ends...

print("")
print("***** Milky... ****")
print("")
print("One day Milky wakes up and can't find his precious ribbon at home.")
print("")
print("")

print("He looks everywhere but it was not at home at all...")
print("")
print("That ribbon was the world to him and he would not think of a life without his ribbon.")
print("")
print("He decides to go on an adventure.")
print("")

x = ""

while 1 == 1:
    print("")
    x = input("If you want to continue helping Milky while he is searching his ribbon, please write \"yes\" and press Enter... \r\n \r\n If you wish not, then please write \"no\" and press Enter...")
    print("")
    
    if x == "yes":
        cls()
        print("")
        print("***** Ribbon... ****")
        print("")
        print("So i see it is a yes!")
        print("")
        print("")
        print("Milky left home to find his ribbon. The only place in his mind was the SEASHORE.")
        print("")
        print("The ribbon might have fallen down from the window and wind would have taken it away.")
        cls()
        print("")
        print("If he is lucky enough he would might get it in the sea shore,")
        print("")
        print("Before it gets lost in the depth of the sea.")
        print("")
        cls()
        Scenes.Seashore()

        break

        
    elif x == "no":
        print("")
        print("***** Bye... ****")
        print("")
        print(" So our friend Milky will go on this adventure on his own... Bye!")
        break

