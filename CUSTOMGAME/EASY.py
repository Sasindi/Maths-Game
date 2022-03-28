# EASY GAME
import random

# Function to ask questions

def Equestions(Qnumber):
    "This line is to ask uqestions"
    x=0
    List1=[]
    while(x<Qnumber):
        List2=[]
        num1=random.randrange(0,11)
        List2.append(num1)
        num2=random.randrange(0,11)
        List2.append(num2)
        print(num1,"+",num2,":",end="")
        ans=int(input())
        List2.append(ans)
        x=x+1
        List1.append(List2)
    return List1

# Function to display Easy mode result

def Eresult(Elist,Qnumber):
    "This line i to display result of Easy mode"
    x=0
    a=0
    while(x<Qnumber):
        print(Elist[x][0],"+",Elist[x][1]," = ",Elist[x][2],end="")
        Eans=Elist[x][0]+Elist[x][1]
        print("(answer : ",Eans,")",end="")
        if(Eans==Elist[x][2]):
            print("[correct]")
            a=a+1
        else:
            print("[incorrect]")
        x=x+1
    return a
    
    



        
        
        
