#Milky's Way. In this story based adventure game, a cat, named Milky, tries to find his beloved toy, a ribbon, out in the streets, in transportation, in many places.


#Modules:

import random
import os
from tqdm import tqdm
from colorama import Fore, Back, Style 
import time

#Functions, Environments:
#Beginning with CLEAR function: To clear previously written stuff during game:

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

#I packed whole Scenes (functions) in one class, Scenes, to have interactions among them. Scenes written in functions with the given Scene name.

class Scenes:
    ClassName = ""
    CameFromSeashore = False
    SecondVisit = False
    From_Island = False    

    def ContinueLoop():
        while 1 == 1:
            print("")
            input("Please press Enter to continue episode...       \r\n \r\n" + Scenes.ClassName)
            print("")
            
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

    def AskForEnter():
        while 1 == 1:
            print("")
            x = input("Please press Enter to continue episode  ")
            if x == "":
                print("")
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
            print("\r\n He goes to the seashore and searches everywhere. Even under the rocks, he looked.")
            time.sleep(2)
            print("\r\n He asked the flower lady if she might have seen his ribbon.")
            time.sleep(2)            
            print(" \r\n She answers, yes, she saw the ribbon but she would tell only under one condition.")
            time.sleep(2)
            print("\r\n \r\n If he buys all of her flowers...\r\n \r\n")
            time.sleep(2)
            print("\r\n Milky, then, desperately buys all the flowers she sells with the last penny he owns")
            time.sleep(2)
            print("\r\n and asks immidiately, where she has seen the ribbon... ")
            time.sleep(2)
            Scenes.AskForEnter()
            print("\r\n Flower lady smiled unpleasingly and said that she tricked him into buying all the flowers. ")
            time.sleep(2)
            print(" \r\n \r\n ... and has no idea where this stupid ribbon might be... ")
            time.sleep(2)
            print("\r\n \r\n ... Here we have two options: 1. Milky, scracthes the woman and runs away to home.") 
            time.sleep(2)
            print("\r\n \r\n ... 2. Milky, scracthes the woman and goes to the port nearby to take a ferry to ISLAND...") 
            time.sleep(2)

            while 1 == 1:
                print("")
                x = input("Type \"1\" or \"2\" to select one of the options above and then press Enter...")
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
                else:
                    cls()

        elif Scenes.SecondVisit:
            Scenes.ContinueLoop()
            print(" \r\n Which way should we pick now? City or the port? \r\n \r\n Write 1 for the city and 2 for the port and then please press Enter... \r\n ")

            while 1 == 1:
                x = input("\r\n \r\n Please write 1 or 2 to select the new destination and then press Enter...")
                print("")

                if x == "1":
                    print("\r\n We are heading to Smalltown! \r\n")
                    cls()
                    Scenes.Smalltown()
                    break 
                elif x== "2":
                    print("\r\n We are heading into Port to take a ferry to the Island! \r\n")
                    cls()
                    Scenes.Port()
                    break
                else:
                    cls()

                
    def Port():
        Scenes.ClassName = "Port"

        Scenes.ContinueLoop()
        print("")
        print("***** Port ****")
        print("")

        if Scenes.From_Island == False:

            print("After reaching the port, Milky searched the ways he could enter the ferry without getting caught by security guard.")
            time.sleep(2)
            print("\r\n \r\n There seem to be three reasonable paths: ")
            time.sleep(1)
            print("\r\n \r\n 1. Leaking from enterance door with the crowd walking in and carefully getting into the boat...")
            time.sleep(1)
            print("\r\n \r\n 2. Climbing to safety fences outside and then jumping into the boat... ")
            time.sleep(1)
            print("\r\n \r\n 3. Leaking from exit door when new ferry comes and people start going out...")
            time.sleep(2)            
            Scenes.AskForEnter()
            cls()
            print("")
            
            print("")
            b = random.randint(1, 3)
            b = str(b)

            while 1 == 1:
                x = input("\r\n \r\n Please select one option to help Milky... \r\n \r\n ... Press '1' for enterance door, '2' for safety fences or '3' for exit door and then press Enter...")
                print("")

                if x == b:
                    cls()
                    if x == "1":
                        print("\r\n \r\n So we picked the option Enterance Door, ")
                    elif x == "2":
                        print("\r\n \r\n So we picked the option Safety Fences, ")
                    else:
                        print("\r\n \r\n So we picked the option Exit Door, \r\n \r\n ")                   
                    print("\r\n \r\n Well done, my friend! Milky listened to you, and got into the boat!\r\n \r\n")
                    time.sleep(5)
                
                    Scenes.Island()
                    break
                else:
                    cls()
                    bad = "\r\n \r\n Well, it's bad news. Milky got caught by the security guard and missed the ferry. Select again how to continue... \r\n \r\n Please select 1, 2, or 3 and press Enter... Hopefully Milky will make it this time!"
                    if x == "1":
                        print("\r\n \r\n Soo we picked the option Enterance Door but, " + bad)

                    elif x == "2":
                        print("\r\n \r\n Soo we picked the option Safety Fences but, " + bad)
                    elif x == "3":
                        print("\r\n \r\n Soo we picked the option Exit Door but, " + bad) 
                    else:
                        cls()

        elif Scenes.From_Island == True:
            print("\r\n \r\n Milky has left the Island and turned back to the port.")
            time.sleep(2)
            print("\r\n \r\n After he reached the port, his friend Kindy called. ")
            time.sleep(2)
            print("\r\n \r\n Milky told him the things happened... ")
            time.sleep(2)
            print("\r\n \r\n Kindy got really upset about it and offered Milky to go to Smalltown City Center \r\n \r\n and find a ribbon there. ")
            time.sleep(2)                        
            print("Why not? replied Milky, let's go and find a ribbon in the town!")
            time.sleep(2)
            Scenes.AskForEnter()                      
            Scenes.Smalltown()

    def Home_I():
        Scenes.ClassName = "Home"

        print("")
        print("***** At home again ****")
        print("")
        if Scenes.CameFromSeashore == True:
            print("\r\n Milky is at home now. So pissed of about his money. \r\n \r\n")
            time.sleep(3)
            print("\r\n But he has to turn back and find the toy in anyway...  \r\n \r\n")
            time.sleep(3)
            print("\r\n He is not afraid of the lady or of anything...  \r\n \r\n")
            time.sleep(3)
            time.sleep(3)
            print("\r\n He called his buddy Kindy and asked if he can accompany him ...  \r\n \r\n")
            time.sleep(3)            
            print("\r\n so he is going back to the Seashore again... \r\n")

            Scenes.SecondVisit = True
            Scenes.Seashore()

        else:
            print("\r\n \r\n Milky is at home again... \r\n \r\n We are all tired but at least the case is solved, right?  \r\n \r\n")
            time.sleep(3)            
            print("\r\n \r\n But wait...")
            time.sleep(3)            
            print("\r\n \r\n ISN'T IT, THIS RIBBON, ON THE SOFA, WE HAVE BEEN SEARCHING FOR, \r\n \r\n ")
            time.sleep(3)            
            print("\r\n \r\n HIS SISTER PLAYING WITH IT RIGHT NOW !!!")
            time.sleep(4)
            print("\r\n \r\n THE END... ")
            time.sleep(4)
            Scenes.AskForEnter()
            cls()
            print("Thank you for helping out Milky my friend! But this thing with the ribbon, it's unbelievable isn't it?  \r\n \r\n")
            print("")
            time.sleep(3)
            print("\r\n \r\n It was nice meeting you. \r\n \r\n ")
            time.sleep(3)
            print("\r\n \r\n Come and play Milky's Way whenever you want to have fun... \r\n \r\n ")
            time.sleep(3)
            print("\r\n \r\n Remember. This game always changes and there is no strict path... \r\n \r\n ")
            time.sleep(3)
            print("\r\n \r\n Till then, take care... \r\n \r\n ")
            time.sleep(3)
            input("\r\n \r\n Please press Enter to quit. \r\n \r\n ")                                                    


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
        Scenes.AskForEnter()
        print("\r\n After some search, he found the competition area, \r\n \r\n ... there is also a game where he can get a ribbon as a prize. \r\n ")
        time.sleep(2)
        print("\r\n The game is basically a card game, \r\n \r\n ... Stage Owner: \"The rules are simple. We get 5 cards in the beginning. We pick one of them and compare with the opponent... The bigger number wins... \r\n ")        
        time.sleep(3)
        print("\r\n If you get more scores than i get, \r\n you get the ribbon my friend! Or else, you lose the game and walk away.\" \r\n ")
        time.sleep(2)

        print("")
        print("\r\n Let's help Milky to win the game! \r\n ")

        Scenes.CardGame()

        
    def CardGame():
        import random
        input("enter any key to continue...")

        # to generate card list
        ten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        card_list_milky = random.sample(ten_list, 5)
        card_list_owner = random.sample(ten_list, 5)
        milky_points = 0
        owner_points = 0
        rounds = 1

        while rounds < 6:
            print ("\r\n \r\n Milky's cards : " +  str(card_list_milky))
            m = input("\r\n \r\n Your cards are shown in the above list, please pick one of them to start the " + str(rounds) + ". Round... \r\n \r\n ")
            print("")
            m = int(m)
            o = random.choice(card_list_owner)
                
            if m not in card_list_milky:
                time.sleep(2)
                cls()
                print("\r\n Card is not in your list... \r\n")
                time.sleep(2)
            else:
                card_list_owner.remove(o)
                card_list_milky.remove(m)
                time.sleep(3)
                cls()
                if m > o:
                    print("\r\n \r\n Soo, you picked the card " + str(m))
                    print("\r\n \r\n And it is bigger than opponent's card!         " + str(o))
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
                    rounds += 1
                    print("\r\n \r\n Scoreboard: Milky:    " + str(milky_points) + "     Opponent:        " + str(owner_points))

                    time.sleep(2)            

        print("\r\n \r\n Thank you for playing the Card Game")
        time.sleep(2)
        if milky_points > owner_points:
            print("\r\n \r\n Milky won the Ribbon by the help of you!")
            time.sleep(2)
            print("\r\n \r\n He can now go back to home and enjoy his new toy \r\n \r\n  without any further troubles in the city...")
            time.sleep(2)
            Scenes.CameFromSeashore = False
            Scenes.Home_I()
        elif milky_points < owner_points:
            print("\r\n \r\n Unfortunately Milky lost the game!")
            time.sleep(2)
            print("\r\n \r\n But stop... Our friend is very stubborn and never giving up.")
            time.sleep(2)
            print("\r\n \r\n Let's turn back to the port \r\n \r\n and find a way!")
            Scenes.From_Island = True
            Scenes.Port()
        else:
            print("\r\n \r\n Well it's not a common case. But it's a tie game!")
            time.sleep(2)
            print("\r\n \r\n Let's try one more time...")
            time.sleep(2)
            Scenes.CardGame()

    def Smalltown():
        Scenes.ClassName = "Smalltown"
        Scenes.ContinueLoop()
        print("")
        print("")
        print("***** Smalltown Center ****")
        print("")
        print("")        
        print("\r\n \r\n Milky and Kindy came to town center together with Kindy's car.")
        time.sleep(2)
        print("\r\n \r\n They have been looking for a ribbon that they can play with. ")
        time.sleep(2)
        print("\r\n \r\n They saw one of their friend Vanessa in the center.")
        time.sleep(2)
        print("\r\n \r\n Milky told him that his ribbon, they played, is lost. \r\n \r\n And they are searching for a new one right now. ")
        time.sleep(3)
        print("\r\n \r\n Vanessa listened... Then she offered Milky and Kindy to give one of her ribbons")
        time.sleep(3)                        
        print("But since it's a precious ribbon of her, she wanted to give it not for a price \r\n \r\n but after a quiz she will make! ")        
        time.sleep(3)
        Scenes.AskForEnter()
        print("Why not? replied Milky. They both got excited and accepted Vanessa's quiz offer!")
        time.sleep(3)                        
        print("In the quiz there will be 3 questions. And if you answer all correct, Vanessa will give us one of her Ribbon! ")
        time.sleep(3) 
        print("\r\n \r\n But one more thing, you have 3 tries to guess. \r\n \r\n  If you cannot give the correct answer in 3 tries, then game over!")
        time.sleep(3) 


        question1 = "What is milky way?"
        question2 = "When was the first sale year of Kinder Surprise?"
        question3 = "We have a 100-meter piece of ribbon. \r\n \r\n If it takes 1 second to cut it into a 1-meter strip... \r\n \r\n How long would it take to cut the entire ribbon into 1-meter strips? -write your answer in seconds-"
        question4 = "Which of the notes is not a string note of a violin: E - G - A - B - D"
        question5 = "Who released the song 'Under The Milky Way' in 1988?"
        question6 = "We want 200 ribbons of length 130 cm for a party. However, the ribbons were sold at 25 m per tape. How many tapes will we need?"
        question7 = "By how many islands are formed 'Prince's Islands' in Istanbul?"
        question8 = "Which city on the world is shared between two continents?"
        question9 = "If Milky is 3 years old, how old is he in Human Years?"
                
        answer1 = "galaxy"
        answer2 = "1974"
        answer3 = "99"
        answer4 = "b"
        answer5 = "the church"
        answer6 = "11"
        answer7 = "9"
        answer8 = "istanbul"
        answer9 = "28"

        questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9]
        answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9]
        
        questions_tripple = []
        answers_tripple = []

        for i in range(3):
            q = random.choice(questions)
            a = answers[questions.index(q)]
            questions_tripple.append(q)
            answers_tripple.append(a)
            questions.remove(q)
            answers.remove(a)            
        
        Scenes.AskForEnter()

        print("\r\n \r\n So, first question comes... \r\n \r\n")

        time.sleep(3)                         
        lost_game = False

        for i in range(len(questions_tripple)):
            tries = 0
            if lost_game == False:
                while 1 == 1:
                    print(" ")
                    print(" ")
                    print("\r\n \r\n " + questions_tripple[i])
                    x = input("\r\n \r\n Please type your answer and then press Enter... \r\n \r\n")
                    x = x.lower()
                    cls()
                    if x == answers_tripple[i]:
                        if i != 2:
                            print("\r\n Well, it's correct! Only       " + str(2 - i) + "      more questions left to get the ribbon! \r\n")
                            time.sleep(2)                        
                            break
                        else:
                            print("\r\n Well, it's also correct! You answered all the questions correct! We won! \r\n")
                            time.sleep(2)                        
                            break                    
                    elif x != answers_tripple[i] and tries < 2:
                        tries += 1
                        left_tries = 3 - tries
                        print("\r\n Are you sure about the answer? Please think through and answer one more time. \r\n")
                        print("\r\n Guesses left:       " + str(left_tries) + " \r\n")
                        time.sleep(2) 
                    else:
                        print("\r\n \r\n Unfortunately, Milky and Kindy lost the quiz, and so a new Ribbon...")
                        time.sleep(2)
                        print("\r\n \r\n But stop... Our friend is very stubborn and never giving up.")
                        time.sleep(2)
                        print("\r\n \r\n They will go Copper Valley to have bigger chance for finding a ribbon there!")
                        time.sleep(2)

                        lost_game = True
                        break
            else:
                break            

        if lost_game == False:
            print("\r\n \r\n Thank you for playing the quiz")
            time.sleep(2)
            print("\r\n \r\n Milky and Kindy won the Ribbon by the help of you!")
            time.sleep(2)
            print("\r\n \r\n Milky can now go back to home and enjoy his new toy \r\n \r\n with their friends... Without any further troubles in the city...")
            time.sleep(2)
            Scenes.AskForEnter()
            Scenes.CameFromSeashore = False
            Scenes.Home_I()
        else:
            Scenes.CopperValley()

    def CopperValley():
        Scenes.ClassName = "CopperValley"
        print("")
        Scenes.ContinueLoop()
    
        print("***** Copper Valley City ****")
        print("")
        print("")        
        print("\r\n \r\n Milky and Kindy came to Copper Valley town center.")
        time.sleep(3)
        print("\r\n \r\n Milky was so tired. He lost his ambition to find a new ribbon toy.")
        time.sleep(3)
        print("\r\n \r\n He thought that he can and he has to live without a ribbon toy!")
        time.sleep(3)
        print("\r\n \r\n He could be acting more mature since he is not a kitten anymore!")
        time.sleep(3)
        print("\r\n \r\n He turned to Kindy and thanked for all his support until now...")
        time.sleep(3)                       
        print("He was also a bit sorry that he took him in this unreasonable rush too.")
        time.sleep(3)                       
        print("'Oh, buddy, not a big deal. It was our best toy. It was no problem for me at all'.")
        time.sleep(3)                       
        print("'Yes, but, i agree. Today it's late and better we go home and maybe do it next time!' replied Kindy.")
        time.sleep(3)                       
        print("So our friend Milky headed back to home, in Small Town by Kindy's car...")
        Scenes.CameFromSeashore = False
        Scenes.Home_I()
        Scenes.ContinueLoop()

    def HomeFinal():
        pass

#Home: Where it all begins, and it all ends...

print("")
print("***** Milky... ****")
print("")
print("One day Milky wakes up and can't find his precious ribbon at home.")
print("")
print("")
time.sleep(3)                       

print("He looks everywhere but it was not at home at all...")
print("")
time.sleep(2)                       
print("That ribbon was the world to him and he would not think of a life without his ribbon.")
print("")
time.sleep(2)                       
print("He decides to go on an adventure.")
print("")
time.sleep(2)                       

x = ""

while 1 == 1:
    print("")
    x = input("If you want to continue helping Milky while he is searching his ribbon, please write \"y\" and press Enter... \r\n \r\n If you wish not, then please write \"n\" and press Enter...   \r\n \r\n")
    time.sleep(2)
    print("Well...")
    time.sleep(2)

    
    if x == "y":
        cls()
        print("")
        print("***** Ribbon ****")
        print("")
        print("... i see it is a yes!")
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

        
    elif x == "n":
        print("")
        print("***** Bye... ****")
        print("")
        print("... So our friend Milky will go on this adventure on his own... Bye!")
        break
    else:
        cls()

