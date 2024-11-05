import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("bookstore.db")
mycursor = conn.cursor()

def first_time_login():
    """Create tables in the database if they do not exist.""" 
    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Book_Record (
        BookID INTEGER PRIMARY KEY,
        Bookname TEXT NOT NULL,
        Author TEXT NOT NULL,
        Quantity INTEGER NOT NULL,
        Price REAL NOT NULL
    )
    """)
    
    # Create Purchase Log table
    mycursor.execute(""" 
    CREATE TABLE IF NOT EXISTS PurchaseLog (
        PurchaseID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID TEXT NOT NULL,
        BookID INTEGER NOT NULL,
        Bookname TEXT NOT NULL,
        Author TEXT NOT NULL,
        Price REAL NOT NULL,
        Quantity INTEGER NOT NULL,
        FOREIGN KEY (BookID) REFERENCES Book_Record (BookID)
    )
    """)
    conn.commit()

class BookstoreApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Bibliomart Book Store")
        self.window.configure(bg="#f0f0f0")
        self.window.minsize(800, 600)
        
        self.configure_grid()
        first_time_login()
        self.create_widgets()

    def configure_grid(self):
        """Configure grid layout with proper weights.""" 
        for i in range(8):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(6):
            self.window.grid_columnconfigure(i, weight=1)

    def create_widgets(self):
        """Create and arrange the UI components.""" 
        self.text_color = "#333333"
        self.title_bg = "#3399ff"
        self.title_fg = "#ffffff"
        
        self.title_font = ("Arial", 28, "bold")
        self.instruction_font = ("Arial", 20, "bold")
        self.button_font = ("Arial", 14)

        self.create_title_frame()
        self.create_instruction_label()
        self.create_buttons()

    def create_title_frame(self):
        """Create and place the title frame with logo and label.""" 
        self.title_frame = tk.Frame(self.window, bg=self.title_bg)
        self.title_frame.grid(row=0, column=0, columnspan=6, sticky='ew', padx=20, pady=10)

        try:
            self.logo_image = tk.PhotoImage(file=r"F:\Divya MCA Notes\python new\bookstore_logo.png")
            self.logo_label = tk.Label(self.title_frame, image=self.logo_image, bg=self.title_bg)
            self.logo_label.pack(side=tk.RIGHT, padx=(10, 20))
        except Exception as e:
            print(f"Error loading image: {e}")

        self.title_label = tk.Label(self.title_frame, text="BIBLIOMART - BOOK STORE APPLICATION",
                                 bg=self.title_bg, fg=self.title_fg, font=self.title_font)
        self.title_label.pack(side=tk.LEFT, padx=(20, 10), pady=10, expand=True, fill=tk.X)

    def create_instruction_label(self):
        """Create and place the instruction label.""" 
        instruction_label = tk.Label(self.window, text="Select an option below",
                                  bg="#f0f0f0", fg=self.text_color, font=self.instruction_font)
        instruction_label.grid(row=1, column=0, columnspan=6, pady=(20, 10))

    def create_buttons(self):
        """Create and place the Administrator and Customer buttons.""" 
        admin_button = tk.Button(self.window, text="Administrator", width=20, height=2,
                              bg="#4682b4", fg="white", font=self.button_font,
                              command=self.show_admin_login)
        admin_button.grid(row=2, column=0, columnspan=6, pady=(20, 10))

        customer_button = tk.Button(self.window, text="Shop", width=20, height=2,
                                 bg="#4682b4", fg="white", font=self.button_font,
                                 command=self.customer_login)
        customer_button.grid(row=3, column=0, columnspan=6, pady=(20, 10))

    def clear_window(self):
        """Clear all widgets from the window.""" 
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_admin_login(self):
        """Display the admin login screen.""" 
        self.clear_window()
        from administrator import Administrator
        admin = Administrator(self.window, mycursor, conn, self)
        admin.show_login()

    def customer_login(self):
        """Display the customer menu.""" 
        self.clear_window()
        from customer import Customer
        customer = Customer(self.window, mycursor, conn, self)
        customer.show_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()
