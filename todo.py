tasks = []

def add_task(task):
    tasks.append(task)
    #print("Task added")

def view_tasks():
    for i, task in enumerate(tasks):
        #print(i+1, task)
        
def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    
    print("Task added successfully")
    
# Main branch change

# Feature change 1
# Feature change 2
# Another main change
# temp1
# temp2
# temp3
