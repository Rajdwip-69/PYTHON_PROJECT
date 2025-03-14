
tasks = [] 
def task():
  
    print("-----Welcome to the Task Management App-----")

total_task=int(input("Enter how many task you want to do ="))
for i in range(1,total_task+1):
    task_name=input(f"Enter task{i} =")
    tasks.append(task_name)


print(f"Todays tasks are {tasks}")
while True:
    operation=int(input("1-Add\n2-Update\n3-Delete\n4-View\n3-Stop \n Enter Which you want to perfrom :"))
    if operation == 1:
        add=input("Enter task you want to add =")
        tasks.append(add)
        print(f"Task{add} has been sucessfully added...")
    elif operation == 2:
        upadate_val = input("Enter the task you want to upadte= ")
        if upadate_val in tasks:
            up=input("Enter new task =")
            ind = tasks.index(upadate_val)
            tasks[ind] = up
            print(f"Updated task {up}")
    elif operation == 3:
        del_val = input("Which task you want to delete =")
        if del_val in tasks:
            ind = tasks.index(del_val)
            del tasks[ind]
            print(f"Task{del_val} has been deleted...")

    elif operation ==4:
        print(f"Total tasks= {tasks}")

    elif operation == 5:
        print("Closing the Program...")
        break

    else:
        print("Invalid Input")