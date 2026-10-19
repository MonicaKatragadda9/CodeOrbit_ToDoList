
# CodeOrbit Tech - To-Do List CLI App
# This program allows users to add, view, remove, and save tasks.

# Store all tasks in a list
tasks = []

# Load previously saved tasks from a text file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        # The file will be created when tasks are saved
        pass

# Save all tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task():
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

# Display all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Remove a task using its number
def remove_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter the task number to remove: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks()
                print("Removed task:", removed)
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

# Main menu of the application
def main():
    load_tasks()

    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

# Start the program
if __name__ == "__main__":
    main()
