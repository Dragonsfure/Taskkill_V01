import os
import subprocess

# Constant to find all ".exe"-Processes 
# This should be an REGEX Thing for better use :D 
EXECONST = ".exe"

#The Class for a Task-Item	
class TaskItem: 
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def __str__(self):
        return("Name: "+str(self.name)+"\nIndex: "+str(self.index) +"\n")

def GetTaskList():
	#Gets the Items from Shell-Command 
	tasks = os.popen('tasklist').readlines() 
	#Creates empty Task-List
	newTasks = []

	for i in tasks:
		if EXECONST in i:
			newTasks.append(i.split(EXECONST)[0] +EXECONST)

	newTasks = list(dict.fromkeys(newTasks))
	newTasks.sort()

	# Reuses the Variable by clearing it before
	tasks.clear()
	i =0

	for item in newTasks:
		tasks.append(TaskItem(item,i))
		i+=1

	# Returns a List of Tasks with their Index and Names
	return tasks

# Gets the list of Tasks that are currently running. 
taskList = GetTaskList()
for x in taskList:
	print(x)

# Asks for the specific Task Selection
index = int(input("Press index: "))

# Creates the Command in extra Variable for easier Debugging
st = f"taskkill /f /im {taskList[index].name}"

# Gets the specific name of the the Process 
y = taskList[index].name.split(EXECONST)[0]


# Opens a Cmd and changes it to a powershell-shell
# Selects a process with the corresponding name and the Object-path
# Gains a list of items as result    
paths = subprocess.Popen(['powershell.exe',f' Get-Process {y} | Select-Object Path'],stdout=subprocess.PIPE).communicate()

# Uses this list to make an String for it, to then split it and get the names of the process for later use
string = ""
for item in paths[0]:
	string  = string + chr(item)

paths = string.split("\r\n")

# Prints the paths of the Process before killing it with the predefined command in st-variable
print(paths)
os.popen(st)
print(st + "\nGot executed\n")

# To not close the Shell instantly
input("Press Enter to continue...")


# Here the Paths should be used to restart the closed programm with the paths :D
# If it got started one time already it continues with the next one, or at least should, if i wasn't to lazy to implement it LOL