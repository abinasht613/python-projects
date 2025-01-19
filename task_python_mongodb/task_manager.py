from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.task_management #db
tasks_collection = db.tasks # collection

# Function to add a new task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks_collection.insert_one(task)
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    print("\n--- All Tasks ---")
    tasks = tasks_collection.find()
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['_id']}, Title: {task['title']}, Status: {status}")

# Function to mark a task as complete
def complete_task():
    task_id = input("Enter task ID to mark as complete: ")
    result = tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})
    if result.matched_count > 0:
        print("Task marked as completed!")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task():
    try:
        task_id = input("Enter task ID to delete: ")
        result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
        print(result)
        if result.deleted_count > 0:
            print("Task deleted!")
        else:
            print("Task not found.")
    except Exception as e:
        print("Error:", e)

# Main Menu
def main_menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
