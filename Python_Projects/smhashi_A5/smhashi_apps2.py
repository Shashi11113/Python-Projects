# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, A5

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks yet! Use option 2 to add a new task.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print(f"\nTotal tasks: {len(tasks)}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    while True:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully.")
                break
            else:
                print("Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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
