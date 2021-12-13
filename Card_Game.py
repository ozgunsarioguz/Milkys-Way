import random
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def CardGame():
    import random
    input("enter any key to continue...")
    # to generate card list
    ten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #card_list_milky = random.sample(ten_list, 5)
    #card_list_owner = random.sample(ten_list, 5)
    card_list_milky = [1, 1, 1, 1, 1]
    card_list_owner = [1, 1, 1, 1, 1]
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
        input("enter any key to continue...")
    elif milky_points < owner_points:
        print("\r\n \r\n Unfortunately Milky lost the game!")
        time.sleep(2)
        print("\r\n \r\n But stop... Our friend is very stubborn and never giving up.")
        time.sleep(2)
        print("\r\n \r\n Let's turn back to the port \r\n \r\n and find a way!")
        input("enter any key to continue...")
    else:
        print("\r\n \r\n Well it's not a common case. But it's a tie game!")
        time.sleep(2)
        print("\r\n \r\n Let's try one more time...")
        time.sleep(2)
        CardGame()

CardGame()