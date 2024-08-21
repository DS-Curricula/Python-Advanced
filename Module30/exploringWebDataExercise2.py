import requests
from bs4 import BeautifulSoup
import time

url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"

# Function to fetch data from the URL
def fetch_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for _ in range(3):  # Try up to 3 times
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        print("Retrying in 5 seconds...")
        time.sleep(5)
    return None

# Function to parse data from the HTML content
def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_='product_pod')
    results = []
    for item in items:
        name_tag = item.find('h3')
        price_tag = item.find('p', class_='price_color')
        if name_tag and price_tag:
            name = name_tag.text
            price = price_tag.text
            results.append((name, price))
        else:
            print("Name or price not found for one item")
    return results

# Fetch and parse data, then print results
html = fetch_data(url)
if html:
    data = parse_data(html)
    for name, price in data:
        print(f"Name: {name}, Price: {price}")
else:
    print("Failed to retrieve data from the website.")

