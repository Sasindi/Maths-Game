# COMMON FUNCTIONS FOR CUSTOM GAME

# Function to create mode menu

def modemenu():
    "This line is to display mode menu "
    print("____________________________________________________________________________________________________________")
    print("\n","                MODE MENU")
    print("1.Easy game")
    print("2.Medium game")
    print("3.Hard game")
    print("Select a mode number :",end="")
    modenumber=int(input())
    return modenumber


# Function to enter details

def details(mode):
    "This line is to enter details"
    print("____________________________________________________________________________________________________________")
    print("\n","                  GAME PLAY")
    print("Type your name : ",end="")
    name=input()
    if(mode==1):
        modename="Easy Game"
    if(mode==2):
        modename="Medium Game"
    if(mode==3):
        modename="Hard Game"
    print("You are playing ",modename)
    return name

# Function to ask the quantity of questions required

def quantity():
    "This line is to ask the quentity of questions"
    print("How many quesions do you want? : ",end="")
    questions=int(input())
    return questions
    

# Function ta display common result

def commonresult(Qnumber,mode,playerNAME):
    "This line is to display common result"
    print("_________________________________________________________________________________________________________________")
    print("\n","                GAME RESULT")
    print("\n","Your name is ",playerNAME)
    if(mode==1):
        modename="Easy Game"
    if(mode==2):
        modename="Medium Game"
    if(mode==3):
        modename="Hard Game"
    print("You played ",modename)
    print("You answered ",Qnumber," questions")
    return


#Function to display Final score

def Cfinal(CORRECT,Qnumber):
    "This line is to display final score"
    print("\n","you answered ",CORRECT, " questions correctly")
    Cpercentage=int(CORRECT/Qnumber*100)
    print("Final score is :",Cpercentage,"%")
    return Cpercentage

