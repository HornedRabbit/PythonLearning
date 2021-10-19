"""

JSON

json.dumps(data) - zapisuje dane do postaci String json
json.dump(data, nameOfFile, ensure_ascii=False) - zapisuje dane do pliku w postaci json

"""

import json

#python data format
film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

#zapis danych w formacie JSON - string
encodedFilm = json.dumps(film, ensure_ascii=False)

#zapis danych do pliku w formacie JSON
with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)


#JSON data format
"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""

