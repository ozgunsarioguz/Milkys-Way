import random
import os
from tqdm import tqdm 
from colorama import Fore, Back, Style 
import time

#Functions, Environments:
#Beginning with CLEAR function: To clear previously written stuff during game:

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

print("In the quiz there will be 3 questions. And if you answer all correct, Vanessa will give us one of her Ribbon!")
time.sleep(3) 
print("\r\n \r\n But one more thing, you have 3 tries to guess. \r\n \r\n If you cannot give the correct answer in 3 tries, then game over!")
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
print(questions_tripple)

print(answers_tripple)
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
                print("\r\n Are you sure about the answer. Please think through and answer one more time. \r\n")
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
    Scenes.CameFromSeashore == False
    Scenes.Home_I()
else:
    print("\r\n \r\n Going to copper valley")
    time.sleep(2)

