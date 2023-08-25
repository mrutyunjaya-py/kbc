import random

questions = [["[*] Which one is the smallest ocean in the World?",
              "(A) Indian ", "(B) Pacific", "(C) Atlantic", "(D) Arctic", "d"],

             ["[*] Which country gifted the ‘Statue of Liberty’ to USA in 1886? ",
              "(A) France", "(B) Canada", "(C) Brazil", "(D) England", "a"],

             ["[*] Dead Sea is located between which two countries? ",
              "(A) Jordan and Sudan","(B) Jordan and Israel","(C) Turkey and UAE","(D) UAE and Egypt","b"],

             ["[*] In which ocean ‘Bermuda Triangle’ region is located?",
              "(A) Atlantic","(B) Indian","(C) Pacific","(D) Arctic","a"],

             ["[*] Which country is known as the ‘playground of Europe’?",
              "(A) Austria","(B) Holland","(C) Switzerland","(D) Italy","c"],

             ["[*] Total number of oceans in the World is","(A) 3","(B) 5","(C) 7","(D) 12","b"],

             ["[*] Which country is also known as the (Land of Thousand Lakes)",
             "(A) Iceland","(B) Norway","(C) Finland","(D) Switzerland","c"],

             ["[*] Which Plateau (पठार) is known as the ‘Roof of the World’?",
              "(A) Andes","(B) Himalaya","(C) Karakoram","(D) Pamir","d"],

             ["[*] The world’s longest straight road without any corners is located in",
              "(A) USA","(B) Australia","(C) Saudi Arabia","(D) China","c"],

             ["[*] Which one is the biggest island in the World? ",
              "(A) Borneo","(B) Finland","(C) Sumatra","(D) Greenland","d"]
             ]

D = [0,1,2,3,4,5,6,7,8,9]
levels = [1000, 2000,4000,8000,16000,32000,64000,128000,256000,10000000]
print("welcome ", input("Enter your name: "), " to KBC :)")

for j in range(len(levels)):

    print(f"Questions for Rs. {levels[j]}")
    random.shuffle(D)
    a =D[0]


    print(f"Your question is here: \n {questions[a][0]}")
    print(f" {questions[a][1]}         {questions[a][2]} ")
    print(f" {questions[a][3]}         {questions[a][4]} ")
    answer = str(input("enter your answer (a-d) or 0 to quit \n"))
    if (answer.lower() == questions[a][5]):
        print(f"correct answer :) You won Rs. {levels[j]}")
    elif(answer==0):
        break
    else:
        print("oops! wrong answer :)")

        if (j<4 and j>=0):
            print(f"your take money home is Rs.{levels[0]}")
        elif(j<9 and j>=4):
            print(f"your take money home is Rs.{levels[4]}")
        elif(j==9):
            print(f"your take money home is Rs.{levels[8]}")
        elif(j==10):
            print(f"your take money home is Rs.{levels[9]}")
        else:
            print("oops! wrong answer :)")
        break



