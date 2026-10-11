def view_tasks(task_list):
    """Handles the DISPLAY (View) portion of the IPO model."""
    print("\n--- Current To-Do List ---")
    if not task_list:
        print("Your list is empty.")
    else:
        # Using enumerate() for simultaneous access to Index and Value
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
    print("--------------------------\n")
 
def main():
    my_tasks = []
 
    print("DecodeLabs To-Do List Initialized.")
 
    while True:
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Exit")
 
        choice = input("Select an option (1-3): ")
 
        if choice == '1':
            new_task = input("Enter the task (e.g., 'Finish Python assignment'): ").strip()
            if new_task:
                my_tasks.append(new_task)
                print(f"Task '{new_task}' added.")
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            view_tasks(my_tasks)
        elif choice == '3':
            print("Process Terminated. Remember: RAM is volatile = Data Lost!")
            break
        else:
            print("Invalid input. Please try again.")
 
if __name__ == "__main__":
    main()
 
