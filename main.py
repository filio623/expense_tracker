import tkinter as tk
from gui import ExpenseTrackerGUI
from database import init_database



if __name__ == '__main__':
    init_database()
    root = tk.Tk()

    app = ExpenseTrackerGUI(root)

    root.mainloop()
