import tkinter as tk
from tkinter import Toplevel, Listbox, Scrollbar, Entry, Button, Label, messagebox

class Customer:
    def __init__(self, window, mycursor, conn, main_app):
        self.window = window
        self.mycursor = mycursor
        self.conn = conn
        self.main_app = main_app
        self.cart_items = []
        self.customer_id = ""

    def show_menu(self):
        """Display the customer menu."""
        self.clear_window()

        shop_frame = tk.Frame(self.window, bg="#e0f7fa")
        shop_frame.pack(pady=50, padx=50, fill="both", expand=True)

        tk.Label(shop_frame, text="Welcome to the Shop", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        tk.Button(shop_frame, text="Browse Books", command=self.browse_books, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10, fill="x")
        tk.Button(shop_frame, text="Search Books by Title", command=self.search_books_by_title, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10, fill="x")
        tk.Button(shop_frame, text="Search Books by Author", command=self.search_books_by_author, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10, fill="x")
        tk.Button(shop_frame, text="View Cart", command=self.view_cart, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10, fill="x")
        tk.Button(shop_frame, text="Back to Main Menu", command=self.go_back_to_main_menu, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10, fill="x")

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.window.winfo_children():
            widget.destroy()

    def go_back_to_main_menu(self):
        """Clear current window and return to the main menu."""
        self.clear_window()
        self.main_app.create_widgets()  # Call create_widgets to set up the main menu

    def browse_books(self):
        """Open window to browse books."""
        browse_window = Toplevel(self.window)
        browse_window.title("Browse Books")
        browse_window.geometry("600x500")  # Increased window size
        browse_window.configure(bg="#e0f7fa")

        tk.Label(browse_window, text="Browse Books", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        self.books_listbox = Listbox(browse_window, font=("Arial", 14), height=20)
        self.books_listbox.pack(pady=10, fill="both", expand=True)
        self.load_books(self.books_listbox)

        scroll = Scrollbar(browse_window, orient=tk.VERTICAL, command=self.books_listbox.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.books_listbox.config(yscrollcommand=scroll.set)

        self.select_button = tk.Button(browse_window, text="Select Book", command=lambda: self.select_book(self.books_listbox, browse_window), font=("Arial", 14), bg="#00796b", fg="white")
        self.select_button.pack(pady=10)

    def load_books(self, listbox):
        """Load books into the listbox."""
        listbox.delete(0, tk.END)
        self.mycursor.execute("SELECT * FROM Book_Record")
        books = self.mycursor.fetchall()
        for book in books:
            listbox.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[4]:.2f}, Quantity: {book[3]}")

    def search_books_by_title(self):
        """Open window to search for books by title."""
        search_window = Toplevel(self.window)
        search_window.title("Search Books by Title")
        search_window.geometry("600x500")  # Increased window size
        search_window.configure(bg="#e0f7fa")

        tk.Label(search_window, text="Search Books by Title", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        tk.Label(search_window, text="Search by Title:", font=("Arial", 14), bg="#e0f7fa", fg="#004d40").pack(pady=5)
        self.search_title_entry = Entry(search_window, font=("Arial", 14))
        self.search_title_entry.pack(pady=5)

        tk.Button(search_window, text="Search", command=self.perform_search_by_title, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=20)

        self.search_results_listbox = Listbox(search_window, font=("Arial", 14), height=10)
        self.search_results_listbox.pack(pady=10, fill="both", expand=True)

        self.select_button = tk.Button(search_window, text="Select Book", command=lambda: self.select_book(self.search_results_listbox, search_window), font=("Arial", 14), bg="#00796b", fg="white")
        self.select_button.pack(pady=10)

    def search_books_by_author(self):
        """Open window to search for books by author."""
        search_window = Toplevel(self.window)
        search_window.title("Search Books by Author")
        search_window.geometry("600x500")  # Increased window size
        search_window.configure(bg="#e0f7fa")

        tk.Label(search_window, text="Search Books by Author", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        tk.Label(search_window, text="Search by Author:", font=("Arial", 14), bg="#e0f7fa", fg="#004d40").pack(pady=5)
        self.search_author_entry = Entry(search_window, font=("Arial", 14))
        self.search_author_entry.pack(pady=5)

        tk.Button(search_window, text="Search", command=self.perform_search_by_author, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=20)

        self.search_results_listbox = Listbox(search_window, font=("Arial", 14), height=10)
        self.search_results_listbox.pack(pady=10, fill="both", expand=True)

        self.select_button = tk.Button(search_window, text="Select Book", command=lambda: self.select_book(self.search_results_listbox, search_window), font=("Arial", 14), bg="#00796b", fg="white")
        self.select_button.pack(pady=10)

    def perform_search_by_title(self):
        """Perform search based on title."""
        title = self.search_title_entry.get()

        query = "SELECT * FROM Book_Record WHERE Bookname LIKE ?"
        params = [f"%{title}%"]

        self.mycursor.execute(query, params)
        books = self.mycursor.fetchall()

        self.search_results_listbox.delete(0, tk.END)
        for book in books:
            self.search_results_listbox.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[4]:.2f}, Quantity: {book[3]}")

    def perform_search_by_author(self):
        """Perform search based on author."""
        author = self.search_author_entry.get()

        query = "SELECT * FROM Book_Record WHERE Author LIKE ?"
        params = [f"%{author}%"]

        self.mycursor.execute(query, params)
        books = self.mycursor.fetchall()

        self.search_results_listbox.delete(0, tk.END)
        for book in books:
            self.search_results_listbox.insert(tk.END, f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[4]:.2f}, Quantity: {book[3]}")

    def select_book(self, listbox, parent_window):
        """Open window to select quantity and proceed to purchase."""
        selected = listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No book selected.")
            return

        book_info = listbox.get(selected[0])
        book_id = int(book_info.split(",")[0].split(":")[1].strip())
        book_title = book_info.split(",")[1].split(":")[1].strip()

        # Open window to select quantity
        quantity_window = Toplevel(self.window)
        quantity_window.title("Select Quantity")
        quantity_window.geometry("400x200")
        quantity_window.configure(bg="#e0f7fa")

        tk.Label(quantity_window, text=f"Select Quantity for '{book_title}'", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        tk.Label(quantity_window, text="Quantity:", font=("Arial", 14), bg="#e0f7fa", fg="#004d40").pack(pady=5)
        self.quantity_entry = Entry(quantity_window, font=("Arial", 14))
        self.quantity_entry.pack(pady=5)

        tk.Button(quantity_window, text="Add to Cart", command=lambda: self.add_to_cart(book_id, quantity_window, parent_window), font=("Arial", 14), bg="#00796b", fg="white").pack(pady=20)

    def add_to_cart(self, book_id, quantity_window, parent_window):
        """Add selected book and quantity to cart."""
        quantity = self.quantity_entry.get()
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showwarning("Input Error", "Invalid quantity.")
            return

        quantity = int(quantity)

        self.mycursor.execute("SELECT * FROM Book_Record WHERE BookID = ?", (book_id,))
        book = self.mycursor.fetchone()

        if not book:
            messagebox.showerror("Error", "Book not found.")
            return

        if quantity > book[3]:
            messagebox.showwarning("Quantity Error", "Not enough stock available.")
            return

        self.cart_items.append({
            'book_id': book[0],
            'title': book[1],
            'author': book[2],
            'price': book[4],
            'quantity': quantity
        })

        messagebox.showinfo("Success", "Book added to cart.")
        quantity_window.destroy()
        parent_window.destroy()  # Close the parent search window

    def view_cart(self):
        """Open window to view shopping cart."""
        cart_window = Toplevel(self.window)
        cart_window.title("Shopping Cart")
        cart_window.geometry("600x500")  # Increased window size
        cart_window.configure(bg="#e0f7fa")

        tk.Label(cart_window, text="Shopping Cart", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        self.cart_listbox = Listbox(cart_window, font=("Arial", 14), height=20)
        self.cart_listbox.pack(pady=10, fill="both", expand=True)

        for item in self.cart_items:
            self.cart_listbox.insert(tk.END, f"Title: {item['title']}, Author: {item['author']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}")

        tk.Button(cart_window, text="Remove Selected Item", command=self.remove_from_cart, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10)
        tk.Button(cart_window, text="Proceed to Checkout", command=self.checkout, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=10)

    def remove_from_cart(self):
        """Remove selected item from the cart."""
        selected = self.cart_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No item selected.")
            return

        del self.cart_items[selected[0]]
        self.cart_listbox.delete(selected[0])
        messagebox.showinfo("Removed", "Item removed from cart.")

    def checkout(self):
        """Open window to proceed with checkout."""
        checkout_window = Toplevel(self.window)
        checkout_window.title("Checkout")
        checkout_window.geometry("400x250")
        checkout_window.configure(bg="#e0f7fa")

        tk.Label(checkout_window, text="Checkout", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=20)

        tk.Label(checkout_window, text="Customer ID:", font=("Arial", 14), bg="#e0f7fa", fg="#004d40").pack(pady=5)
        self.customer_id_entry = Entry(checkout_window, font=("Arial", 14))
        self.customer_id_entry.pack(pady=5)

        tk.Button(checkout_window, text="Complete Purchase", command=self.complete_purchase, font=("Arial", 14), bg="#00796b", fg="white").pack(pady=20)

    def complete_purchase(self):
        """Complete the purchase process, update book quantities, and log it."""
        customer_id = self.customer_id_entry.get()
        if not customer_id.strip():
            messagebox.showwarning("Input Error", "Customer ID is required.")
            return

        if not self.cart_items:
            messagebox.showwarning("Cart Empty", "Your cart is empty.")
            return

        for item in self.cart_items:
            # Check if the book exists in the database
            self.mycursor.execute("SELECT * FROM Book_Record WHERE BookID = ?", (item['book_id'],))
            book = self.mycursor.fetchone()

            if book:
                if book[3] >= item['quantity']:  # Ensure enough stock is available
                    # Insert purchase log entry
                    self.mycursor.execute("""INSERT INTO PurchaseLog (CustomerID, BookID, Bookname, Author, Price, Quantity)
                    VALUES (?, ?, ?, ?, ?, ?)""", (customer_id, item['book_id'], item['title'], item['author'], item['price'], item['quantity']))

                    # Update book quantity
                    self.mycursor.execute("UPDATE Book_Record SET Quantity = Quantity - ? WHERE BookID = ?", (item['quantity'], item['book_id']))
                else:
                    messagebox.showwarning("Out of Stock", f"The book '{item['title']}' is out of stock or not enough stock available.")
                    self.conn.rollback()
                    return
            else:
                messagebox.showerror("Error", f"Book with ID {item['book_id']} does not exist.")
                self.conn.rollback()
                return

        self.conn.commit()
        self.cart_items.clear()
        messagebox.showinfo("Success", "Purchase completed successfully.")
        self.show_menu()  # Return to the main customer menu
