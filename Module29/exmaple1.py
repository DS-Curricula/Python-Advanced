from bs4 import BeautifulSoup

# HTML content for demonstration
html_content = "<html><body><p>Hello, Beautiful Soup!</p></body></html>"

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Extract text from the paragraph tag
paragraph_text = soup.find('p').text

# Print the extracted text
print(paragraph_text)
