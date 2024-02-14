#Create a project management class where you will manage the resources, the tasks maintained by them
#Also display the skills possessed by the resource.
#Use dictionaries, lists and class appropraiately.

from datetime import *

class Project_Management:
    def __init__(self, name, startdate, enddate):
        self.name = name
        self.startdate = startdate
        self.enddate = enddate
        self.tasks = []

    def addTasks(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        # tasks can have multiple resources. Hence defining as lists
        self.resources = []

    def addResource(self, resource):
        self.resources.append(resource)


class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


P1 = Project_Management("AI",date(2022,11,1),date(2022,11,1))
task = Task("Create BOT",90)
resource = Resource("John","Python")
task.addResource(resource)
P1.addTasks(task)

# to print the tasks in project
for eachtask in P1.tasks:
    print("The task is:",eachtask.name)
    print("The duration of the task is:",eachtask.duration)
    for eachResource in task.resources:
        print("The resource name is:",eachResource.name)
        print("The skill possessed by the resource is :",eachResource.skill)
