import tkinter as tk

class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Учёт задач")
        self.geometry("300x400")

        self.task_list = tk.Listbox(self, height=10, width=30)
        self.task_list.pack(pady=10)

        self.task_entry = tk.Entry(self, width=20)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(self, text="Добавить", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Удалить", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self, text="Завершить", command=self.complete_task)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            self.task_list.delete(selected)

    def complete_task(self):
        selected = self.task_list.curselection()
        if selected:
            task = self.task_list.get(selected)
            self.task_list.delete(selected)
            self.task_list.insert(tk.END, f"✔ {task}")

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()