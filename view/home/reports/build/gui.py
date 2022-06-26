from pathlib import Path
from tkinter import CENTER, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter.ttk import Treeview
from tkinter import filedialog
from view.home.reports.sugggestions.build.gui import suggestions_Window
import pandas as pd
import mysql.connector



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def reports_Window(manager):
    Reports(manager = manager)

class Reports(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    def backToDashboard(self):
        self.destroy()
        #homeWindow()
        self.home_manager.homeWindow()

    def openSuggestions(self):
        suggestions_Window()

    def __init__(self, manager, *args, **kwargs):

        self.reports = {
            "Order by Most Paid Teachers": "SELECT teachers.*, transactions.amount FROM teachers LEFT JOIN transactions ON transactions.teacher_id = teachers.teacher_id WHERE transactions.type = 'Salary' ORDER BY transactions.amount DESC;",
            "Order by Highest Achieving Student" : "SELECT students.*, student_br_teacher.class_year, SUM(students_asses.grade) as total_marks FROM students LEFT JOIN students_asses ON students.student_id = students_asses.student_id LEFT JOIN student_br_teacher ON student_br_teacher.student_id = students.student_id WHERE student_br_teacher.class_year = YEAR(current_date()) GROUP BY students_asses.student_id;",
            "Order by Student With Highest Attendance" : "SELECT students.*, COUNT(std_attendance.student_id) as total_attendance FROM students LEFT JOIN std_attendance ON std_attendance.student_id = students.student_id WHERE YEAR(std_attendance.date)=YEAR(current_date()) GROUP BY std_attendance.student_id ORDER BY COUNT(std_attendance.student_id) DESC;",
            "Order by Teacher With Highest Attendance" : "SELECT teachers.*, COUNT(tch_attendance.teacher_id) as total_attendance FROM teachers LEFT JOIN tch_attendance ON tch_attendance.teacher_id = teachers.teacher_id WHERE YEAR(tch_attendance.date)=YEAR(current_date()) GROUP BY tch_attendance.teacher_id ORDER BY COUNT(tch_attendance.teacher_id) DESC;"
        }

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
            18.0,
            571.0,
            anchor="nw",
            text="All rights reserved.",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            69.0,
            108.0,
            anchor="nw",
            text="Here you can choose to generate reports.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            243.0,
            52.0,
            anchor="nw",
            text="Reports\n",
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
            command=lambda: self.handle_generate(),
            relief="flat"
        )
        button_1.place(
            x=224.0,
            y=520.0,
            width=83.0,
            height=43.0
        )

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
            x=530.0,
            y=520.0,
            width=235.0,
            height=60.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openSuggestions(),
            relief="flat"
        )
        button_4.place(
            x=326.0,
            y=520.0,
            width=155.0,
            height=42.0
        )

        self.columns = {
            "Name": ["Name", 100],
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

        # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

        for row in self.reports.keys():
            self.treeview.insert("", "end", values=[row])

        self.mainloop()

    def on_treeview_select(self, event=None):
            try:
                self.treeview.selection()[0]
            except:
                self.selected_rid = None
                return
            # Get the selected item
            item = self.treeview.selection()[0]
            # Get the id
            self.selected_rid = self.treeview.item(item, "values")[0]

    def handle_generate(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        self.reports[self.selected_rid]
        sql_query = pd.read_sql_query(self.reports[self.selected_rid],mydb)
        df = pd.DataFrame(sql_query)
        directory = filedialog.asksaveasfilename()
        df = pd.DataFrame(sql_query)
        df.to_csv (directory, index = False)
