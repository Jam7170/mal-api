import json

import malapi

CONSTANT = "value"

CLIENT_ID, CLIENT_SECRET = malapi.load_secrets('config/secrets.json')

mal = malapi.MAL(CLIENT_ID)

data = mal.search_anime("Reincarnared", limit=2)

print(json.dumps(data, indent=4))
