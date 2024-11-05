import tkinter as tk
from tkinter import Frame, Label, Button, Entry, messagebox, Toplevel, Listbox, END, Scrollbar, Canvas

class Administrator:
    def __init__(self, window, mycursor, conn, main_app):
        self.window = window
        self.mycursor = mycursor
        self.conn = conn
        self.main_app = main_app  # Reference to the main application

        # Define colors and fonts
        self.bg_color = "#e0f7fa"  # Light cyan background
        self.button_color = "#00796b"  # Dark teal for buttons
        self.text_color = "#004d40"  # Dark teal text
        self.title_font = ("Arial", 24, "bold")
        self.label_font = ("Arial", 16)
        self.button_font = ("Arial", 14)
        self.alert_font = ("Arial", 14, "bold")

    def show_login(self):
        """Show the admin login page."""
        self.clear_window()

        login_frame = Frame(self.window, bg=self.bg_color)
        login_frame.pack(pady=50, padx=50, expand=True)

        Label(login_frame, text="Administrator Login", font=self.title_font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, columnspan=2, pady=20)

        Label(login_frame, text="Username:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.username_entry = Entry(login_frame, font=self.label_font)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(login_frame, text="Password:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.password_entry = Entry(login_frame, show="*", font=self.label_font)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        Button(login_frame, text="Login", command=self.validate_login, font=self.button_font, bg=self.button_color, fg="white").grid(row=3, column=0, columnspan=2, pady=20)

        # Add Back to Main Menu button
        Button(login_frame, text="Back to Main Menu", command=self.go_back_to_main_menu, font=self.button_font, bg=self.button_color, fg="white").grid(row=4, column=0, columnspan=2, pady=10)

    def validate_login(self):
        """Validate admin credentials."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple validation (this should be replaced with a more secure approach)
        if username == "admin" and password == "password":
            self.show_menu()
        else:
            self.show_custom_message("Login Failed", "Invalid username or password.")

    def show_menu(self):
        """Show the admin menu after successful login."""
        self.clear_window()

        canvas = Canvas(self.window, bg=self.bg_color)
        scrollbar = Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=self.bg_color)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Populate the menu items
        label = Label(scrollable_frame, text="Administrator Menu", font=self.title_font, bg=self.bg_color, fg=self.text_color)
        label.grid(row=0, column=0, columnspan=2, pady=20)

        button_specs = [
            ("New Book Record", self.add_new_book),
            ("Modify Book Record", self.modify_book),
            ("Delete Book Record", self.delete_book),
            ("View Book Records", self.view_book_records),
            ("Purchase Log", self.view_purchase_log),
            ("Search Book by ID", self.search_book_admin),
            ("Back to Main Menu", self.go_back_to_main_menu)
        ]

        # Center the buttons
        for index, (text, command) in enumerate(button_specs):
            Button(
                scrollable_frame,
                text=text,
                font=self.button_font,
                bg=self.button_color,
                fg="white",
                command=command,
                width=20,
                height=2
            ).grid(row=index + 1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Configure column weight to center-align the buttons
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(1, weight=1)

    def go_back_to_main_menu(self):
        """Clear current window and return to the main menu."""
        self.clear_window()
        self.main_app.create_widgets()  # Call create_widgets to set up the main menu

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.window.winfo_children():
            widget.destroy()

    def add_new_book(self):
        add_window = Toplevel(self.window)
        add_window.title("Add New Book")
        add_window.configure(bg=self.bg_color)

        # Use grid to center-align widgets
        Label(add_window, text="Book ID:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        book_id_entry = Entry(add_window, font=self.label_font)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(add_window, text="Book Name:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        book_name_entry = Entry(add_window, font=self.label_font)
        book_name_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(add_window, text="Author:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        author_entry = Entry(add_window, font=self.label_font)
        author_entry.grid(row=2, column=1, padx=10, pady=10)

        Label(add_window, text="Quantity:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=3, column=0, padx=10, pady=10, sticky="e")
        quantity_entry = Entry(add_window, font=self.label_font)
        quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        Label(add_window, text="Price:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=4, column=0, padx=10, pady=10, sticky="e")
        price_entry = Entry(add_window, font=self.label_font)
        price_entry.grid(row=4, column=1, padx=10, pady=10)

        Button(add_window, text="Add Book", command=lambda: self.insert_book(book_id_entry.get(), book_name_entry.get(), author_entry.get(), quantity_entry.get(), price_entry.get()), font=self.button_font, bg=self.button_color, fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        # Center the button
        add_window.grid_columnconfigure(0, weight=1)
        add_window.grid_columnconfigure(1, weight=1)

    def insert_book(self, book_id, book_name, author, quantity, price):
        try:
            # Insert new book record
            self.mycursor.execute("INSERT INTO Book_Record (BookID, Bookname, Author, Quantity, Price) VALUES (?, ?, ?, ?, ?)",
                                  (int(book_id), book_name, author, int(quantity), float(price)))
            self.conn.commit()
            self.show_custom_message("Success", "Book added successfully.")
        except Exception as e:
            self.show_custom_message("Error", str(e))

    def modify_book(self):
        modify_window = Toplevel(self.window)
        modify_window.title("Modify Book Record")
        modify_window.configure(bg=self.bg_color)

        Label(modify_window, text="Enter Book ID to Modify:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        book_id_entry = Entry(modify_window, font=self.label_font)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        Button(modify_window, text="Search", command=lambda: self.load_book_details(book_id_entry.get(), modify_window), font=self.button_font, bg=self.button_color, fg="white").grid(row=0, column=2, padx=10)

    def load_book_details(self, book_id, window):
        self.mycursor.execute("SELECT * FROM Book_Record WHERE BookID=?", (int(book_id),))
        book = self.mycursor.fetchone()

        if book:
            # Create entry fields for book details
            Label(window, text="Book Name:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            book_name_entry = Entry(window, font=self.label_font)
            book_name_entry.grid(row=1, column=1, padx=10, pady=10)
            book_name_entry.insert(0, book[1])

            Label(window, text="Author:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, padx=10, pady=10, sticky="e")
            author_entry = Entry(window, font=self.label_font)
            author_entry.grid(row=2, column=1, padx=10, pady=10)
            author_entry.insert(0, book[2])

            Label(window, text="Quantity:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=3, column=0, padx=10, pady=10, sticky="e")
            quantity_entry = Entry(window, font=self.label_font)
            quantity_entry.grid(row=3, column=1, padx=10, pady=10)
            quantity_entry.insert(0, book[3])

            Label(window, text="Price:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=4, column=0, padx=10, pady=10, sticky="e")
            price_entry = Entry(window, font=self.label_font)
            price_entry.grid(row=4, column=1, padx=10, pady=10)
            price_entry.insert(0, book[4])

            Button(window, text="Update", command=lambda: self.update_book(book_id, book_name_entry.get(), author_entry.get(), quantity_entry.get(), price_entry.get()), font=self.button_font, bg=self.button_color, fg="white").grid(row=5, column=0, columnspan=3, pady=10)
        else:
            self.show_custom_message("Error", "No book found with this ID.")

    def update_book(self, book_id, book_name, author, quantity, price):
        try:
            self.mycursor.execute("UPDATE Book_Record SET Bookname=?, Author=?, Quantity=?, Price=? WHERE BookID=?",
                                  (book_name, author, int(quantity), float(price), int(book_id)))
            self.conn.commit()
            self.show_custom_message("Success", "Book updated successfully.")
        except Exception as e:
            self.show_custom_message("Error", str(e))

    def delete_book(self):
        delete_window = Toplevel(self.window)
        delete_window.title("Delete Book Record")
        delete_window.configure(bg=self.bg_color)

        Label(delete_window, text="Enter Book ID to Delete:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        book_id_entry = Entry(delete_window, font=self.label_font)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        Button(delete_window, text="Delete", command=lambda: self.remove_book(book_id_entry.get()), font=self.button_font, bg=self.button_color, fg="white").grid(row=0, column=2, padx=10)

    def remove_book(self, book_id):
        try:
            self.mycursor.execute("DELETE FROM Book_Record WHERE BookID=?", (int(book_id),))
            self.conn.commit()
            self.show_custom_message("Success", "Book deleted successfully.")
        except Exception as e:
            self.show_custom_message("Error", str(e))

    def view_book_records(self):
        view_window = Toplevel(self.window)
        view_window.title("View Book Records")
        view_window.configure(bg=self.bg_color)

        self.mycursor.execute("SELECT * FROM Book_Record")
        books = self.mycursor.fetchall()

        listbox = Listbox(view_window, width=80, height=20, bg=self.bg_color, fg=self.text_color, font=self.label_font)
        for book in books:
            listbox.insert(END, f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Quantity: {book[3]}, Price: {book[4]}")

        listbox.pack(pady=20, padx=20)

    def view_purchase_log(self):
        log_window = Toplevel(self.window)
        log_window.title("Purchase Log")
        log_window.configure(bg=self.bg_color)

        self.mycursor.execute("SELECT * FROM PurchaseLog")
        purchases = self.mycursor.fetchall()

        listbox = Listbox(log_window, width=100, height=20, bg=self.bg_color, fg=self.text_color, font=self.label_font)
        for purchase in purchases:
            listbox.insert(END, f"Purchase ID: {purchase[0]}, Customer ID: {purchase[1]}, Book ID: {purchase[2]}, Book Name: {purchase[3]}, Quantity: {purchase[6]}, Price: {purchase[5]}")

        listbox.pack(pady=20, padx=20)

    def search_book_admin(self):
        search_window = Toplevel(self.window)
        search_window.title("Search Book by ID")
        search_window.configure(bg=self.bg_color)

        Label(search_window, text="Enter Book ID:", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        book_id_entry = Entry(search_window, font=self.label_font)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        Button(search_window, text="Search", command=lambda: self.search_book(book_id_entry.get(), search_window), font=self.button_font, bg=self.button_color, fg="white").grid(row=0, column=2, padx=10)

    def search_book(self, book_id, window):
        self.mycursor.execute("SELECT * FROM Book_Record WHERE BookID=?", (int(book_id),))
        book = self.mycursor.fetchone()

        if book:
            Label(window, text=f"Book ID: {book[0]}", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, columnspan=2, pady=10)
            Label(window, text=f"Book Name: {book[1]}", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, columnspan=2, pady=10)
            Label(window, text=f"Author: {book[2]}", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=3, column=0, columnspan=2, pady=10)
            Label(window, text=f"Quantity: {book[3]}", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=4, column=0, columnspan=2, pady=10)
            Label(window, text=f"Price: {book[4]}", font=self.label_font, bg=self.bg_color, fg=self.text_color).grid(row=5, column=0, columnspan=2, pady=10)
        else:
            self.show_custom_message("Error", "No book found with this ID.")

    def show_custom_message(self, title, message):
        """Show a custom message box."""
        messagebox.showinfo(title, message)
