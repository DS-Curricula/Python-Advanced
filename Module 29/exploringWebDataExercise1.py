import requests               # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML
import os                     # Library for interacting with the operating system
import re                     # Library for working with regular expressions

# URL of the webpage with images
url = "https://www.nationalgeographic.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image URLs
    image_urls = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith('data:image'):  # Skip embedded images
            image_urls.append(src)

    # Create a directory for saving images
    save_dir = './images'
    os.makedirs(save_dir, exist_ok=True)

    # Download images
    for img_url in image_urls:
        img_name = img_url.split('/')[-1].split('?')[0]  # Extract filename
        img_name = re.sub(r'[^\w\-_.]', '', img_name)   # Ensure filename is valid
        img_path = os.path.join(save_dir, img_name)     # Combine directory and filename

        # Download and save the image
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded: {img_name}")
        else:
            print(f"Failed to download: {img_url}")
else:
    print(f"Failed to retrieve content from {url}")

