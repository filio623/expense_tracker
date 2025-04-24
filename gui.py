import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import add_expense, get_all_expenses, init_database

class ExpenseTrackerGUI:
    """
    Manages the main GUI window for the Expense Tracker.
    """
    def __init__(self, root_window):
        """
        Initializes the GUI components.

        Args:
            root_window (tk.Tk): The main Tkinter window.
        """
        self.root = root_window
        self.root.title("Expense Tracker")
        # self.root.geometry("800x600") # Optional: Set initial window size

        # Configure root window grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1) # Allow Treeview frame to expand

        # --- Create Frames ---
        self._create_input_frame()
        self._create_display_frame()

        # --- Load initial data ---
        self._load_expenses() # We'll implement this later

    def _create_input_frame(self):
        """Creates the frame for input fields and the add button."""
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        input_frame.columnconfigure(1, weight=1) # Allow entry fields to expand slightly
        input_frame.columnconfigure(3, weight=1)

        # --- Widgets for Input Frame ---
        # Date
        ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.date_entry = ttk.Entry(input_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        # TODO: Add default date? Maybe a calendar picker later?

        # Description
        ttk.Label(input_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.desc_entry = ttk.Entry(input_frame, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="ew") # Span across more columns

        # Category
        ttk.Label(input_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.category_entry = ttk.Entry(input_frame, width=15)
        self.category_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        # TODO: Maybe use a Combobox/dropdown later?

        # Amount
        ttk.Label(input_frame, text="Amount:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(input_frame, width=15)
        self.amount_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

        # Add Expense Button
        self.add_button = ttk.Button(input_frame, text="Add Expense", command=self._add_expense_callback)
        self.add_button.grid(row=3, column=0, columnspan=4, pady=10)

    def _create_display_frame(self):
        """Creates the frame for displaying the list of expenses."""
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(0, weight=1)

        # --- Treeview for Expenses ---
        columns = ('id', 'date', 'description', 'category', 'amount')
        self.tree = ttk.Treeview(display_frame, columns=columns, show='headings', height=15)

        # Define headings
        self.tree.heading('id', text='ID')
        self.tree.heading('date', text='Date')
        self.tree.heading('description', text='Description')
        self.tree.heading('category', text='Category')
        self.tree.heading('amount', text='Amount')

        # Configure column widths (adjust as needed)
        self.tree.column('id', width=40, stretch=tk.NO, anchor='center')
        self.tree.column('date', width=100, stretch=tk.NO, anchor='center')
        self.tree.column('description', width=300) # Allow description to stretch
        self.tree.column('category', width=120, anchor='w')
        self.tree.column('amount', width=80, anchor='e') # Align amount to the right (east)

        self.tree.grid(row=0, column=0, sticky='nsew')

        # --- Scrollbar ---
        scrollbar = ttk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # TODO: Add buttons for Delete/Edit later?
        # TODO: Add summary labels (e.g., Total Expenses) later?

    def _add_expense_callback(self, event=None):
        """Handles the 'Add Expense' button click."""
        # --- Get data from entry fields ---
        date = self.date_entry.get()
        description = self.desc_entry.get()
        category = self.category_entry.get()
        amount_str = self.amount_entry.get()

        # --- Basic Validation ---
        if not all([date, description, category, amount_str]):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            # Convert amount to float
            amount = float(amount_str)
            if amount <= 0: # Add check for non-positive amount
                 messagebox.showerror("Input Error", "Amount must be positive.")
                 return
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a valid number.")
            return

        # --- Call database function (placeholder) ---
        print(f"Attempting to add: Date={date}, Desc={description}, Cat={category}, Amt={amount}")
        success = add_expense(date, description, category, amount)

        # --- Update display and clear fields (placeholder) ---
        if success: 
            messagebox.showinfo("Success", "Expense added successfully!") # Placeholder feedback
            self._clear_input_fields()
            self._load_expenses() #Refresh the list
        else:
            messagebox.showerror("Database Error", "Failed to add expense to the database.")

    def _clear_input_fields(self):
        """Clears the content of the input entry fields."""
        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        # Optional: Set focus back to the first field
        # self.date_entry.focus_set()

    # --- Placeholder for loading data ---
    def _load_expenses(self):
        """Clears the Treeview and loads all expenses from the database."""
        # Clear existing items in the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
    
        # Get expenses from database
        print("Loading expenses from database....")
        expenses = get_all_expenses()
        print(f"Found {len(expenses)} expenses")
    
        # Insert expenses into the treeview
        for expense in expenses:
            formatted_amount = f"{expense['amount']:.2f}"
            self.tree.insert('', tk.END, values=(
                expense['id'],
                expense['date'],
                expense['description'],
                expense['category'],
                formatted_amount # Format amount to 2 decimal places
            ))
        print("Finished loading expenses into Treeview.")
        self.root.update_idletasks() # Force GUI to process updates

# --- Main execution block (Should be in main.py) ---
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ExpenseTrackerGUI(root)
#     root.mainloop()
