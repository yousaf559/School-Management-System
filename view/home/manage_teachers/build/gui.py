from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from view.home.manage_teachers.add_teacher.build.gui import add_Teacher_Window
from view.home.manage_teachers.view_teachers.build.gui import view_Teachers_Window


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("814x615")
# window.configure(bg = "#FFFFFF")

def manage_Tch_Window(manager):
    Manage_Tch(manager = manager)

class Manage_Tch(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    def backToDashboard(self):
        self.destroy()
        #homeWindow()
        self.home_manager.homeWindow()

    def openAddTeacher(self):
        add_Teacher_Window()

    def openViewTeachers(self):
        view_Teachers_Window()

    def __init__(self, manager, *args, **kwargs):

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
            text="Here you can choose whether to Add, Edit or Delete a Teacher Record",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            243.0,
            52.0,
            anchor="nw",
            text="Manage Teachers\n",
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
            command=lambda: self.openAddTeacher(),
            relief="flat"
        )
        button_1.place(
            x=124.0,
            y=188.0,
            width=235.0,
            height=60.0
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
            x=446.0,
            y=468.0,
            width=235.0,
            height=60.0
        )

        # button_image_3 = PhotoImage(
        #     file=relative_to_assets("button_3.png"))
        # button_3 = Button(
        #     self.canvas,
        #     image=button_image_3,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_3 clicked"),
        #     relief="flat"
        # )
        # button_3.place(
        #     x=446.0,
        #     y=304.0,
        #     width=235.0,
        #     height=60.0
        # )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openViewTeachers(),
            relief="flat"
        )
        button_4.place(
            x=446.0,
            y=188.0,
            width=235.0,
            height=60.0
        )
        self.resizable(False, False)
        self.mainloop()
