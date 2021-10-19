"""

JSONplaceholder - miejsce zastępcze na przyszły JSON

"""

import requests
import json
from collections import defaultdict
r = requests.get("https://jsonplaceholder.typicode.com/todos")

#/////////////////////////////////
def count_task_completion(tasks):
    completedTasksByUser = defaultdict(int) 
    for item in tasks:
        if (item["completed"] == True):
                completedTasksByUser[item["userId"]] += 1

    return completedTasksByUser

#////////////////////////////////
#to samo co niżej tylko bardziej ogólne
def get_keys_with_top_values(my_dict):
    return[
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]


#////////////////////////////////
def get_users_with_most_completed_tasks(completedTasksByUser):
    highestAmmountOfCompletedTasks = max(completedTasksByUser.values())
    userIdWithhighestAmmountOfCompletedTasks = []
    
    for userId, numberOfFinishedTasks in completedTasksByUser.items():
        if (numberOfFinishedTasks == highestAmmountOfCompletedTasks):
            userIdWithhighestAmmountOfCompletedTasks.append(userId)
            
    return userIdWithhighestAmmountOfCompletedTasks


#////////////////////////////////
def change_list_into_conj_of_param(my_list, key = "id"):
    conj_param = key + "="
    lastIterationNumber = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIterationNumber):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
        
    return conj_param


#////////////////////////////////
def rewarding_the_users(conj_param):
    r = requests.get("https://jsonplaceholder.typicode.com/users/", params=conj_param)
    try:
        users = r.json()
    except json.decoder.JSONDecodeError:
        print("niepoprawny format")
    else:
        for user in users:
            print("Nagrodę na największą ilość wykonanych zadań wręczamy: ", user["name"])   


# tasks = json.loads(r.text) - nieidealna metoda

try:
    tasks = r.json() #działa jak powyższa funkcja, ale dodatkowo sprawdza czy format importowanych danych zgadza się z rządanym formatem
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else: #wykonuje instrukcje po bloku "try:"
    completedTasksByUser = count_task_completion(tasks)
    userIdWithhighestAmmountOfCompletedTasks = get_users_with_most_completed_tasks(completedTasksByUser)
    conj_param = change_list_into_conj_of_param(userIdWithhighestAmmountOfCompletedTasks)
    rewarding_the_users(conj_param)

"""
#sposób 1 (pobieramy całą bazę na raz)   
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()
for user in users:
    if (user["id"] in userIdWithhighestAmmountOfCompletedTasks):
        print("Nagrodę na największą ilość wykonanych zadań wręczamy: ", user["name"])
"""
"""
#sposób 2 (kontaktujemy się z serwerem wiele razy - może być bardzo wolne)
for userId in userIdWithhighestAmmountOfCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users/", params="id="+str(userId))
    users = r.json()
    #print("Nagrodę na największą ilość wykonanych zadań wręczamy: ", user["name"])
"""
"""
#sposób 3 (najlepszy)

conj_param = change_list_into_conj_of_param(userIdWithhighestAmmountOfCompletedTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users/", params=conj_param)
users = r.json()
for user in users:
    print("Nagrodę na największą ilość wykonanych zadań wręczamy: ", user["name"])   
"""







""" Mało czytelne, robimy z tego funkcje

        completedTasksByUser = dict() 
        for item in tasks:
            if (item["completed"] == True):
                try:
                    completedTasksByUser[item["userId"]] += 1
                except KeyError:
                    completedTasksByUser[item["userId"]] = 1
        
        highestAmmountOfCompletedTasks = max(completedTasksByUser.values())
        userIdWithhighestAmmountOfCompletedTasks = []
        
        for userId, numberOfFinishedTasks in completedTasksByUser.items():
            if (numberOfFinishedTasks == highestAmmountOfCompletedTasks):
                userIdWithhighestAmmountOfCompletedTasks.append(userId)
"""        

   
