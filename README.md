# luchador_api
A simple API of Luchador facts built in Flask + postgres db. 


Data Structure:


    {
      "fact": "Luchadors wrestle because they with to be hugged", 
      "id": 1, 
      "uri": "http://www.luchadorapi.com/facts/1"
    },
    
    {
      "fact": "Luchadors are universally left handed", 
      "id": 2, 
      "uri": "http://www.luchadorapi.com/facts/2"
    },
    
    {
      "fact": "A luchadors favorite color is neon", 
      "id": 3, 
      "uri": "http://www.luchadorapi.com/facts/3"
    }, 
    
    {
      "fact": "Luchadors wear masks because they are too handsome", 
      "id": 4, 
      "uri": "http://www.luchadorapi.com/facts/4"
    },
    
    {
      "fact": "Contrary to popular belief, luchadors are in fact born wearing neon spandex onsies", 
      "id": 5, 
      "uri": "http://www.luchadorapi.com/facts/5"
    }
    



-------GET-----------

Return a list of all facts:
http://www.luchadorapi.com/facts

Return a specific fact:
http://www.luchadorapi.com/facts/ + fact_id

Return a random fact:
http://www.luchadorapi.com/facts/random

HTTPBasicAuth credentials necessary for the below.
Email beth0851@gmail.com for access.

--------POST----------

r = requests.post("http://www.luchadorapi.com/facts", json=data, auth=auth)

--------PUT----------

r = requests.put("http://www.luchadorapi.com/facts/3", json=data, auth=auth)

--------DELETE----------

r = requests.put("http://www.luchadorapi.com/facts/3", auth=auth)
