"""
Kolorado test api
"""
import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': 'token'}

body = {
    "name": "Marcus",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

body={
    "pokemon_id": "508",
    "name": "Luffy",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

response=requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

body={
    "pokemon_id": "508"
}

response=requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')


