import requests

def fetch(url):
    """Fetch a URL and return the response object."""
    response = requests.get(url)
    response.raise_for_status()
    return response