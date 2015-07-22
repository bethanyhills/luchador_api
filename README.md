# luchador_api

GET

Return a list of all facts:
https://morning-everglades-5851.herokuapp.com/facts

Return a specific fact:
https://morning-everglades-5851.herokuapp.com/facts/<id>

Return a random fact:
https://morning-everglades-5851.herokuapp.com/facts/random

P0ST:
r = requests.post("https://morning-everglades-5851.herokuapp.com/facts", json=data, auth=auth)
