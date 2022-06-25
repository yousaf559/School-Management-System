from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox
import mysql.connector
from tkinter.ttk import Treeview


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mark_Ass_Window():
    Mark_Ass()

class Mark_Ass(Toplevel):

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

        self.columns = {
            "Student ID": ["Student ID", 10],
            "Assignment ID": ["Assignment ID", 10],
            "Marks Obtained": ["Marks Obtained", 100]    
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

        self.treeview.place(x=221.0, y=302.0, width=447.0, height=184.0)

        # set data in tree
        self.insert_transactions_data()
        # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

        self.canvas.create_text(
            110.0,
            178.0,
            anchor="nw",
            text="Marks:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            232.0,
            anchor="nw",
            text="Student List:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            215.0,
            95.0,
            anchor="nw",
            text="Here you can aassign marks for selected Assignment.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            260.0,
            27.0,
            anchor="nw",
            text="Mark Student's Assignment",
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
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_1.place(
            x=275.0,
            y=171.0,
            width=331.0,
            height=37.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            440.5,
            244.5,
            image=entry_image_4
        )
        self.entry_4 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_4.place(
            x=275.0,
            y=225.0,
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
            command=self.add_transaction_info,
            relief="flat"
        )
        button_2.place(
            x=280.0,
            y=466.0,
            width=231.0,
            height=52.0
        )

        self.resizable(False, False)
        self.mainloop()


    def on_treeview_select(self, event=None):
        try:
            self.treeview.selection()[0]
        except:
            self.selected_rid = None
            return
        # Get the selected item
        self.selected_item = self.treeview.selection()[0]
        # Get the room id
        self.selected_rid = self.treeview.item(self.selected_item, "values")[0]
        self.edit_btn.config(state="normal")
        self.delete_btn.config(state="normal")

    def insert_students_assignment_data(self):
        self.treeview.delete(*self.treeview.get_children())
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from students_asses"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.treeview.insert("", "end", values=row)
        mydb.close()