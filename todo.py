import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


def add_task(task_description):
    tasks = load_tasks()
    task = {"description": task_description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Task list is empty.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✖"
            print(f"{i}. {task['description']} [{status}]")


def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\n1. Add Task\n2. View All Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Select an action: ")
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to complete: "))
            complete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()