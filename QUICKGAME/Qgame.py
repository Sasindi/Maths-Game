# QUICK GAME
import random

# Function to get players details

def Quick():
    "This line is to get details"
    print("___________________________________________________________________________________________________________")
    print("                            GAME PLAY")
    print("___________________________________________________________________________________________________________")
    print("Type your name : ",end="")
    Qname=input()
    print("You are playing Quick Game")
    print("You have to answer 5 questions")
    return Qname


# Function to play Game

def Qplay():
    "This line is to play game"
    x=0
    num1=0
    num2=0
    Qlist1=[]
    while(x<5):
        Qlist2=[]
        num1=random.randrange(0,11)
        Qlist2.append(num1)
        num2=random.randrange(0,11)
        Qlist2.append(num2)
        print(num1,"+",num2," :  ",end="")
        Qanswer=int(input())
        Qlist2.append(Qanswer)
        x=x+1
        Qlist1.append(Qlist2)
    return Qlist1

# Function to display result

def Qresult(Quicklist,Quickname):
    "This line is to display result"
    print("___________________________________________________________________________________________________________")
    print("                        GAME RESULT")
    print("___________________________________________________________________________________________________________")
    print("\n","Your name is ",Quickname)
    print("You played Quick Game")
    print("You answered five questions")
    x=0
    y=0
    while(x<5):
        print("\n",Quicklist[x][0],"+",Quicklist[x][1]," : ",Quicklist[x][2],end="")
        Qcorrect=Quicklist[x][0]+Quicklist[x][1]
        print("(Correct answer : ",Qcorrect,")",end="")
        if(Qcorrect==Quicklist[x][2]):
           print(" [correct]")
           y=y+1
        else:
            print(" [incorrect]")
        x=x+1
    return y

#Function to display Final score

def Qfinal(Quickcorrect):
    "This line is to display final score"
    print("\n","you answered ",Quickcorrect, " questions correctly")
    Qpercentage=int(Quickcorrect/5*100)
    print("Final score is :",Qpercentage,"%")
    return Qpercentage
    


