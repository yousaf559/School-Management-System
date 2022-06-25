from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from view.home_teacher.manage_assignments.add_new.build.gui import add_Ass_Window
from view.home_teacher.manage_assignments.view_existing.build.gui import view_Asses_Window

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def manage_Ass_Window(teacher_id):
    Manage_Asses(teacher_id)

class Manage_Asses(Toplevel):

    def openAddAss(self):
        add_Ass_Window(self.teacher_id)

    def openViewAss(self):
        view_Asses_Window(self.teacher_id)


    def __init__(self, teacher_id, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)
        self.teacher_id = teacher_id

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
            text="Here you can manage Subject Assignments.",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            243.0,
            52.0,
            anchor="nw",
            text="Manage Assignments\n",
            fill="#000000",
            font=("Inter", 36 * -1)
        )
            # New Assignment
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openAddAss(),
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
            command=lambda: self.destroy(),
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
            # Manage Existing Assignments
        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.openViewAss(),
            relief="flat"
        )
        button_4.place(
            x=446.0,
            y=188.0,
            width=235.0,
            height=60.0
        )

        # button_image_5 = PhotoImage(
        #     file=relative_to_assets("button_5.png"))
        # button_5 = Button(
        #     self.canvas,
        #     image=button_image_5,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_5 clicked"),
        #     relief="flat"
        # )
        # button_5.place(
        #     x=124.0,
        #     y=300.0,
        #     width=235.0,
        #     height=60.0
        # )
        self.resizable(False, False)
        self.mainloop()
