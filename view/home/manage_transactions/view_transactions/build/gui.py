from pathlib import Path
from tkinter.ttk import Treeview
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
import mysql.connector
from view.home.manage_transactions.view_transactions.edit_transaction.build.gui import edit_Trans_Window
from tkinter.messagebox import askyesno
import tkinter.ttk as ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_Trans_Window():
    View_Trans()

class View_Trans(Toplevel):

        # FOR RETURNING TO DASHBOARD 
    # def backToDashboard(self):
    #     self.destroy()
    #     #homeWindow()
    #     self.home_manager.homeWindow()

    def openEditTransaction(self):
        edit_Trans_Window(self, self.selected_rid)

    def __init__(self, *args, **kwargs):

        # self.home_manager=manager
        Toplevel.__init__(self, *args, **kwargs)

        def fixed_map(option):
            # Fix for setting text colour for Tkinter 8.6.9
            # From: https://core.tcl.tk/tk/info/509cafafae
            #
            # Returns the style map for 'option' with any styles starting with
            # ('!disabled', '!selected', ...) filtered out.

            # style.map() returns an empty list for missing options, so this
            # should be future-safe.
            return [elm for elm in style.map('Treeview', query_opt=option) if
                    elm[:2] != ('!disabled', '!selected')]

        style = ttk.Style()
        style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

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
            text="Transactions",
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
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_1.place(
            x=583.0,
            y=462.0,
            width=165.0,
            height=46.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.edit_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_edit(),
            relief="flat",
            state="disabled"
        )
        self.edit_btn.place(
            x=254.0,
            y=462.0,
            width=116.0,
            height=48.0
        )

        approve_image = PhotoImage(
            file=relative_to_assets("approve.png"))
        self.approve_btn = Button(
            self.canvas,
            image=approve_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.transaction_action('approved'),
            relief="flat",
            state="disabled"
        )
        self.approve_btn.place(
            x=190.0,
            y=462.0,
            width=50.0,
            height=50.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.delete_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.delete_transaction(),
            relief="flat",
            state="disabled",
        )
        self.delete_btn.place(
            x=380.0,
            y=462.0,
            width=116.0,
            height=48.0
        )

        reject_image = PhotoImage(
            file=relative_to_assets("reject.png"))
        self.reject_btn = Button(
            self.canvas,
            image=reject_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.transaction_action('rejected'),
            relief="flat",
            state="disabled"
        )
        self.reject_btn.place(
            x=520.0,
            y=462.0,
            width=50.0,
            height=50.0
        )

        self.canvas.create_rectangle(
            28.0,
            16.0,
            29.0,
            18.0,
            fill="#D9D9D9",
            outline="")

        self.columns = {
            "ID": ["ID", 10],
            "Date": ["Date", 100],
            "Amount": ["Amount", 100],
            "Type": ["Type", 80],
            "Description": ["Description", 80],
            "Teacher ID": ["Teacher ID", 80],
            "Student ID": ["Student ID", 80],
            "Status": ["Status", 80],        
        }

        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )
        self.treeview.tag_configure("approved", background="green", foreground="white")
        self.treeview.tag_configure("rejected", background="red", foreground="white")


        # Show the headings
        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.treeview.column(idx, width=txt[1])

        self.treeview.place(x=64.0, y=135.0, width=672.0, height=300.0)

        # set data in tree
        self.insert_transactions_data()
        # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)
        self.mainloop()

    def on_treeview_select(self, event=None):
            try:
                self.treeview.selection()[0]
            except:
                self.selected_rid = None
                return
            # Get the selected item
            self.selected_item = self.treeview.selection()[0]
            # Get the room id
            self.selected_rid = self.treeview.item(self.selected_item, "values")[0]
            self.edit_btn.config(state="normal")
            self.delete_btn.config(state="normal")
            self.approve_btn.config(state="normal")
            self.reject_btn.config(state="normal")

    def insert_transactions_data(self):
        self.treeview.delete(*self.treeview.get_children())
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
        )
        mycursor = mydb.cursor()

        sql = "SELECT * from transactions"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            self.treeview.insert("", "end", values=row)
        mydb.close()

    def handle_edit(self):
        self.openEditTransaction()

    def handle_refresh(self):
       self.insert_transactions_data()

    def delete_transaction(self):

        confirm_delete = askyesno(title='Confirmation',
                          message='Are you sure that you want to delete selected record?')
        if confirm_delete:

         mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin12",
            database="sms"
         )

         mycursor = mydb.cursor()
         query = "DELETE from transactions WHERE transaction_id = %s"
         param_list = list()
         param_list.append(self.selected_rid)
         mycursor.execute(query, param_list)
         mydb.commit()
         if mycursor.rowcount > 0:
             messagebox.showinfo("Successful", "Transaction Record Deleted Successfully")
             self.handle_refresh()
         else:
             messagebox.showinfo("Error", "Unable to delete selected transaction")

    def transaction_action(self, approved):
        mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin12",
        database="sms"
        )
        mycursor = mydb.cursor()

        query1 = "UPDATE transactions SET status = %s WHERE transaction_id = %s"
        param_list1 = list()
        param_list1.append(approved)
        param_list1.append(self.selected_rid)
        mycursor.execute(query1, param_list1)
        mydb.commit()
        values = self.treeview.item(self.selected_item, "values")
        #values[7] = approved
        values_list = list(values)
        #values_list.append(*values)
        values_list[7] = approved
        self.treeview.item(self.selected_item, tags=[approved], values=values_list)
        