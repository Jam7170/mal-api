import json

import malapi

CLIENT_ID, CLIENT_SECRET = malapi.load_secrets('config/secrets.json')

mal = malapi.MAL(CLIENT_ID)

data = mal.get_user_anime_list("Yamari_", "completed")

print(data)
