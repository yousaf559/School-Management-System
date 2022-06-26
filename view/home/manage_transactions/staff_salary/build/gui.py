from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox
import mysql.connector
from tkinter.ttk import Treeview


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def staff_salary_Window():
    Staff_Salary()

class Staff_Salary(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    # def backToDashboard(self):
    #     self.destroy()
    #     #homeWindow()
    #     self.home_manager.homeWindow()

    def __init__(self, *args, **kwargs):

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
            215.0,
            95.0,
            anchor="nw",
            text="Here you can pay salary to staff.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            260.0,
            27.0,
            anchor="nw",
            text="Pay Salary",
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
            x=658.0,
            y=466.0,
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
            command=lambda: self.pay_salary(),
            relief="flat"
        )
        button_2.place(
            x=280.0,
            y=466.0,
            width=231.0,
            height=52.0
        )

        self.columns = {
            "ID": ["ID", 10],
            "Name": ["Name", 100],
            "Address": ["Address", 170],
            "Subject Taught": ["Subject Taught", 80],
            "Phone": ["Phone", 80],
            "Salary": ["Salary", 80],
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
        self.insert_teachers_data()
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
            item = self.treeview.selection()[0]
            # Get the id
            self.selected_rid = self.treeview.item(item, "values")[0]
            self.salary = self.treeview.item(item, "values")[5]

    def insert_teachers_data(self):
        self.treeview.delete(*self.treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        # sql = "SELECT teacher_id, teacher_name, teacher_address, subject_taught, teacher_phone from teachers"
        sql = "SELECT teachers.teacher_id, teachers.teacher_name, teachers.teacher_address, subjects.subject_name, teachers.teacher_phone, teachers.salary from teachers LEFT JOIN subjects ON subjects.subject_id = teachers.subject_taught;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.treeview.insert("", "end", values=row)
        mydb.close()

    def handle_refresh(self):
       self.insert_teachers_data()


    def pay_salary(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        myparam = list()
        myparam.append(self.salary)
        myparam.append(self.selected_rid)

        sql = "SELECT * from transactions WHERE teacher_id = %s AND type = 'Salary' AND MONTH(transaction_date) = MONTH(CURRENT_DATE())"
        mycursor.execute(sql, [self.selected_rid])
        result = mycursor.fetchall()
        if len(result) <= 0:
            sql = "INSERT INTO transactions (transaction_date, amount, type, teacher_id, status, description) VALUES (current_date(), %s, 'Salary', %s, 'approved', '')"
            mycursor.execute(sql, myparam)
            mydb.commit()
            mydb.close()
        else:
            messagebox.showerror("Error","Salary Already Paid to Selected Staff Member for this month")


