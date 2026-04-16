tasks=[]

tasks.append("study")
tasks.append("exercise")
tasks.append("sleep")

tasks[1] = "play" #update tasks
tasks.remove("sleep")#remove task
tasks.sort()#sort tasks

tasks_tuple = tuple(tasks)

for t in tasks_tuple:
    print(t)
