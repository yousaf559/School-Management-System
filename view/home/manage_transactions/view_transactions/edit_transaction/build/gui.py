from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def edit_Trans_Window(parent,transaction_id):
    Edit_Trans(parent,transaction_id)

class Edit_Trans(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    # def backToDashboard(self):
    #     self.destroy()
    #     #homeWindow()
    #     self.home_manager.homeWindow()

    def __init__(self, parent, transaction_id, *args, **kwargs):

        # self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)
        self.transaction_id = transaction_id
        self.parent = parent
        self.display_transaction_info_to_edit()

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
            text="Date:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            232.0,
            anchor="nw",
            text="Amount:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            110.0,
            288.0,
            anchor="nw",
            text="Type:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            111.0,
            342.0,
            anchor="nw",
            text="Description:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )
        self.canvas.create_text(
            225.0,
            96.0,
            anchor="nw",
            text="Here you can edit a Transaction.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            221.0,
            24.0,
            anchor="nw",
            text="Edit Transaction",
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
        entry_text_1.set(self.transaction_info[1])
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
            244.5,
            image=entry_image_2
        )
        entry_text_2 = StringVar()
        entry_text_2.set(self.transaction_info[2])
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
            y=225.0,
            width=331.0,
            height=37.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            440.5,
            299.5,
            image=entry_image_3
        )
        entry_text_3 = StringVar()
        entry_text_3.set(self.transaction_info[3])
        self.entry_3 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            state="normal",
            textvariable=entry_text_3
        )
        self.entry_3.place(
            x=275.0,
            y=280.0,
            width=331.0,
            height=37.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            440.5,
            360.5,
            image=entry_image_4
        )
        entry_text_4 = StringVar()
        entry_text_4.set(self.transaction_info[4])
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
            y=341.0,
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
            command=self.update_transaction_info,
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

    def display_transaction_info_to_edit(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from transactions where transaction_id = " + self.transaction_id + ";"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.transaction_info = result[0]
        mydb.close()

    def update_transaction_info(self):
        updated_info = list()
        updated_info.append(self.entry_1.get())
        updated_info.append(self.entry_2.get())
        updated_info.append(self.entry_3.get())
        updated_info.append(self.entry_4.get())
        updated_info.append(self.transaction_id)

        mydb_conn = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        cursor = mydb_conn.cursor()

        sql = "UPDATE transactions SET transaction_date = %s, amount = %s, type = %s, description = %s WHERE transaction_id = %s"
        cursor.execute(sql, updated_info)

        mydb_conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Successful", "Details Updated Successfully")
            self.destroy()
            self.parent.handle_refresh()

        else:
            messagebox.showerror("Error", "Failed to update student's details")
