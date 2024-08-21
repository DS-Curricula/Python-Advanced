import requests

# Your actual credentials
username = "my_username"
password = "my_password"

# URL for httpbin endpoint that requires basic authentication
url = f"https://httpbin.org/basic-auth/{username}/{password}"

# Basic authentication
response = requests.get(url, auth=(username, password))
print("Response from basic authentication:")
print(response.text)

# Session handling
session = requests.Session()
session.auth = (username, password)
response = session.get(url)
print("\nResponse from session handling:")
print(response.text)
