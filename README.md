# Python Tkinter Expense Tracker

A simple desktop application built with Python and Tkinter for tracking personal expenses. Expenses are stored locally in an SQLite database.

## Features

* Add new expenses with Date (YYYY-MM-DD), Description, Category, and Amount.
* Expenses are saved persistently in a local SQLite database (`expenses.db`).
* View all recorded expenses in a sortable table format.
* The expense list automatically refreshes when a new expense is added.
* Basic input validation for required fields and numeric amount.

## Screenshot

*(Optional: Add a screenshot of your application window here)*
`![Expense Tracker Screenshot](path/to/your/screenshot.png)`

## Technologies Used

* Python 3.x
* Tkinter (via `tkinter.ttk` for themed widgets)
* SQLite 3 (via Python's built-in `sqlite3` module)

## Setup and Installation

1.  **Clone the repository (or download the source code):**
    ```bash
    git clone <your-repository-url>
    cd expense_tracker
    ```

2.  **Create and activate a virtual environment (Recommended):**
    * On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

3.  **Install dependencies:**
    *(Currently, this project only uses built-in Python libraries, so no external packages are required via `requirements.txt` unless you add features later).*

4.  **Database Setup:**
    The SQLite database file (`expenses.db`) and the necessary table (`expenses`) will be created automatically the first time you run the application via `main.py`.

## Usage

1.  Make sure your virtual environment is activated (if you created one).
2.  Run the main application script from the project's root directory (`expense_tracker/`):
    ```bash
    python main.py
    ```
3.  The application window will appear, displaying any previously saved expenses.
4.  Fill in the Date, Description, Category, and Amount fields.
5.  Press the `Enter` key while in the Amount field or click the "Add Expense" button.
6.  The expense will be saved, and the list will update.

## Future Improvements

* Add functionality to delete selected expenses.
* Implement editing of existing expenses.
* Add filtering or searching capabilities (e.g., by date range or category).
* Display summary statistics (e.g., total expenses).
* Use a calendar widget for date input.
* Use a dropdown (Combobox) for predefined categories.
* Improve date validation.
* Enhance visual styling.

