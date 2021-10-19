import requests


#Saving the working URLs into a text file
"""
with open("Working sites.txt", "w", encoding="UTF-8") as file:
    for element in request_list:
         if element.status_code == 200:
             file.write(element + "\n")
"""         
response = requests.get("http://videokurs.pl")

if response.status_code == 200:
    print("Działa.")
