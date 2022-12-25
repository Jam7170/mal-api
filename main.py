import json

import malapi

CLIENT_ID, CLIENT_SECRET = malapi.load_secrets('config/secrets.json')

mal = malapi.MAL(CLIENT_ID)

data = mal.search_anime("Reincarnated")

print(data)
