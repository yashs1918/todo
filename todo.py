# Simple To-Do List Program in Python

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("\nEnter the task title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['title']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
