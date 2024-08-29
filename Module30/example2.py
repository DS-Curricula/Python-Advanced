from bs4 import BeautifulSoup

# HTML content for demonstration
html_content = """
<html>
<head>
  <title>Example Page</title>
</head>
<body>
  <h1>Welcome to Beautiful Soup</h1>
  <p class="intro">Beautiful Soup makes web scraping easy!</p>
  <div id="content">
    <p>Here are some links:</p>
    <a href="http://example.com/page1">Link 1</a>
    <a href="http://example.com/page2">Link 2</a>
    <a href="http://example.com/page3">Link 3</a>
  </div>
</body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Example 1: Extracting text and attributes
print("Title of the page:", soup.title.text)  # Output: Example Page

# Example 2: Finding elements by tag and class
intro_text = soup.find('p', class_='intro').text
print("Intro text:", intro_text)  # Output: Beautiful Soup makes web scraping easy!

# Example 3: Navigating the HTML structure
div_content = soup.find('div', id='content')
links = div_content.find_all('a')
for link in links:
    print("Link:", link['href'])  # Output: Link: http://example.com/page1, Link: http://example.com/page2,
    # Link: http://example.com/page3

# Example 4: Handling nested elements and siblings
first_link = soup.find('a')
print("First link text:", first_link.text)  # Output: Link 1
print("Next sibling of the first link:", first_link.next_sibling)  # Output: , Link 2

# Example 5: CSS Selector
paragraphs = soup.select('div#content p')
for paragraph in paragraphs:
    print("Paragraph inside content:", paragraph.text)  # Output: Here are some links:

# Example 6: Modifying the HTML (adding a new tag)
new_tag = soup.new_tag('b')
new_tag.string = "Important"
soup.h1.append(new_tag)

print("Modified h1 tag:", soup.h1)  # Output: <h1>Welcome to Beautiful Soup<b>Important</b></h1>
