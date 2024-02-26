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
    # messagestr = ["cookLog", "recipeId", "cookDate"] IM NOT SURE HOW YOU HAVE YOUR DB SETUP BUT HOWEVER ATTRIBUTES ORDERED
    messagestr = messagestr.split()
    currentID = messagestr[1]
    currentlogDate = messagestr[2]



    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:  # AS YOU HAVE YOUR DATABASE SET UP in RECIPE REQUEST
        with conn.cursor() as cursor:
            #  RETURN ALL DATES WHEN RECIPE COOKED
            if messagestr[0] == "update_cookLog":  # (IF CORRECT PROMPT FROM DRIVER)
                cursor.execute("SELECT currentlogDate FROM [dbo].[recipes] WHERE RecipeID={}".format(messagestr))  #HOWEVER YOU HAVE YOUR DATABASE ORGANIZED...PULL OBJECT ATTRIBUTE DATES
                row = cursor.fetchone()
                while row:
                    if debug == 1:
                        print (str(row[0]) + " " + str(row[1]))
                        ##IMPORTANT!! This is only outputting columns 0 and 1!!  #YOUR WARNING                     #CYCLE THROUGH LIKE YOUR PREVIOUS IMPLEMENTATION
                    recipe_string = ""
                    for i in range (len(row)):
                        recipe_string = recipe_string +" " + str(row[i])
                    socket.send_string(recipe_string)
                    row = cursor.fetchone()
                

