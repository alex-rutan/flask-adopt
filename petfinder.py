from projects_secrets import API_KEY, API_SECRET

import requests, random

def get_updated_token():
    """authenticate """

    resp = requests.post("https://api.petfinder.com/v2/oauth2/token", 
                    data = {"grant_type": "client_credentials", 
                            "client_id": API_KEY, 
                            "client_secret": API_SECRET})

    return resp.json()["access_token"]
    
def get_pet_from_API(token):
    """Make a GET request for one random pet."""
    
    resp = requests.get("https://api.petfinder.com/v2/animals",
                        params={"limit": 100},
                        headers={"Authorization": f"Bearer {token}"})
    
    return resp.json()
    # random_num = random.randrange(0, 100)