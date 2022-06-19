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

        # FOR RETURNING TO DASHBOARD 
    # def backToDashboard(self):
    #     self.destroy()
    #     #homeWindow()
    #     self.home_manager.homeWindow()

    def __init__(self, record_id, table_name, *args, **kwargs):

        # self.home_manager=manager
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

        cal=Calendar(self.canvas, selectmode='day')
        cal.tag_config('present', background='green', foreground='white')
        cal.tag_config('absent', background='red', foreground='white')
        cal.place(
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

        self.canvas.create_rectangle(
            28.0,
            16.0,
            29.0,
            18.0,
            fill="#D9D9D9",
            outline="")

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
        print(self.selectedrid)
        mycursor.execute(self.query, [self.selectedrid])
        results = mycursor.fetchall()
        for result in results:
            #date=datetime.strptime(result[1],"%Y-%m-%d").date()
            cal.calevent_create(result[1], result[2], result[2])
        self.resizable(False, False)






    #     self.columns = {
    #         "ID": ["ID", 5],
    #         "Name": ["Name", 100],
    #         "Address": ["Address", 150],
    #         "Age": ["Age", 10],
    #         "Class": ["Class", 50],
    #         "Phone": ["Phone", 100],
    #     }

    #     self.treeview = Treeview(
    #         self,
    #         columns=list(self.columns.keys()),
    #         show="headings",
    #         height=200,
    #         selectmode="browse",
    #         # ="#FFFFFF",
    #         # fg="#5E95FF",
    #         # font=("Montserrat Bold", 18 * -1)
    #     )

    #     # Show the headings
    #     for idx, txt in self.columns.items():
    #         self.treeview.heading(idx, text=txt[0])
    #         # Set the column widths
    #         self.treeview.column(idx, width=txt[1])

    #     self.treeview.place(x=64.0, y=135.0, width=672.0, height=300.0)

    #    # set data in tree
    #     self.insert_students_data()
    #     # Add selection event
    #     self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

    #     # mydb.close()
    #     #
    #     # #self.resizable(False, False)
        self.mainloop()
