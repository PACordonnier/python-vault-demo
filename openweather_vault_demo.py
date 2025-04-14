import os
import requests

# Récupération de la clé API depuis Vault (injection automatique)
api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

# Ville à interroger
city = "Paris"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Requête API
response = requests.get(url)
data = response.json()

# Résultat
weather = data['weather'][0]['description']
temp = data['main']['temp']
print(f"Météo à {city} : {weather}, {temp}°C")
