from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from view.home.edit_account.build.gui import edit_Account_Window
from view.home.manage_attendance.build.gui import manage_Atten_Window

from view.home.manage_students.build.gui import manage_Std_Window
from view.home.manage_subjects.build.gui import manage_Sbj_Window
from view.home.manage_teachers.build.gui import manage_Tch_Window
from view.home.manage_transactions.build.gui import manage_Trns_Window
from utils.Constants import Constants



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def homeWindow():
     Home()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomeWindowManager:

    def homeWindow(self):
        home = Home(manager =self)



class Home(Toplevel):

    def openManageStudents(self):
        self.destroy()
        manage_Std_Window(self.manager)

    def openEditAccount(self):
        edit_Account_Window(Constants.LOGIN_USER_NAME)

    def openManageTeachers(self):
        self.destroy()
        manage_Tch_Window(self.manager)

    def openManageAttendance(self):
        self.destroy()
        manage_Atten_Window(self.manager)

    def openManageSubjects(self):
        self.destroy()
        manage_Sbj_Window(self.manager)

    def openManageTransactions(self):
        self.destroy()
        manage_Trns_Window(self.manager)


    def __init__(self, manager ,*args, **kwargs):

        self.manager = manager
        Toplevel.__init__(self, *args, **kwargs)

        self.title("School Management System")

        self.geometry("810x562")
        self.configure(bg="#FFFFFF")

        self.current_window = None        

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 562,
            width = 809,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            10.0,
            17.0,
            810.0,
            562.0,
            fill="#AFAEF0",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            797.0,
            549.0,
            fill="#FFFDFD",
            outline="")

        self.canvas.create_text(
            11.0,
            521.0,
            anchor="nw",
            text="All rights reserved ",
            fill="#000000",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            297.0,
            30.0,
            anchor="nw",
            text="Dashboard",
            fill="#000000",
            font=("Inter", 36 * -1)
        )
            # Manage Students Button
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openManageStudents(),
            relief="flat"
        )
        button_1.place(
            x=87.0,
            y=147.0,
            width=189.0,
            height=46.0
        )
            # Edit Account Button
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openEditAccount(),
            relief="flat"
        )
        button_2.place(
            x=482.0,
            y=309.0,
            width=189.0,
            height=46.0
        )
            # Manage Attendance Button
        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openManageAttendance(),
            relief="flat"
        )
        button_3.place(
            x=482.0,
            y=147.0,
            width=189.0,
            height=46.0
        )
            # Manage Transactions Button
        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openManageTransactions(),
            relief="flat"
        )
        button_4.place(
            x=482.0,
            y=223.0,
            width=189.0,
            height=46.0
        )
            # Manage Teachers Button
        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openManageTeachers(),
            relief="flat"
        )
        button_5.place(
            x=87.0,
            y=228.0,
            width=189.0,
            height=46.0
        )
            # Manage Subjects Button
        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openManageSubjects(),
            relief="flat"
        )
        button_6.place(
            x=87.0,
            y=309.0,
            width=189.0,
            height=46.0
        )
            # Log Out Button
        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            self.canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: quit(),
            relief="flat"
        )
        button_7.place(
            x=537.0,
            y=446.0,
            width=165.0,
            height=46.0
        )

        self.canvas.create_rectangle(
            28.0,
            16.0,
            29.0,
            18.0,
            fill="#D9D9D9",
            outline="")
        self.resizable(False, False)
        self.mainloop()

    def set_manager(self,manager):
        self.manager=manager