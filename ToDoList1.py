def taskaddition():
    n=int(input("Enter no of task you want to add: "))
    
    for i in range(n):
        T=input("Enter your task")
        T1.append(T)
    print("**Tasks are added successfully**")    
    return T1    
def taskdisplay():
    if len(T1)==0:
        print("List is empty")
        choice1=input("Do you want to add task? yes or no")
        if choice1=='yes':
            s=taskaddition()
            print("Below are the task details: \n",s)
        elif choice1=='no':
            print("Thank yosu:")
            exit
    else:
        return T1
def taskremove():
    if len(T1)==0:
        print("List is empty")
    else:
        choice3=int(input("Enter the number of tasks you want to delete from below tasks: "))
        if len(taskdisplay())>=choice3:
            print(taskdisplay())
            for i in range(choice3):
                a=input()
                if a in T1:
                    T1.remove(a)
                    print("Tasks are removed successfully and rest of tasks are",T1)
                else:
                    print("Task doesn't exists")
        else:
            print("Length of delete task must be less than ",len(taskdisplay()))
                    
            
        exit
        

    

if __name__=='__main__':
    T1=[]
    while True:
        print("1.Task Addition\n2.Task display \n3.Task Remove\n")
        choice=input("Enter your choice (1-3):")
        if choice=='1':
            taskaddition()
            exit
        elif choice=='2':
            taskdisplay()
            exit
        elif choice=='3':
            taskremove()
            exit
            
    else:
        exit
        
        
        
            
        
        
