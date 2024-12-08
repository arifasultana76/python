# To-Do App
tasks = {}

def add_task(task_id, task_name):
    tasks[task_id] = {"task": task_name, "completed": False}
    print(f"Task '{task_name}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available!")
        return
    for task_id, details in tasks.items():
        status = "Completed" if details["completed"] else "Pending"
        print(f"{task_id}: {details['task']} [{status}]")

def mark_complete(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"Task '{tasks[task_id]['task']}' marked as completed!")
    else:
        print("Task not found!")

def delete_task(task_id):
    if task_id in tasks:
        removed_task = tasks.pop(task_id)
        print(f"Task '{removed_task['task']}' deleted successfully!")
    else:
        print("Task not found!")

def main():
    while True:
        print("\nTo-Do App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task_id = input("Enter task ID: ")
            task_name = input("Enter task name: ")
            add_task(task_id, task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = input("Enter task ID to mark as complete: ")
            mark_complete(task_id)
        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()