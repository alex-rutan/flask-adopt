from projects_secrets import API_KEY, API_SECRET

import requests

TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"

TOKEN_REQUEST_DICT = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": API_SECRET}


def get_token(TOKEN_URL, TOKEN_REQUEST_DICT):
    """authenticate """

    resp = requests.post(TOKEN_URL, 
                    data = TOKEN_REQUEST_DICT)

    print(resp)