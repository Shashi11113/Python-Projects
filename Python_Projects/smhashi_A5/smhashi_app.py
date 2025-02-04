# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, A5

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks(tasks):
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid option. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
