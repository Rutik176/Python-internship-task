from tkinter import *
from tkinter import messagebox, simpledialog

class ToDoListApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x400")

        self.tasks = []

        self.task_listbox = Listbox(self, selectmode=SINGLE, font=('Arial', 12))
        self.task_listbox.pack(fill=BOTH, expand=True)

        self.add_task_entry = Entry(self, font=('Arial', 12))
        self.add_task_entry.pack(pady=10)

        self.add_task_button = Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.edit_task_button = Button(self, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack(pady=5)

        self.delete_task_button = Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.mark_completed_button = Button(self, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.pack(pady=5)

    def add_task(self):
        task = self.add_task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.add_task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=self.tasks[selected_task_index])
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            self.tasks[selected_task_index] += " (Completed)"
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)

if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()
