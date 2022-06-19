import tkinter as tk
from view.login.gui import loginWindow

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window



if __name__ == "__main__":
    loginWindow()
    # mainWindow()

    root.mainloop()
