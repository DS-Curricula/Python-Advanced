import requests

url = "https://www.wikipedia.org"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for HTTP errors (4xx or 5xx)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

