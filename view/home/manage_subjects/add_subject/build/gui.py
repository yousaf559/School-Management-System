
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_Subject_Window():
    Add_Subject()

class Add_Subject(Toplevel):

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

        self.canvas.create_text(
            110.0,
            178.0,
            anchor="nw",
            text="ID:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            232.0,
            anchor="nw",
            text="Name:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            253.0,
            92.0,
            anchor="nw",
            text="Here you can add a new Subject.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            260.0,
            27.0,
            anchor="nw",
            text="Add New Subject",
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

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            440.5,
            244.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_2.place(
            x=275.0,
            y=225.0,
            width=331.0,
            height=37.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_subject_info,
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

    def add_subject_info(self):
        new_info = list()
        new_info.append(self.entry_1.get())
        new_info.append(self.entry_2.get())

        mydb_conn = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        cursor = mydb_conn.cursor()

        sql = "INSERT INTO subjects (subject_id, subject_name) VALUES (%s, %s)"
        cursor.execute(sql, new_info)

        mydb_conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Successful", "Subject Record Added")
            self.destroy()

        else:
            messagebox.showerror("Error", "Failed to update student's details")
