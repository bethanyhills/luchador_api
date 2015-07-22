# luchador_api
Data Structure:

{
  "facts": [
    {
      "fact": "Luchadors wrestle because they with to be hugged", 
      "id": 1, 
      "uri": "http://morning-everglades-5851.herokuapp.com/facts/1"
    }, 
    {
      "fact": "Luchadors are universally left handed", 
      "id": 2, 
      "uri": "http://morning-everglades-5851.herokuapp.com/facts/2"
    }, 
    {
      "fact": "A luchadors favorite color is neon", 
      "id": 3, 
      "uri": "http://morning-everglades-5851.herokuapp.com/facts/3"
    }, 
    {
      "fact": "Luchadors wear masks because they are too handsome", 
      "id": 4, 
      "uri": "http://morning-everglades-5851.herokuapp.com/facts/4"
    }, 
    {
      "fact": "Contrary to popular belief, luchadors are in fact born wearing neon spandex onsies", 
      "id": 5, 
      "uri": "http://morning-everglades-5851.herokuapp.com/facts/5"
    }
  ]
}


-------GET-----------

Return a list of all facts:
https://morning-everglades-5851.herokuapp.com/facts

Return a specific fact:
https://morning-everglades-5851.herokuapp.com/facts/ + <fact_id>

Return a random fact:
https://morning-everglades-5851.herokuapp.com/facts/random

HTTPBasicAuth credentials necessary for the below:

--------POST----------

r = requests.post("https://morning-everglades-5851.herokuapp.com/facts", json=data, auth=auth)

--------PUT----------

r = requests.put("https://morning-everglades-5851.herokuapp.com/facts/3", json=data, auth=auth)

--------DELETE----------

r = requests.put("https://morning-everglades-5851.herokuapp.com/facts/3", auth=auth)
