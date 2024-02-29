todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")

def remove_task(task_number):
    if task_number<=len(todo_list)-1:
        todo_list.pop(task_number)
        print("Task removed successfully!")
    else:
        print("Task number not found!")

def display_list():
    if todo_list:
        print("To-Do List:")
        task_number = 0
        for task in todo_list:
            print(f"{task_number+1}. {task}")
            task_number += 1
    else:
        print("To-Do List is empty.")

while True:
    print("\n===== To-Do List Manager =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display List")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        for i in range(len(todo_list)):
            print(f"{i+1}. {todo_list[i]}")
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number-1)
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Thank you for using To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
