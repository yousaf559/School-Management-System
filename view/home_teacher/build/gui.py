from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
# from view.home.manage_students.add_student.build.gui import add_Student_Window
# from view.home.manage_students.view_students.build.gui import view_Students_Window
from view.home_teacher.mark_student_attendance.build.gui import markStd_Attendance


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def tch_Dashboard_Window(teacher_id):
    Tch_Dashboard(teacher_id)

class Tch_Dashboard(Toplevel):

    def open_mark_std_atten(self):
        markStd_Attendance(self.teacher_id)

    def __init__(self, teacher_id,*args, **kwargs):

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
            text="Here you can choose a function",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            243.0,
            52.0,
            anchor="nw",
            text="Teacher Dashboard\n",
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
            command=lambda: self.open_mark_std_atten(),
            relief="flat"
        )
        button_1.place(
            x=87.0,
            y=147.0,
            width=235.0,
            height=60.0
        )
            # Log Out Button
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: quit(),
            relief="flat"
        )
        button_2.place(
            x=583.0,
            y=462.0,
            width=165.0,
            height=46.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_4 = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("sad"),
            relief="flat"
        )
        button_4.place(
            x=487.0,
            y=147.0,
            width=175.0,
            height=52.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_5 = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("sad"),
            relief="flat"
        )
        button_5.place(
            x=87.0,
            y=228.0,
            width=175.0,
            height=62.0
        )

        self.resizable(False, False)
        self.mainloop()