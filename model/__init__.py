import mysql.connector

def __init__():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin12",
        database="sms"
    )
    mycursor = mydb.cursor()
    return mycursor