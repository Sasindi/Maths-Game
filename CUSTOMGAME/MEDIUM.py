# MEDIUM GAME
import random
import operator

# Function to ask questions

def Mquestions(Qnumber):
    "This line is to ask uqestions"
    x=0
    List1=[]
    opr=["+","-"]
    while(x<Qnumber):
        List2=[]
        num1=random.randrange(0,51)
        List2.append(num1)
        num2=random.randrange(0,51)
        List2.append(num2)
        operator=random.choice(opr)
        List2.append(operator)
        if(operator=="+"):
            print(num1,"+",num2,":",end="")
        else:
            print(num1,"-",num2,":",end="")
        ans=int(input())
        List2.append(ans)
        x=x+1
        List1.append(List2)
    return List1

# Function to display Medium mode result

def Mresult(Mlist,Qnumber):
    "This line i to display result of Easy mode"
    x=0
    a=0
    while(x<Qnumber):
        if(Mlist[x][2]=="+"):
            print(Mlist[x][0],"+",Mlist[x][1]," = ",Mlist[x][3],end="")
            Mans=Mlist[x][0]+Mlist[x][1]
        else:
            print(Mlist[x][0],"-",Mlist[x][1]," = ",Mlist[x][3],end="")
            Mans=Mlist[x][0]-Mlist[x][1]
        print("(answer : ",Mans,")",end="")
        if(Mans==Mlist[x][3]):
            print("[correct]")
            a=a+1
        else:
            print("[incorrect]")
        x=x+1
    return a
