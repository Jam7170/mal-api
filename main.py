import json

import malapi

CLIENT_ID, CLIENT_SECRET = malapi.load_secrets('config/secrets.json')

mal = malapi.MAL(CLIENT_ID)

data = mal.search_anime("Reincarnated")['data']

for result in data:
    print(f"{result['node'].get('title')} | {result['node'].get('id')}")

print(data)
