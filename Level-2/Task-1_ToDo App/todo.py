import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} [{status}]")
    print()


def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as done.\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully.\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
