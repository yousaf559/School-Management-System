from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox, OptionMenu
import mysql.connector


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_Ass_Window(teacher_id):
    Add_Ass(teacher_id)

class Add_Ass(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    # def backToDashboard(self):
    #     self.destroy()
    #     #homeWindow()
    #     self.home_manager.homeWindow()

    def __init__(self, teacher_id, *args, **kwargs):
        self.teacher_id = teacher_id

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
            text="Date(YYYY-MM-DD):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            340.0,
            anchor="nw",
            text="Resource URL:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            400.0,
            anchor="nw",
            text="Total Marks:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            441.0,
            anchor="nw",
            text="Subject:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            281.0,
            anchor="nw",
            text="Short Description: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            215.0,
            95.0,
            anchor="nw",
            text="Here you can add a new Assignment.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            260.0,
            27.0,
            anchor="nw",
            text="Add New Assignment",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            475.5,
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
            x=310.0,
            y=171.0,
            width=331.0,
            height=37.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            475.5,
            352.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_2.place(
            x=310.0,
            y=333.0,
            width=331.0,
            height=37.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            475.5,
            298.5,
            image=entry_image_3
        )
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_3.place(
            x=310.0,
            y=279.0,
            width=331.0,
            height=37.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            475.5,
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
            x=310.0,
            y=225.0,
            width=331.0,
            height=37.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_5 = self.canvas.create_image(
            475.5,
            406.5,
            image=entry_image_5
        )
        self.entry_5 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.entry_5.place(
            x=310.0,
            y=387.0,
            width=331.0,
            height=37.0
        )

        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT subject_id, subject_name FROM subjects"
        mycursor.execute(sql)
        subjects = mycursor.fetchall()
        self.subjects_hash = {}
        for id, name in subjects:
          self.subjects_hash[id] = f'{id} / {name}'

        self.menu= StringVar()
        self.menu.set("Select Subject")
        self.drop= OptionMenu(
            self,
            self.menu,
            command=lambda x:  self.display_selected(),
            *self.subjects_hash.values()
           )
        self.drop.place(
            x=310.0,
            y=441.0,
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
            y=520.0,
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
            command=self.add_ass_info,
            relief="flat"
        )
        button_2.place(
            x=280.0,
            y=520.0,
            width=231.0,
            height=52.0
        )

        self.resizable(False, False)
        self.mainloop()

    def add_ass_info(self):
        new_info = list()
        new_info.append(self.entry_1.get())
        new_info.append(self.entry_4.get())
        new_info.append(self.entry_3.get())
        new_info.append(self.entry_2.get())
        new_info.append(self.teacher_id)
        new_info.append(self.entry_5.get())
        new_info.append(self.subject_id)
        

        mydb_conn = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        cursor = mydb_conn.cursor()

        sql = "INSERT INTO assignments (name, date, description, resource, teacher_id, marks_alloted, subject) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, new_info)

        mydb_conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Successful", "New Assignment Created")
            self.destroy()

        else:
            messagebox.showerror("Error", "Failed to create Assignment")

    def display_selected(self):
        subject_hash_values = list(self.subjects_hash.values())
        subject_hash_keys = list(self.subjects_hash.keys())
        self.subject_id = subject_hash_keys[subject_hash_values.index(self.menu.get())]
