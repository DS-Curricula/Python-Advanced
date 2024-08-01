import requests

url = "https://www.wikipedia.org"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # Specific handling for HTTP errors
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")  # Specific handling for connection errors
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")  # Specific handling for timeout errors
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")  # General handling for all other request-related errors
