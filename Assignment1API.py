import requests
from requests.structures import CaseInsensitiveDict

API_KEY = input("Geef uw API-KEY in:")
request = input("Geef de naam van een film in: ")
response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=' + API_KEY + '&query=' + request)
JSONB = response.json() # store parsed json response

print("=============================================")
print('Titel: '+ JSONB['results'][0]['title']+'\n')
print('Originele Taal: '+ JSONB['results'][0]['original_language']+'\n')
print('Release Date: '+ JSONB['results'][0]['release_date']+'\n')
print('Beschrijving: '+ JSONB['results'][0]['overview'])
print("=============================================")