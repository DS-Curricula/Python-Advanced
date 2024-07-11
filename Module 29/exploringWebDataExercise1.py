from bs4 import BeautifulSoup
import requests
import os
import re

# URL of the webpage with images
url = "https://www.nationalgeographic.com/"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse HTML using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all image URLs
    image_urls = [img['src'] for img in soup.find_all('img') if img.get('src') and img['src'].startswith('http')]

    # Download images to local directory
    save_dir = './images'
    os.makedirs(save_dir, exist_ok=True)

    for img_url in image_urls:
        # Extract filename without query parameters
        img_name = img_url.split('/')[-1].split('?')[0]

        # Ensure filename is valid using regular expressions
        img_name = re.sub(r'[^\w\-_.]', '', img_name)

        img_path = os.path.join(save_dir, img_name)

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded: {img_name}")
        else:
            print(f"Failed to download: {img_url}")
else:
    print(f"Failed to retrieve content from {url}")

