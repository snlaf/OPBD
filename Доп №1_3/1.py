import customtkinter as ctk
from tkinter import messagebox
from CTkListbox import *

class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Login")
        self.geometry("200x150")

        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack()
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack()

        self.login_button = ctk.CTkButton(self, text="Login", command=self.on_login)
        self.login_button.pack()

    def on_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            self.master.show_main_window()
            self.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.login_window = LoginWindow(self)
        self.login_window.lift()

        self.task_list = []
        self.main_window = None

    def show_main_window(self):
        self.main_window = MainWindow(self)
        self.deiconify()

class MainWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Task Manager")
        self.geometry("400x500")

        self.task_entry = ctk.CTkEntry(self)
        self.task_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Добавить", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(pady=5, fill="both", expand=True)

        self.task_scrollable_frame = ctk.CTkScrollableFrame(self.task_frame)
        self.task_scrollable_frame.pack(pady=5, fill="both", expand=True)

        self.task_listbox = CTkListbox(self.task_scrollable_frame)
        self.task_listbox.pack(pady=5, fill="both", expand=True)

        self.complete_button = ctk.CTkButton(self, text="Завершить", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(self, text="Убрать", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(ctk.END, task)
            self.task_entry.delete(0, ctk.END)

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.task_listbox.get(selected)
            self.task_listbox.delete(selected)
            self.task_listbox.insert(ctk.END, f"✔ {task}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()