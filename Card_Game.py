import random
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def CardGame():


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


CardGame()
