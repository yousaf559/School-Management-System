from pathlib import Path

from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage

from controller.admin_controller import AdminController
from controller.teacher_controller import TeacherController
from view.home.gui import HomeWindowManager
from view.teacher_home.build.gui import Teachers_HomeWindow
from utils.Constants import Constants


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def loginWindow():
    Login()

class Login(Toplevel):

    def handle_adminlogin(self):
        if AdminController.login(self.username.get(), self.password.get()):
            Constants.LOGIN_USER_NAME = self.username.get()
            self.destroy()
            HomeWindowManager().homeWindow()
            return

    def handle_teacherlogin(self):
        teacher_id = TeacherController.login(self.tch_username.get(), self.tch_password.get())
        if teacher_id:
            self.destroy()
            Teachers_HomeWindow(teacher_id)
            return

    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)
        self.title("School Management System")

        self.geometry("1000x600")
        self.configure(bg="#FFFFFF")

        self.current_window = None
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 602,
            width = 998,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            498.0,
            602.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            157.0,
            87.0,
            anchor="nw",
            text="Admin Login",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

        self.canvas.create_text(
            89.0,
            168.0,
            anchor="nw",
            text="Sign in to your account.",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            610.0,
            87.0,
            anchor="nw",
            text="Teacher Login",
            fill="#000000",
            font=("Inter", 36 * -1)
        )

        self.canvas.create_text(
            589.0,
            168.0,
            anchor="nw",
            text="Sign in to your account.",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            258.0,
            301.0,
            image=entry_image_1
        )
        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#CDCDCD",
            highlightthickness=0
        )
        self.username.place(
            x=67.0,
            y=272.0,
            width=382.0,
            height=56.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            258.0,
            402.0,
            image=entry_image_2
        )
        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#CDCDCD",
            highlightthickness=0,
            show="*"
        )
        self.password.place(
            x=67.0,
            y=373.0,
            width=382.0,
            height=56.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_2 = self.canvas.create_image(
            258.0,
            301.0,
            image=entry_image_3
        )
        self.tch_username = Entry(
            self.canvas,
            bd=0,
            bg="#CDCDCD",
            highlightthickness=0
        )
        self.tch_username.place(
            x=550.0,
            y=272.0,
            width=382.0,
            height=56.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            258.0,
            402.0,
            image=entry_image_4
        )
        self.tch_password = Entry(
            self.canvas,
            bd=0,
            bg="#CDCDCD",
            highlightthickness=0,
            show="*"
        )
        self.tch_password.place(
            x=550.0,
            y=373.0,
            width=382.0,
            height=56.0
        )

        self.canvas.create_rectangle(
            500.0,
            149.0,
            495.0,
            571.0,
            fill="#000000",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_adminlogin(),
            relief="raised"
        )
        button_1.place(
            x=65.0,
            y=463.0,
            width=382.0,
            height=58.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_teacherlogin(),
            relief="raised"
        )
        button_2.place(
            x=550.0,
            y=463.0,
            width=382.0,
            height=58.0
        )

        self.canvas.create_text(
            78.0,
            231.0,
            anchor="nw",
            text="Username:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            78.0,
            335.0,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            561.0,
            231.0,
            anchor="nw",
            text="Email:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            561.0,
            335.0,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )
        self.resizable(False, False)
        self.mainloop()

