import pyodbc
import zmq
from datetime import date #  THIS WILL PULL CURRENT DATE
#  MY COMMENTS WILL BE IN ALL CAPS - JACQUELINE



server = 'aidan361.database.windows.net'
database = '361RecipeDB'
username = 'azureuser'
password = 'aidan361SQL'
driver= '{ODBC Driver 18 for SQL Server}'
debug = 1

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    message = socket.recv()
    messagestr = str(message)
    if debug == 1:
        print("received message: %s" % messagestr)
    

    #clean up input  I DO NOT KNOW IF I NEED THIS STRING CLEANUP
    messagestr = messagestr[2:-1]
    if debug == 1:
        print("input selector is: %s" % messagestr)


    #split string to get relevant informations
    # messagestr = ["cookLog", "recipeId", "cookDate"] IM NOT SURE HOW YOU HAVE YOUR DB SETUP BUT HOWEVER ATTRIBUTES ORDERED THIS IS EXAMPLE
    messagestr = messagestr.split()
    currentID = messagestr[1]
    currentlogDate = messagestr[2]



    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:  # AS YOU HAVE YOUR DATABASE SET UP
        with conn.cursor() as cursor:
            #log when a recipe is cooked
            if messagestr[0] == "cookLog" :    # command from YOUR driver (IF CORRECT PROMPT FROM DRIVER)
                current_object = cursor.execute("SELECT * FROM [dbo].[recipes] WHERE RecipeID= {currentID}")  # HOWEVER YOU HAVE YOUR DATABASE ORGANIZED...PULL OBJECT
                today = date.today()
                "INSERT INTO 'current_object'(currentLogDate) VALUES(today)"          # INSERT VALUE INTO OBJECT AS YOUR DATABASE IS ORGANIZED AND CURSON MOVEMENTS
                
                #if successful:
                    # message = confirmation
                    
                #else:
                    # message = error
                    
                # socket.send_string(message)