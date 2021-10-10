import requests
from requests.structures import CaseInsensitiveDict

API_KEY = input("Geef uw API-KEY in:") # Vraagt aan gebruiker voor de API-KEY
request = input("Geef de naam van een film in: ") # Vraagt naar de naam van de film
response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=' + API_KEY + '&query=' + request) #Stuurt de request met de API-KEY en filmnaam toegevoegd
JSONB = response.json() # json file in variabele steken


# Vervolgens worden de gegevens die interessant zijn geselecteerd en uitgeprint
print("=============================================")
print('Titel: '+ JSONB['results'][0]['title']+'\n')
print('Originele Taal: '+ JSONB['results'][0]['original_language']+'\n')
print('Release Date: '+ JSONB['results'][0]['release_date']+'\n')
print('Beschrijving: '+ JSONB['results'][0]['overview'])
print("=============================================")