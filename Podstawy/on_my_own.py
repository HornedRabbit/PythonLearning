import requests
import json

#function blocks

def count_task_completion_per_user(tasks):
    completedTasksByUserId = dict()
    for item in tasks:
        if (item["completed"] == True):
            try:
                completedTasksByUserId[item["userId"]] += 1    
            except KeyError:
                completedTasksByUserId[item["userId"]] = 1
                
    return completedTasksByUserId


def get_keys_with_top_values(my_dict):
    return[
            item
            for (item, value) in my_dict.items()
            if value  == max(my_dict.values())
           ]
        
#main fucntion        


r = requests.get("https://jsonplaceholder.typicode.com/todos")

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong data format.")
else:
    ammountOfTasksCompletedPerUserID = count_task_completion_per_user(tasks)
    usersWithMostTasksCompleted = get_keys_with_top_values(ammountOfTasksCompletedPerUserID)     
