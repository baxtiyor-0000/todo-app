from datetime import datetime

def add_task(tasks):
    title = input("Enter task title: ")
    if title in tasks:
        print("Task with this title already exists.")
        return
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    tasks[title] = {
        "description": description,
        "due_date": due_date,
        "status": "Pending"
    }
    print("Task added successfully.")

def remove_task(tasks):
    title = input("Enter the title of the task to remove: ")
    if title in tasks:
        del tasks[title]
        print("Task removed successfully.")
    else:
        print("Task not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    for title, details in tasks.items():
        print(f"Title: {title}")
        print(f"Description: {details['description']}")
        print(f"Due Date: {details['due_date'].strftime('%Y-%m-%d')}")
        print(f"Status: {details['status']}")
        print("-" * 30)

def sort_by_due_date(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    sorted_tasks = sorted(tasks.items(), key=lambda item: item[1]['due_date'])
    for title, details in sorted_tasks:
        print(f"Title: {title}")
        print(f"Description: {details['description']}")
        print(f"Due Date: {details['due_date'].strftime('%Y-%m-%d')}")
        print(f"Status: {details['status']}")
        print("-" * 30)

def search_task(tasks):
    search_query = input("Enter title to search: ").lower()
    found_tasks = {title: details for title, details in tasks.items() if search_query in title.lower()}
    if found_tasks:
        for title, details in found_tasks.items():
            print(f"Title: {title}")
            print(f"Description: {details['description']}")
            print(f"Due Date: {details['due_date'].strftime('%Y-%m-%d')}")
            print(f"Status: {details['status']}")
            print("-" * 30)
    else:
        print("No tasks found.")

def display_overdue_tasks(tasks):
    current_date = datetime.now()
    overdue_tasks = {title: details for title, details in tasks.items() if details['due_date'] < current_date and details['status'] == "Pending"}
    if overdue_tasks:
        for title, details in overdue_tasks.items():
            details['status'] = "Failed"
            print(f"Title: {title}")
            print(f"Description: {details['description']}")
            print(f"Due Date: {details['due_date'].strftime('%Y-%m-%d')}")
            print(f"Status: {details['status']}")
            print("-" * 30)
    else:
        print("No overdue tasks.")

def mark_task_as_completed(tasks):
    title = input("Enter the title of the task to mark as completed: ")
    if title in tasks:
        tasks[title]['status'] = "Completed"
        print("Task marked as completed.")
    else:
        print("Task not found.")

def main():
    tasks = {}
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Sort by Due Date")
        print("5. Search Task")
        print("6. Display Overdue Tasks")
        print("7. Mark Task as Completed")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            sort_by_due_date(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            display_overdue_tasks(tasks)
        elif choice == "7":
            mark_task_as_completed(tasks)
        elif choice == "8":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
