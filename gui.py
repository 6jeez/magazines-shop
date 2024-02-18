import tkinter as tk
from tkinter import messagebox
from database import DatabaseManager


class JournalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adding a magazine")
        self.root.configure(bg="#333333")
        
        self.db_manager = DatabaseManager("journals.db")

        self.create_widgets()

    def create_widgets(self):
        fg_color = "white"
        
        self.label_title = tk.Label(self.root, text="Title:", bg="#333333", fg=fg_color)
        self.label_title.grid(row=0, column=0, padx=5, pady=5)

        self.entry_title = tk.Entry(self.root)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5)

        self.label_content = tk.Label(self.root, text="Content:", bg="#333333", fg=fg_color)
        self.label_content.grid(row=1, column=0, padx=5, pady=5)

        self.entry_content = tk.Entry(self.root)
        self.entry_content.grid(row=1, column=1, padx=5, pady=5)

        self.label_price = tk.Label(self.root, text="Price:", bg="#333333", fg=fg_color)
        self.label_price.grid(row=2, column=0, padx=5, pady=5)

        self.entry_price = tk.Entry(self.root)
        self.entry_price.grid(row=2, column=1, padx=5, pady=5)

        self.btn_add = tk.Button(self.root, text="Add", bg="#555555", fg=fg_color)
        self.btn_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


def main():
    root = tk.Tk()
    gui = JournalGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
