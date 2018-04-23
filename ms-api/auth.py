import requests
from keys import *

def get_token(token_endpoint, client_id, client_secret):
    """
    Generates an authentication access token using the tokenEndpoint URI
    """
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "resource": "https://management.azure.com/",
    }
    response = requests.post(token_endpoint, data=payload).json()
    return response['access_token']


def generate_headers():
    """
    Generates the authorization request headers for requests
    """
    token = get_token(tokenEndpoint, clientId, clientSecret)
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return headers

