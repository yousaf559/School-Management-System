from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox, OptionMenu
import mysql.connector
from validate_email import validate_email

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def edit_Teacher_Window(parent,teacher_id):
    Edit_Teacher(parent,teacher_id)

class Edit_Teacher(Toplevel):

    def __init__(self, parent, teacher_id, *args, **kwargs):

        # self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)
        self.teacher_id = teacher_id
        self.parent = parent
        self.display_teacher_info_to_edit()

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
            text="Full Name: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            232.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            340.0,
            anchor="nw",
            text="Phone:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            400.0,
            anchor="nw",
            text="Email:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            440.0,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            495.0,
            anchor="nw",
            text="Salary:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            281.0,
            anchor="nw",
            text="Subject: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            215.0,
            95.0,
            anchor="nw",
            text="Here you can edit a Teacher Record.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            260.0,
            27.0,
            anchor="nw",
            text="Edit Teacher",
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
        entry_text_1 = StringVar()
        entry_text_1.set(self.teacher_info[1])
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_1
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
            352.5,
            image=entry_image_2
        )
        entry_text_2 = StringVar()
        entry_text_2.set(self.teacher_info[3])
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_2
        )
        self.entry_2.place(
            x=275.0,
            y=333.0,
            width=331.0,
            height=37.0
        )

        # entry_image_3 = PhotoImage(
        #     file=relative_to_assets("entry_3.png"))
        # entry_bg_3 = self.canvas.create_image(
        #     440.5,
        #     298.5,
        #     image=entry_image_3
        # )
        # entry_text_3 = StringVar()
        # entry_text_3.set(self.teacher_info[3])
        # self.entry_3 = Entry(
        #     self,
        #     bd=0,
        #     bg="#D9D9D9",
        #     highlightthickness=0,
        #     state="normal",
        #     textvariable=entry_text_3
        # )
        # self.entry_3.place(
        #     x=275.0,
        #     y=279.0,
        #     width=331.0,
        #     height=37.0
        # )

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
            x=275.0,
            y=279.0,
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
        entry_text_4 = StringVar()
        entry_text_4.set(self.teacher_info[2])
        self.entry_4 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_4
        )
        self.entry_4.place(
            x=275.0,
            y=225.0,
            width=331.0,
            height=37.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_5 = self.canvas.create_image(
            440.5,
            406.5,
            image=entry_image_5
        )
        entry_text_5 = StringVar()
        entry_text_5.set(self.teacher_info[4])
        self.entry_5 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_5
        )
        self.entry_5.place(
            x=275.0,
            y=387.0,
            width=331.0,
            height=37.0
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_6 = self.canvas.create_image(
            440.5,
            460.5,
            image=entry_image_5
        )
        entry_text_6 = StringVar()
        entry_text_6.set(self.teacher_info[5])
        self.entry_6 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_6,
            show="*"
        )
        self.entry_6.place(
            x=275.0,
            y=441.0,
            width=331.0,
            height=37.0
        )

        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_7 = self.canvas.create_image(
            440.5,
            514.5,
            image=entry_image_7
        )
        entry_text_7 = StringVar()
        entry_text_7.set(self.teacher_info[7])
        self.entry_7 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_7
        )
        self.entry_7.place(
            x=275.0,
            y=495.0,
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
            y=540.0,
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
            command=self.update_teacher_info,
            relief="flat"
        )
        button_2.place(
            x=280.0,
            y=540.0,
            width=231.0,
            height=52.0
        )

        self.resizable(False, False)
        self.mainloop()

    def display_teacher_info_to_edit(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from teachers where teacher_id = " + self.teacher_id + ";"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.teacher_info = result[0]
        mydb.close()

    def update_teacher_info(self):
        if validate_email(self.entry_5.get()):
            updated_info = list()
            updated_info.append(self.entry_1.get())
            updated_info.append(self.entry_4.get())
            updated_info.append(self.subject_id)
            updated_info.append(self.entry_2.get())
            updated_info.append(self.entry_5.get())
            updated_info.append(self.entry_6.get())
            updated_info.append(self.entry_7.get())
            updated_info.append(self.teacher_id)

            mydb_conn = mysql.connector.connect(
                host="localhost",
                user="admin",
                password="admin12",
                database="sms"
            )
            cursor = mydb_conn.cursor()

            sql = "UPDATE teachers SET teacher_name = %s, teacher_address = %s, subject_taught = %s, teacher_phone = %s, tch_email = %s, tch_password = %s, salary = %s WHERE teacher_id = %s"
            cursor.execute(sql, updated_info)

            mydb_conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Successful", "Details Updated Successfully")
                self.destroy()
                self.parent.handle_refresh()

            else:
                messagebox.showerror("Error", "Failed to update teacher's details")
        else:
            messagebox.showerror("Error", "Enter a valid email address")

    def display_selected(self):
        subject_hash_values = list(self.subjects_hash.values())
        subject_hash_keys = list(self.subjects_hash.keys())
        self.subject_id = subject_hash_keys[subject_hash_values.index(self.menu.get())]
