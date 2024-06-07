import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("550x550")

        self.tasks = []

        self.task_entry = tk.Entry(root)
        self.task_entry.configure(width=13,font="helvetica 35 bold",fg="white",bg="cyan")
        self.task_entry.pack(pady=10,padx=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.configure(font="helvetica 35 bold",bd=5,bg="yellow")
        self.add_button.pack(padx=23,pady=20)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.configure(font="helvetica 35 bold",bd=5,bg="yellow")
        self.remove_button.pack(padx=23,pady=20)

        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks)
        self.show_button.configure(font="helvetica 35 bold",bd=5,bg="yellow")
        self.show_button.pack(padx=23,pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Success", f"Task '{task}' added to the list.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty.")

    def remove_task(self):
        task = self.task_entry.get()
        if task in self.tasks:
            self.tasks.remove(task)
            messagebox.showinfo("Success", f"Task '{task}' removed from the list.")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Task '{task}' not found in the list.")

    def show_tasks(self):
        if self.tasks:
            tasks_text = "\n".join(self.tasks)
            messagebox.showinfo("Tasks", f"Tasks:\n{tasks_text}")
        else:
            messagebox.showinfo("Tasks", "No tasks in the list.")

def main():
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()