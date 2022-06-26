from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox, OptionMenu
from itertools import chain
import mysql.connector
from tkinter.ttk import Treeview


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_Class_Window():
    Create_Class()

class Create_Class(Toplevel):

    def __init__(self, *args, **kwargs):

        self.student_ids = []
        # self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)

        self.title("School Management System")

        self.geometry("814x615")
        self.configure(bg="#FFFFFF")

        self.current_window = None     

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 614,
            width = 817,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            20.0,
            12.0,
            817.0,
            614.0,
            fill="#AFAEF0",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            600.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            110.0,
            178.0,
            anchor="nw",
            text="Name:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            232.0,
            anchor="nw",
            text="Head Teacher:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        # self.canvas.create_text(
        #     110.0,
        #     340.0,
        #     anchor="nw",
        #     text="Type:",
        #     fill="#000000",
        #     font=("Inter", 20 * -1)
        # )

        # self.canvas.create_text(
        #     110.0,
        #     281.0,
        #     anchor="nw",
        #     text="Description: ",
        #     fill="#000000",
        #     font=("Inter", 20 * -1)
        # )

        self.canvas.create_text(
            215.0,
            95.0,
            anchor="nw",
            text="Here you can create a new Class.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            260.0,
            27.0,
            anchor="nw",
            text="Create a Class",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            440.5,
            190.5,
            image=entry_image_1
        )
        self.class_name = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.class_name.place(
            x=275.0,
            y=171.0,
            width=331.0,
            height=37.0
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
            x=658.0,
            y=532.0,
            width=105.0,
            height=52.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.submission(),
            relief="flat"
        )
        button_2.place(
            x=280.0,
            y=532.0,
            width=231.0,
            height=52.0
        )
            # ADD BUTTON
        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.student_ids.append(self.treeview.item(self.treeview.selection()[0], "values")[0]),
            relief="flat"
        )
        button_3.place(
            x=320.0,
            y=466.0,
            width=60.0,
            height=25.0
        )
            # REMOVE BUTTON
        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.student_ids.remove(self.treeview.item(self.treeview.selection()[0], "values")[0]),
            relief="flat"
        )
        button_4.place(
            x=420.0,
            y=466.0,
            width=91.0,
            height=25.0
        )

        self.columns = {
            "ID": ["ID", 5],
            "Name": ["Name", 50],
            "Age": ["Age", 10],
            "Phone": ["Phone", 50],
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

        self.treeview.place(x=170.0, y=280.0, width=499.0, height=180.0)

       # set data in tree
        self.insert_students_data()
        # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

        # mydb.close()
        #
        # #self.resizable(False, False)

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT teacher_id, teacher_name, tch_email from teachers"
        mycursor.execute(sql)
        teachers = mycursor.fetchall()
        self.teachers_hash = {}
        for id, name, email in teachers:
          self.teachers_hash[id] = f'{name} / {email}'

        self.menu= StringVar()
        self.menu.set("Select Teacher")
        self.drop= OptionMenu(
            self,
            self.menu,
            command=lambda x:  self.display_selected(),
            *self.teachers_hash.values()
           )
        self.drop.place(
            x=275.0,
            y=225.0,
            width=331.0,
            height=37.0
        )
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

    def insert_students_data(self):
        self.treeview.delete(*self.treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT student_id, student_name, student_age, student_phone from students WHERE student_id NOT IN (SELECT student_id FROM Student_Br_Teacher)"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.treeview.insert("", "end", values=row)
        mydb.close()

    def display_selected(self):
        teacher_hash_values = list(self.teachers_hash.values())
        teacher_hash_keys = list(self.teachers_hash.keys())
        self.teacher_id = teacher_hash_keys[teacher_hash_values.index(self.menu.get())]

    def submission(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()
        for student_id in self.student_ids:
            sql = "INSERT INTO Student_Br_Teacher (student_id, teacher_id, class_name) VALUES (%s, %s, %s)"
            param_list = list()
            param_list.append(student_id)
            param_list.append(self.teacher_id)
            param_list.append(self.class_name.get())
            mycursor.execute(sql, param_list)
            mydb.commit()