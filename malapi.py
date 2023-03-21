import os, requests, json
from typing import Optional

BASE_URL = "https://api.myanimelist.net/v2"

def load_secrets(path_):
    if not os.path.exists(path_): return
    with open(path_, 'r') as f:
        secrets = json.loads(f.read())
    return secrets['client-id'], secrets['client-secret']

class MAL:
    def __init__(self, client_id: str, client_secret: Optional[str] = None):
        self._client_id = client_id

    def _get_without_auth(self, endpoint):
        url = f"{BASE_URL}/{endpoint}"
        res = requests.get(url,headers={"X-MAL-CLIENT-ID": self._client_id})
        return res

    def get_anime_by_id(self, anime_id: int | str) -> dict:
        return self._get_without_auth(f'anime/{anime_id}').json()

    def search_anime(self, query: str, limit: int=20) -> dict:
        endpoint=f'anime?q={query}&limit={limit}&fields=alternative_titles'
        return self._get_without_auth(endpoint).json()

    def get_user_anime_list(self, username: str, status: Optional[str] = None) -> dict:
        endpoint = f"users/{username}/animelist"
        if status is not None: endpoint += f"?status={status}"
        return self._get_without_auth(endpoint).json()