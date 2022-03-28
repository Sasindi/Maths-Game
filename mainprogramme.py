# MAIN PROGRAMME

import CUSTOMGAME.COMMON
import QUICKGAME.Qgame
import CUSTOMGAME.EASY
import CUSTOMGAME.MEDIUM
import CUSTOMGAME.HARD
import DATABASE.DATA
import mysql.connector

# PrettyTable
from prettytable import PrettyTable
x=PrettyTable()


# Check the database connection
from mysql.connector import Error

# Exception handling
try:
    conn = mysql.connector.connect(host='localhost',user='root',password='')
    if conn.is_connected():
        print("connected")
except Error as e:
    print("oops!")
    print(e)

#Open database connection with a dictionary
conDict = {'host':'localhost','user':'root','password':''}



# Prepare a cursor object using cursor() method
cursor = conn.cursor()

# Create database
cursor=conn.cursor
cursor.execute("CREATE DATABASE game")
game= mysql.connector.connect(**conDict)



# Enter to the game
while True:
    # DISPLAY GAME MENU
    print("___________________________________________________________________________________________________________")
    print("\n","                    GAME MENU")
    print("___________________________________________________________________________________________________________")
    print("1.Quick game")
    print("2.Custom game")
    print("3.Display past game details")
    print("4.Exit")
    print("\n","Enter the number you want : ",end="")
    level=int(input())
    # Quick Game
    if(level==1):
        Quickname=QUICKGAME.Qgame.Quick()
        Quicklist=QUICKGAME.Qgame.Qplay()
        Quickcorrect=QUICKGAME.Qgame.Qresult(Quicklist,Quickname)
        Quickpercentage=QUICKGAME.Qgame.Qfinal(Quickcorrect)
        
        # Execute sql querry using execute() method in quick game
        GameSQL = "INSERT INTO maths_table (Name,Correct,TotalQ,percentage) VALUES ( %s,%s,%s,%s)"
        MyGame=(Quickname,Quickcorrect,5,Quickpercentage)
        cursor.execute(GameSQL,MyGame)
        # Commit the change in quick game
        game.commit()
        print(cursor.rowcount, "Record added")
        
        
    # Custom Game
    if(level==2):
        mode=CUSTOMGAME.COMMON.modemenu()
        playerNAME=CUSTOMGAME.COMMON.details(mode)
        Qnumber=CUSTOMGAME.COMMON.quantity()
        #Easy Mode
        if(mode==1):
            Elist=CUSTOMGAME.EASY.Equestions(Qnumber)
            CUSTOMGAME.COMMON.commonresult(Qnumber,mode,playerNAME)
            CORRECT=CUSTOMGAME.EASY.Eresult(Elist,Qnumber)
            PERCENTAGE=CUSTOMGAME.COMMON.Cfinal(CORRECT,Qnumber)
        # Medium Mode
        if(mode==2):
            Mlist=CUSTOMGAME.MEDIUM.Mquestions(Qnumber)
            CUSTOMGAME.COMMON.commonresult(Qnumber,mode,playerNAME)
            CORRECT=CUSTOMGAME.MEDIUM.Mresult(Mlist,Qnumber)
            PERCENTAGE=CUSTOMGAME.COMMON.Cfinal(CORRECT,Qnumber)
        # Hard Mode
        if(mode==3):
            Hlist=CUSTOMGAME.HARD.Hquestions(Qnumber)
            CUSTOMGAME.COMMON.commonresult(Qnumber,mode,playerNAME)
            CORRECT=CUSTOMGAME.HARD.Hresult(Hlist,Qnumber)
            PERCENTAGE=CUSTOMGAME.COMMON.Cfinal(CORRECT,Qnumber)
            
        # Execute sql querry using execute() method in custom game
        GameSQL = "INSERT INTO maths_table (Name,Correct,TotalQ,percentage) VALUES ( %s,%s,%s,%s)"
        MyGame=(playerNAME,CORRECT,Qnumber,PERCENTAGE)
        cursor.execute(GameSQL,MyGame)
        # Commit the change in custom game
        game.commit()
       

        
    # Display past player details
    if(level==3):
        # Execute SQL query using execute() method
        cursor.execute("SELECT * FROM maths_table")
        # Fetch results using fetchall() method
        data = cursor.fetchall()
        for i in data:
            x.field_names = ["Name","Correct","TotalQ","percentage"]
            x.add_row(i)
        print(x)
        print("\n","Do you want to clear past player details ?(if you want to clear, type 'yes' otherwise type 'no') :",end="")
        reply=input()
        if(reply=="yes"):
            cursor.execute("DELETE * FROM maths_table")
            # Commit the change 
            game.commit()
    

    # Refuce invalid numbers
    if(level>4)or(level<=0):
        print("\n","INVALID NUMBER. PLEASE TRY AGAIN   '_' ")

        
    # Exit from the Game
    if(level==4):
        print("\n","                   END of The GAME  *_* ")
        break
    
# Disconnect from server
game.close()

    
        
    
