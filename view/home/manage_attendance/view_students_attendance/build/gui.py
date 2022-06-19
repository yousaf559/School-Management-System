from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import mysql.connector
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from datetime import datetime 


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_StdAtten_Window(record_id, table_name):
    View_StdAtten(record_id, table_name)

class View_StdAtten(Toplevel):

    def __init__(self, record_id, table_name, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)
        self.selectedrid = record_id
        self.table_name = table_name
        
        self.title("School Management System")

        self.geometry("810x562")
        self.configure(bg="#FFFFFF")

        self.current_window = None     



        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 562,
            width = 809,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            10.0,
            17.0,
            810.0,
            562.0,
            fill="#AFAEF0",
            outline="")

        self.cal=Calendar(self.canvas, selectmode='day')
        self.cal.tag_config('present', background='green', foreground='white')
        self.cal.tag_config('absent', background='red', foreground='white')
        self.cal.place(
            x=100.0,
            y=100.0,
            width=600.0,
            height=350.0
        )


        self.canvas.create_rectangle(
            0.0,
            0.0,
            797.0,
            549.0,
            fill="#FFFDFD",
            outline="")

        self.canvas.create_text(
            11.0,
            521.0,
            anchor="nw",
            text="All rights reserved ",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
        if self.table_name == 'teachers':
            self.heading = "Teacher Attendance"
        else:
            self.heading = "Student Attendance"

        self.canvas.create_text(
            215.0,
            33.0,
            anchor="nw",
            text=self.heading,
            fill="#000000",
            font=("Inter", 36 * -1)
        )
            #BACK BUTTON
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_1.place(
            x=583.0,
            y=462.0,
            width=165.0,
            height=46.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.present_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mark_attendance('present'),
            relief="flat"
        )
        self.present_btn.place(
            x=254.0,
            y=462.0,
            width=116.0,
            height=48.0
        )
        button_image_5 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.absent_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mark_attendance('absent'),
            relief="flat"
        )
        self.absent_btn.place(
            x=380.0,
            y=462.0,
            width=116.0,
            height=48.0
        )

        self.canvas.create_rectangle(
            28.0,
            16.0,
            29.0,
            18.0,
            fill="#D9D9D9",
            outline="")

        self.add_color()
        self.resizable(False, False)
        self.mainloop()

    def add_color(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin12",
        database="sms"
        )
         
        mycursor = mydb.cursor()
        if self.table_name == 'teachers':
            self.query = "SELECT * FROM tch_attendance WHERE teacher_id = %s"
        else:
            self.query = "SELECT * FROM std_attendance WHERE student_id = %s"
        mycursor.execute(self.query, [self.selectedrid])
        results = mycursor.fetchall()
        for result in results:
            #date=datetime.strptime(result[1],"%Y-%m-%d").date()
            self.cal.calevent_create(result[1], result[2], result[2])

    def mark_attendance(self, attendance):
        if self.table_name == "teachers":
            self.db_table_name = "tch_attendance"
            self.id_column_name = "teacher_id"
        else:
            self.db_table_name = "std_attendance"
            self.id_column_name = "student_id"

        mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin12",
        database="sms"
        )
         
        mycursor = mydb.cursor()
    
        record_present = "SELECT * FROM "+self.db_table_name+" WHERE "+self.id_column_name+" = %s AND date = %s"
        mycursor.execute(record_present, [self.selectedrid, datetime.strptime(self.cal.get_date(),"%m/%d/%y")])
        student_attendance = mycursor.fetchall()
        if len(student_attendance) > 0:
            sql2 = "UPDATE "+self.db_table_name+" SET status = %s WHERE "+self.id_column_name+" = %s AND date = %s"
            param_list = list()
            param_list.append(attendance)
            param_list.append(self.selectedrid)
            param_list.append(datetime.strptime(self.cal.get_date(),"%m/%d/%y"))
            mycursor.execute(sql2, param_list)
            mydb.commit()
        else:
            query = "INSERT INTO "+self.db_table_name+" ("+self.id_column_name+", date, status) VALUES (%s, %s, %s)"
            param_list = list()
            param_list.append(self.selectedrid)
            param_list.append(datetime.strptime(self.cal.get_date(),"%m/%d/%y"))
            param_list.append(attendance)
            mycursor.execute(query, param_list)
            mydb.commit()
        self.add_color()