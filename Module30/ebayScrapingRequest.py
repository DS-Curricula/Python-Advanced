import requests

# URL of the eBay web page to scrape
url = "https://www.ebay.com/sch/i.html?_nkw=laptop"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response (HTML)
    print(response.text)
else:
    print(f"Failed to retrieve content from {url}")
