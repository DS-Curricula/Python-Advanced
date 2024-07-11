from bs4 import BeautifulSoup
import requests

def scrape_ebay(search_term, pages=1):  # Change pages back to 1 for debugging
    base_url = f"https://www.ebay.com/sch/i.html?_nkw={search_term}"
    all_products = []

    for page in range(1, pages + 1):
        url = f"{base_url}&_pgn={page}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all product containers
            products = soup.find_all('div', class_='s-item__info')

            for product in products:
                # Debug: Print the whole product HTML to understand structure
                print(product.prettify())

                # Try to extract name and price
                name_element = product.find('h3', class_='s-item__title')
                price_element = product.find('span', class_='s-item__price')

                if name_element and price_element:
                    name = name_element.text.strip()
                    price = price_element.text.strip()
                    all_products.append((name, price))
                else:
                    print("Name or price element not found for one item.")

        else:
            print(f"Failed to retrieve content from {url}")

    return all_products

# Example usage
search_results = scrape_ebay("laptop", pages=1)  # Limit to 1 page for debugging
for name, price in search_results:
    print(f"Product: {name} | Price: {price}")
