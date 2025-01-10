
import csv
import os
import sys

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

# Definición de la clase Task
class Task:
    def __init__(self, description, status="Pending"):
        self.description = description
        self.status = status

    def mark_completed(self):
        self.status = "Completed"
    
    def mark_in_progress(self):
        self.status = "In Progress"

    def __str__(self):
        return f"{self.description} [{self.status}]"

# Clase ToDoList para manejar las tareas
class ToDoList:
    def __init__(self, file_name="tasks.csv"):
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, mode='r') as file:
                reader = csv.reader(file)
                self.tasks = [Task(description, status) for description, status in reader]

    def save_tasks(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.description, task.status])

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                self.save_tasks()
                return
        raise ValueError("Task not found")
    
    def mark_task_in_progress(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_in_progress()
                self.save_tasks()
                return
        raise ValueError("Task not found")
    def update_task(self, description, new_description):
        for task in self.tasks:
            if task.description == description:
                task.description = new_description
                self.save_tasks()
                return
        raise ValueError("Task not found")

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()

# Código principal para probar la funcionalidad
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            clear_screen()
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            clear_screen()
            tasks = todo_list.list_tasks()
            for task in tasks:
                print(task)
        elif choice == "3":
            description = input("Enter the task description to mark as completed: ")
            try:
                todo_list.mark_task_completed(description)
            except ValueError as e:
                print(e)
        elif choice == "4":
            clear_screen()
            todo_list.clear_tasks()
            print("All tasks cleared.")
        elif choice == "5":
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")
