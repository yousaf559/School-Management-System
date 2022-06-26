from pathlib import Path
from tkinter.ttk import Treeview
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
import mysql.connector
from model import teacher
from tkinter.messagebox import askyesno
from datetime import date
import tkinter.ttk as ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def approveStd_Fee(teacher_id):
    Approve_Std_Fee(teacher_id)

class Approve_Std_Fee(Toplevel):

    def __init__(self, teacher_id, *args, **kwargs):
        self.teacher_id = teacher_id

        # self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)

        def fixed_map(option):
            # Fix for setting text colour for Tkinter 8.6.9
            # From: https://core.tcl.tk/tk/info/509cafafae
            #
            # Returns the style map for 'option' with any styles starting with
            # ('!disabled', '!selected', ...) filtered out.

            # style.map() returns an empty list for missing options, so this
            # should be future-safe.
            return [elm for elm in style.map('Treeview', query_opt=option) if
                    elm[:2] != ('!disabled', '!selected')]

        style = ttk.Style()
        style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

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

        self.canvas.create_text(
            297.0,
            30.0,
            anchor="nw",
            text="Student Fee List",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        self.button_1.place(
            x=583.0,
            y=462.0,
            width=165.0,
            height=46.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.approve_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.approve_fee(),
            relief="flat",
            state="disabled"
        )
        self.approve_btn.place(
            x=300.0,
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

        self.columns = {
            "ID": ["ID", 10],
            "Name": ["Name", 100],
            "Address": ["Address", 250],
            "Age": ["Age", 20]
        }

        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )
        self.treeview.tag_configure("present", background="green", foreground="white")
        self.treeview.tag_configure("default", background="red", foreground="white")
        #self.treeview.tag_configure("Default", background="white", foreground="black")

        # Show the headings
        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.treeview.column(idx, width=txt[1])

        self.treeview.place(x=64.0, y=135.0, width=672.0, height=300.0)

        # set data in tree
        self.insert_students_data()
        # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)
        self.mainloop()


    def on_treeview_select(self, event=None):
            try:
                self.treeview.selection()[0]
            except:
                self.selected_rid = None
                return
            # Get the selected item
            self.selected_item = self.treeview.selection()[0]
            # Get the id
            self.selected_rid = self.treeview.item(self.selected_item, "values")[0]
            self.approve_btn.config(state="normal")

    def insert_students_data(self):
        self.treeview.delete(*self.treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()


        sql = "SELECT students.*, transactions.transaction_id FROM students LEFT JOIN transactions ON students.student_id = transactions.student_id AND YEAR(transactions.transaction_date) = YEAR(CURRENT_DATE) WHERE students.student_id IN (SELECT student_id FROM Student_Br_Teacher WHERE teacher_id=%s AND Student_Br_Teacher.class_year = YEAR(CURRENT_DATE))"
        #sql = "SELECT students.*, transactions.transaction_id FROM students LEFT JOIN transactions ON students.student_id = transactions.student_id AND YEAR(transactions.transaction_date) = YEAR(CURRENT_DATE) WHERE students.student_id IN (SELECT student_id FROM Student_Br_Teacher WHERE teacher_id=%s);"
        mycursor.execute(sql, [str(self.teacher_id)])
        result = mycursor.fetchall()
        for row in result:
            if row[5]:
                self.treeview.insert("", "end", values=row, tags=['present'])
            else:
                self.treeview.insert("", "end", values=row, tags=['default'])

        mydb.close()

    def approve_fee(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        record_present = "SELECT * FROM transactions WHERE student_id = %s AND YEAR(transaction_date) = YEAR(CURRENT_DATE)"
        mycursor.execute(record_present, [self.selected_rid])
        student_fee = mycursor.fetchall()
        if len(student_fee) == 0:
            query = "INSERT INTO transactions (transaction_date, type, amount, description, student_id) VALUES (CURRENT_DATE, 'Fee', 12500, '', %s)"
            param_list = list()
            param_list.append(self.selected_rid)
            mycursor.execute(query, param_list)
            mydb.commit()
        self.treeview.item(self.selected_item, tags=["present"])