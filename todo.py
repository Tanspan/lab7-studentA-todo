tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added")

def view_tasks():
    if not tasks:
        print("No tasks")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

while True:
    print("\n1.Add Task 2.View Tasks 3.Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
