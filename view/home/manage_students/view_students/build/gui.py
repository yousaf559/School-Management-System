from pathlib import Path
import tkinter
from tkinter.ttk import Treeview

import mysql.connector

# from tkinter import *
from tkinter import Frame, ttk, messagebox
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel

from view.home.manage_students.view_students.edit_student.build.gui import edit_Student_Window

from tkinter.messagebox import askyesno



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_Students_Window():
    View_Students()

class View_Students(Toplevel):

    def openEditStudent(self):
        edit_Student_Window(self, self.selected_rid)

    def __init__(self, *args, **kwargs):

        # self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)
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
            10.0,
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
            text="Students",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

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

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.edit_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_edit(),
            relief="flat",
            state="disabled",
        )
        self.edit_btn.place(
            x=254.0,
            y=462.0,
            width=116.0,
            height=48.0
        )
        button_image_5 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.delete_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.delete_student(),
            relief="flat",
            state="disabled",
        )
        self.delete_btn.place(
            x=380.0,
            y=462.0,
            width=116.0,
            height=48.0
        )


        self.columns = {
            "ID": ["ID", 5],
            "Name": ["Name", 100],
            "Address": ["Address", 150],
            "Age": ["Age", 10],
            "Class": ["Class", 50],
            "Phone": ["Phone", 100],
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

        # mydb.close()
        #
        # #self.resizable(False, False)
        self.mainloop()

    def on_treeview_select(self, event=None):
            try:
                self.treeview.selection()[0]
            except:
                self.selected_rid = None
                return
            # Get the selected item
            item = self.treeview.selection()[0]
            # Get the room id
            self.selected_rid = self.treeview.item(item, "values")[0]
            self.edit_btn.config(state="normal")
            self.delete_btn.config(state="normal")
            #print("Done")


    def insert_students_data(self):
        self.treeview.delete(*self.treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from students"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.treeview.insert("", "end", values=row)
        mydb.close()

    def handle_edit(self):
        self.openEditStudent()


    def delete_student(self):

        confirm_delete = askyesno(title='Confirmation',
                          message='Are you sure that you want to delete selected record?')
        if confirm_delete:

         mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
         )

         mycursor = mydb.cursor()
         query = "delete from students where student_id = %s"
         param_list = list()
         param_list.append(self.selected_rid)
         mycursor.execute(query, param_list)
         mydb.commit()
         if mycursor.rowcount > 0:
             messagebox.showinfo("Successful", "Student Record Deleted Successfully")
             self.handle_refresh()
         else:
             messagebox.showinfo("Error", "Unable to delete selected student")


    def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from students"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.treeview.insert("", "end", values=row)
        mydb.close()


