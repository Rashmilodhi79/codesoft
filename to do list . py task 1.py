# To-Do List Application

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    
# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty!")

# Function to delete a task
def delete_task(tasks):
    if tasks:
        view_tasks(tasks)
        try:
            task_number = int(input("Enter the number of the task to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Your to-do list is empty!")

# Main function to run the To-Do List application
def main():
    tasks = []  # List to store tasks
    while True:
        display_menu()
        
        # Get user input for menu choice
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Run the application
if __name__ == "__main__":
    main()
