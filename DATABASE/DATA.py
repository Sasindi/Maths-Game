import mysql.connector

#Function to Open database connection with a dictionary

def open():
    "This line is to open database connection" 
    conDict = {'host':'localhost','database':'game','user':'root','password':''}
    game= mysql.connector.connect(**conDict)
    # Prepare a cursor object using cursor() method
    cursor = game.cursor()
    return 

#Function to execute sql querry using execute() method

def execute(playerNAME,CORRECT,Qnumber,PERCENTAGE):
    "This line is to execute sql querry"
    GameSQL = "INSERT INTO maths_table (Name,Correct,TotalQ,percentage) VALUES ( %s,%s,%s,%s)"
    MyGame=(playerNAME,CORRECT,Qnumber,PERCENTAGE)
    cursor.execute(GameSQL,MyGame)
    # Commit the change
    game.commit()
    return
