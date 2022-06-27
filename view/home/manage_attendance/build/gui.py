from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter.ttk import Treeview
import mysql.connector
from view.home.manage_attendance.view_students_attendance.build.gui import view_StdAtten_Window
from view.home.manage_attendance.view_teachers_attendance.build.gui import view_TchAtten_Window


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def manage_Atten_Window(manager):
    Manage_Atten(manager = manager)

class Manage_Atten(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    def backToDashboard(self):
        self.destroy()
        #homeWindow()
        self.home_manager.homeWindow()

    def openViewStdAtten(self):
        view_StdAtten_Window(self.selected_rid, 'students')

    def openViewTchAtten(self):
        view_StdAtten_Window(self.selected_rid, 'teachers')

    def __init__(self, manager, *args, **kwargs):

        self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)

        self.title("School Management System")

        self.geometry("814x615")
        self.configure(bg="#FFFFFF")

        self.current_window = None     

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 615,
            width = 814,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            18.0,
            17.0,
            814.0,
            615.0,
            fill="#AFAEF0",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            800.0,
            600.0,
            fill="#FFF8F8",
            outline="")

        self.canvas.create_text(
            489.0,
            169.0,
            anchor="nw",
            text="Teachers",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            173.0,
            171.0,
            anchor="nw",
            text="Students",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            18.0,
            571.0,
            anchor="nw",
            text="All rights reserved.",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            28.0,
            111.0,
            anchor="nw",
            text="Here you can choose whether to Mark/Change Student or Teacher Attendance",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            228.0,
            38.0,
            anchor="nw",
            text="Manage Attendance\n",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

        # button_image_1 = PhotoImage(
        #     file=relative_to_assets("button_1.png"))
        # button_1 = Button(
        #     self.canvas,
        #     image=button_image_1,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.openViewStdAtten(),
        #     relief="flat"
        # )
        # button_1.place(
        #     x=124.0,
        #     y=450.0,
        #     width=235.0,
        #     height=60.0
        # )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.backToDashboard(),
            relief="flat"
        )
        button_2.place(
            x=550.0,
            y=530.0,
            width=235.0,
            height=60.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openViewTchAtten(),
            relief="flat"
        )
        button_3.place(
            x=467.0,
            y=450.0,
            width=235.0,
            height=60.0
        )

        # button_image_4 = PhotoImage(
        #     file=relative_to_assets("button_4.png"))
        # button_4 = Button(
        #     self.canvas,
        #     image=button_image_4,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.openViewTchAtten(),
        #     relief="flat"
        # )
        # button_4.place(
        #     x=467.0,
        #     y=256.0,
        #     width=235.0,
        #     height=60.0
        # )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openViewStdAtten(),
            relief="flat"
        )
        button_5.place(
            x=124.0,
            y=450.0,
            width=235.0,
            height=60.0
        )

        self.canvas.create_rectangle(
            397.0,
            149.0,
            399.0,
            571.0,
            fill="#000000",
            outline="")

            # STUDENT TABLE
        self.student_columns = {
            "ID": ["ID", 10],
            "Name": ["Name", 100],
        }

        self.student_treeview = Treeview(
            self,
            columns=list(self.student_columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )
            # TEACHER TABLE
        self.teacher_columns = {
            "ID": ["ID", 10],
            "Name": ["Name", 100],
        }

        self.teacher_treeview = Treeview(
            self,
            columns=list(self.teacher_columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        # Show the headings for STUDENT TABLE
        for idx, txt in self.student_columns.items():
            self.student_treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.student_treeview.column(idx, width=txt[1])

        self.student_treeview.place(x=80.0, y=220.0, width=272.0, height=200.0)

        # set data in tree FOR STUDENT TABLE
        self.insert_students_data()
        # Add selection event
        self.student_treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

        # Show the headings for TEACHER TABLE
        for idx, txt in self.teacher_columns.items():
            self.teacher_treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.teacher_treeview.column(idx, width=txt[1])

        self.teacher_treeview.place(x=500.0, y=220.0, width=272.0, height=200.0)

        # set data in tree FOR TEACHER TABLE
        self.insert_teachers_data()
        # Add selection event
        self.teacher_treeview.bind("<<TreeviewSelect>>", self.on_treeview_select_teacher)
        self.mainloop()

    def on_treeview_select(self, event=None):
            try:
                self.student_treeview.selection()[0]
            except:
                self.selected_rid = None
                return
            # Get the selected item
            self.selected_item = self.student_treeview.selection()[0]
            # Get the room id
            self.selected_rid = self.student_treeview.item(self.selected_item, "values")[0]

    def on_treeview_select_teacher(self, event=None):
            try:
                self.teacher_treeview.selection()[0]
            except:
                self.selected_rid = None
                return
            # Get the selected item
            self.selected_item = self.teacher_treeview.selection()[0]
            # Get the room id
            self.selected_rid = self.teacher_treeview.item(self.selected_item, "values")[0]

    def insert_students_data(self):
        self.student_treeview.delete(*self.student_treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * FROM students"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.student_treeview.insert("", "end", values=row)
        mydb.close()

    def insert_teachers_data(self):
        self.teacher_treeview.delete(*self.teacher_treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * FROM teachers"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.teacher_treeview.insert("", "end", values=row)
        mydb.close()
