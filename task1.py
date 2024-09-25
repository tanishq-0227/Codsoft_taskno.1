tasks=[]

def addTask():
    task=input("Please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks:")
        for index,task in enumerate(tasks):
            print(f"Task #{index}. {task}")

    
def deleteTask():
    listTasks()
    try:
        task_dlt = int(input("Enter the # to delete:"))
        if task_dlt>=0 and task_dlt < len(tasks):
            tasks.pop(task_dlt)
            print(f"Task {task_dlt} has been removed.")

        else:
            print(f" Task # {task_dlt} was not found.")
    except:
        print("Invalid input.")
            
    

if __name__ == "__main__":
    print ("Welcome to the To Do List Application")
    while True:
        print("\n")
        print("----------------------------------")
        print("Please Select one of the following options:-")
        print("1. Add a new task.")
        print("2. Delete a task.")
        print("3. List task.")
        print("4. Exit.")

        choice =input("Enter your choice:-")

        if (choice=="1"):
            addTask()

        elif (choice=="2"):
            deleteTask()

        elif (choice=="3"):
            listTasks()

        elif (choice=="4"):
            break
        else:
            print("Invalid choice. Please try again...")
            
    print ("GoodBye...")