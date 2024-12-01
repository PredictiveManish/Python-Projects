def main():
    tasks =[]
    
    while True:
        print("To-Do Task app options: \n")
        print("1. Add Tasks")
        print("2. Show complete task list.")
        print("3. Mark Task as done.")
        print("4. Delete a task")
        print("5. Clear list.")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice=='1':
            print()
            n_tasks = int(input("How much tasks you want to add? "))
            
            for n in range(n_tasks):
                task = input("Enter your task: ")
                tasks.append({"task": task, "done": False})
                print("------------\nTasks added!")
                print("------------")
        elif choice=='2':
            if len(tasks)==0:
                print("You have no tasks as of now.")
            else:
                print("------------------------------------------------------------------\nTasks: ")
                for index, task in enumerate(tasks):
                    status = "Done." if task["done"] else "Not done."
                    print(f"{index + 1}. {task['task']} - {status}")
                print("------------------------------------------------------------------")
                
            
        elif choice=='3':
            task_index = int(input("Enter the task number: "))
            if 0<=task_index<len(tasks):
                tasks[task_index]["done"]=True
                print("-----\nTask Marked as done.\n")
                print("------------\n")
            else:
                print("------------\nSelected task is invalid!")
                print("------------")
        elif choice=='4':
            print(tasks)
            task_to_delete = int(input("Enter the task index you want to delete: "))
            tasks.pop(task_to_delete - 1)
            print("------------\nTask deleted successfully!")
            print("------------")
        elif choice=='5':
            print("Do you genuinely want to delete all tasks?")
            yesno = int(input("Enter 1 for yes and 2 for no: "))
            if yesno ==2:
                choice
            elif yesno ==1:
                tasks.clear()
                print("-----------\nYour task list has been cleared./n Thanks")
                print("------------")
        elif choice=='6':
            exit()
        else:
            print("Invalid choice selection. Please try again.")
            
if __name__ == "__main__":
    main()   
        
                
            
                        
                
                            
                
            
            
        
    