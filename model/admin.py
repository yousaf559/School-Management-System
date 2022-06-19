from model.__init__ import __init__ as init_db
import mysql.connector
from tkinter import messagebox
from services.email_sending_service import EmailSendingService

class Admin():
    def __init__(self):
        self.db = init_db()

    def login(self, username, password):
        mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin12",
        database="sms"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * from admin WHERE username = '"+username+"' AND password = '"+password+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()   
        if len(result) > 0:
            #EmailSendingService.alert_admin()
            return True
        else:
            messagebox.showerror("Error!", "Incorrect Credentials, Try Again!")