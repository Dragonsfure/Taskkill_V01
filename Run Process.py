import os
import subprocess

EXECONST = ".exe"

#The Class for a Task-Item	
class TaskItem: 
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def __str__(self):
        return("Name: "+str(self.name)+"\nIndex: "+str(self.index) +"\n")

def GetTaskList():
	#Gets the Items
	tasks = os.popen('tasklist').readlines() 
	#Creates empty Task-List
	newTasks = []

	for i in tasks:
		if EXECONST in i:
			newTasks.append(i.split(EXECONST)[0] +EXECONST)

	newTasks = list(dict.fromkeys(newTasks))
	newTasks.sort()

	tasks.clear()
	i =0

	for item in newTasks:
		tasks.append(TaskItem(item,i))
		i+=1

	return tasks

taskList = GetTaskList()
for x in taskList:
	print(x)

index = int(input("Press index: "))

st = f"taskkill /f /im {taskList[index].name}"

y = taskList[index].name.split(EXECONST)[0]




paths = subprocess.Popen(['powershell.exe',f' Get-Process {y} | Select-Object Path'],stdout=subprocess.PIPE).communicate()

string = ""
for item in paths[0]:
	string  = string + chr(item)

paths = string.split("\r\n")

print(paths)

os.popen(st)
print(st + "\nGot executed\n")


input("Press Enter to continue...")