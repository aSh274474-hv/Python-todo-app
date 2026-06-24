todo_list = []

# Load tasks from file
try:
    with open("tdl.txt", "r") as file:
        todo_list = [line.strip() for line in file]

except FileNotFoundError:
    pass

deleted_tasks = 0

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Exit")

    choice = input("Choose task (1-5): ")

    # Add Task
    if choice == "1":
        task = input("Add task: ")
        todo_list.append(task)

        with open("tdl.txt", "w") as file:
            for item in todo_list:
                file.write(item + "\n")

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks found!")

        else:
            for number, task in enumerate(todo_list, start=1):
                print(number, task)

    # Delete Task
    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to delete!")

        else:
            for number, task in enumerate(todo_list, start=1):
                print(number, task)

            task_no = int(input("Enter task number: "))

            if 1 <= task_no <= len(todo_list):
                removed_item = todo_list.pop(task_no - 1)

                deleted_tasks += 1

                with open("tdl.txt", "w") as file:
                    for item in todo_list:
                        file.write(item + "\n")

                print("Deleted Task:", removed_item)

            else:
                print("Invalid task number!")

    # Search Task
    elif choice == "4":
        search = input("Search task: ")

        found = False

        for task in todo_list:
            if search.lower() in task.lower():
                print("Found:", task)
                found = True

        if not found:
            print("Task not found!")

    # Exit
    elif choice == "5":
        print("\n===== STATS =====")
        print("Total Tasks:", len(todo_list))
        print("Deleted Tasks:", deleted_tasks)
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
