# HARD GAME
import random
import operator

# Function to ask questions

def Hquestions(Qnumber):
    "This line is to ask uqestions"
    x=0
    List1=[]
    opr=["+","-","*"]
    while(x<Qnumber):
        List2=[]
        num1=random.randrange(0,101)
        List2.append(num1)
        num2=random.randrange(0,101)
        List2.append(num2)
        operator=random.choice(opr)
        List2.append(operator)
        if(operator=="+"):
            print(num1,"+",num2,":",end="")
        if(operator=="-"):
            print(num1,"-",num2,":",end="")
        if(operator=="*"):
            print(num1,"x",num2,":",end="")
        ans=int(input())
        List2.append(ans)
        x=x+1
        List1.append(List2)
    return List1

# Function to display Hard mode result

def Hresult(Hlist,Qnumber):
    "This line i to display result of Easy mode"
    x=0
    a=0
    while(x<Qnumber):
        if(Hlist[x][2]=="+"):
            print(Hlist[x][0],"+",Hlist[x][1]," = ",Hlist[x][3],end="")
            Hans=Hlist[x][0]+Hlist[x][1]
        if(Hlist[x][2]=="-"):
            print(Hlist[x][0],"-",Hlist[x][1]," = ",Hlist[x][3],end="")
            Hans=Hlist[x][0]-Hlist[x][1]
        if(Hlist[x][2]=="*"):
            print(Hlist[x][0],"x",Hlist[x][1]," = ",Hlist[x][3],end="")
            Hans=Hlist[x][0]*Hlist[x][1]
        print("(answer : ",Hans,")",end="")
        if(Hans==Hlist[x][3]):
            print("[correct]")
            a=a+1
        else:
            print("[incorrect]")
        x=x+1
    return a
