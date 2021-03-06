from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox
import mysql.connector


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def edit_Account_Window(username):
    Edit_Account(username)

class Edit_Account(Toplevel):
    def __init__(self, username, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)
        self.username = username
        self.display_account_info_to_edit()

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
            text="Username: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            232.0,
            anchor="nw",
            text="New Password: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            340.0,
            anchor="nw",
            text="Address:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            395.0,
            anchor="nw",
            text="Phone: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            281.0,
            anchor="nw",
            text="Name: ",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            215.0,
            95.0,
            anchor="nw",
            text="Here you can edit your account details.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            289.0,
            24.0,
            anchor="nw",
            text="Edit Account",
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
        entry_text_1.set(self.account_info[0])
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state = "normal",
            textvariable= entry_text_1
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
            406.5,
            image=entry_image_2
        )
        entry_text_2 = StringVar()
        entry_text_2.set(self.account_info[4])
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state = "normal",
            textvariable= entry_text_2
        )
        self.entry_2.place(
            x=275.0,
            y=387.0,
            width=331.0,
            height=37.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            440.5,
            352.5,
            image=entry_image_3
        )
        entry_text_3 = StringVar()
        entry_text_3.set(self.account_info[3])
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state = "normal",
            textvariable= entry_text_3
        )
        self.entry_3.place(
            x=275.0,
            y=333.0,
            width=331.0,
            height=37.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            440.5,
            298.5,
            image=entry_image_4
        )
        entry_text_4 = StringVar()
        entry_text_4.set(self.account_info[2])
        self.entry_4 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state = "normal",
            textvariable= entry_text_4
        )
        self.entry_4.place(
            x=275.0,
            y=279.0,
            width=331.0,
            height=37.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            440.5,
            244.5,
            image=entry_image_5
        )
        entry_text_5 = StringVar()
        entry_text_5.set(self.account_info[1])
        self.entry_5 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state = "normal",
            textvariable= entry_text_5,
            show="*"
        )
        self.entry_5.place(
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
            command=self.update_account_info,
            relief="flat"
        )
        button_1.place(
            x=289.0,
            y=469.0,
            width=231.0,
            height=52.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_2.place(
            x=658.0,
            y=469.0,
            width=105.0,
            height=52.0
        )
        self.resizable(False, False)
        self.mainloop()

    def display_account_info_to_edit(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from admin where username = %s;"
        param_list = list()
        param_list.append(self.username)
        mycursor.execute(sql,param_list)
        result = mycursor.fetchall()
        self.account_info = result[0]
        mydb.close()

    def update_account_info(self):
        updated_info = list()
        updated_info.append(self.entry_1.get())
        updated_info.append(self.entry_5.get())
        updated_info.append(self.entry_4.get())
        updated_info.append(self.entry_3.get())
        updated_info.append(self.entry_2.get())
        updated_info.append(self.username)

        mydb_conn = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        cursor = mydb_conn.cursor()

        sql = "UPDATE admin SET username = %s, password = %s, name = %s,  address = %s, phone = %s WHERE username = %s"
        cursor.execute(sql, updated_info)

        mydb_conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Successful", "Details Updated Successfully")
            self.destroy()

        else:
            messagebox.showerror("Error", "Failed to update student's details")
