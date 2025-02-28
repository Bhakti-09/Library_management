import tkinter as tk
from tkinter import messagebox

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book_info = {"title": title, "author": author, "isbn": isbn}
        self.books.append(book_info)

    def display_books(self):
        result_listbox.delete(0, tk.END)
        if self.books:
            for i, book in enumerate(self.books, start=1):
                result_listbox.insert(tk.END, f"ID: {i}, Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        else:
            messagebox.showinfo("Info", "The library is empty.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book["title"].lower()]
        result_listbox.delete(0, tk.END)
        if found_books:
            for i, book in enumerate(found_books, start=1):
                result_listbox.insert(tk.END, f"ID: {i}, Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        else:
            messagebox.showinfo("Info", "No books found with that title.")

    def remove_book(self, index):
        if 0 <= index < len(self.books):
            del self.books[index]
            messagebox.showinfo("Info", "Book removed successfully.")
        else:
            messagebox.showwarning("Warning", "Invalid book ID.")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    if title and author and isbn:
        library.add_book(title, author, isbn)
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        isbn_entry.delete(0, tk.END)
        library.display_books()
    else:
        messagebox.showwarning("Warning", "Please fill in all the fields.")

def search():
    title = search_entry.get()
    if title:
        result_listbox.delete(0, tk.END)
        library.search_book(title)
    else:
        messagebox.showwarning("Warning", "Please enter a title to search for.")

def remove_book():
    selected_book = result_listbox.get(result_listbox.curselection())
    if selected_book:
        try:
            book_id = int(selected_book.split("ID: ")[1].split(",")[0]) - 1
            library.remove_book(book_id)
            library.display_books()
        except ValueError:
            messagebox.showwarning("Warning", "Invalid book ID.")

def display_books():
    library.display_books()

root = tk.Tk()
root.title("Library Management System")
root.geometry("700x600")  # Increase the size of the window
root.configure(bg="#87CEFF")
library = Library()

# Create and pack widgets
title_label = tk.Label(root, text="Title:", font=("Arial", 14), bg="orange")
author_label = tk.Label(root, text="Author:", font=("Arial", 14), bg="Orange")
isbn_label = tk.Label(root, text="ISBN:", font=("Arial", 14), bg="Orange")
title_entry = tk.Entry(root, width=40, bg="gray")
author_entry = tk.Entry(root, width=40, bg="Gray")
isbn_entry = tk.Entry(root, width=40, bg="gray")
add_button = tk.Button(root, text="Add Book", command=add_book, font=("Arial", 14), padx=10, bg="Red")
search_label = tk.Label(root, text="Search by Title:", font=("Arial", 14), bg="Orange")
search_entry = tk.Entry(root, width=40, bg="Gray")
search_button = tk.Button(root, text="Search", command=search, font=("Arial", 14), padx=10, bg="Red")
result_listbox = tk.Listbox(root, height=20, width=40, bg="Gray")
remove_button = tk.Button(root, text="Remove Book", command=remove_book, font=("Arial", 14), padx=10, bg="Red")
display_button = tk.Button(root, text="Display Books", command=display_books, font=("Arial", 14), padx=10, bg="Red")

title_label.pack()
title_entry.pack()
author_label.pack()
author_entry.pack()
isbn_label.pack()
isbn_entry.pack()
add_button.pack()
search_label.pack()
search_entry.pack()
search_button.pack()
display_button.pack()
result_listbox.pack()
remove_button.pack()

root.mainloop()
