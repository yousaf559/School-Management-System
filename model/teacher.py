from model.__init__ import __init__ as init_db
import mysql.connector
from tkinter import messagebox
from services.email_sending_service import EmailSendingService
from datetime import date

class Teacher():
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
        # fetch teacher id
        sql = "SELECT * from teachers WHERE tch_email = '"+username+"' AND tch_password = '"+password+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        # check if record exists
        record_present = "SELECT * FROM tch_attendance WHERE teacher_id = %s AND date = %s"
        #print(result)
        mycursor.execute(record_present, [str(result[0][0]), date.today()])
        teacher_attendance = mycursor.fetchall()
        if len(teacher_attendance) == 0:
            sql2 = "INSERT INTO tch_attendance (teacher_id, date, status) VALUES (%s, %s, %s)"
            param_list = list()
            param_list.append(result[0][0])
            param_list.append(date.today())
            param_list.append("present") 
            mycursor.execute(sql2, param_list)
            mydb.commit()
        if len(result) > 0:
            #EmailSendingService.alert_admin()
            return result[0][0]
        else:
            messagebox.showerror("Error!", "Incorrect Credentials, Try Again!")
            

        