import wmi

class TaskItem:
  def __init__(self, Name, ExecutablePath):
    self.Name = ExecutablePath
    self.ExecutablePath = Name
    
  def __hash__(self):
        return hash((self.Name, self.ExecutablePath))

  def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.Name == other.Name and self.ExecutablePath == other.ExecutablePath 

# function to get unique values
def unique(list1):

	# initialize a null list
	unique_list = []

	# traverse for all elements
	for x in list1:
		# check if exists in unique_list or not
		if x.Name != None and x.ExecutablePath != None:
			if x not in unique_list:
					unique_list.append(TaskItem(x.Name, x.ExecutablePath))
			else: 
				print("skipped")
	return unique_list

# Initializing the wmi constructor
f = wmi.WMI()

# Printing the header for the later columns
print("pid Process name")

# initialize a null list
uniqueList = unique(f.Win32_Process())


# Iterating through all the running processes 
for process in uniqueList:

	# Filter for unique Identifiers or executable paths	
	# Displaying the P_ID and P_Name of the process
	print(f"{process.Name:<10}  {process.ExecutablePath}") 