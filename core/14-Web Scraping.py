"""
BASIC CONCEPTS:
-Get premission to scrape, otherwise your IP address may be blocked.
-Be aware that websites change often, meaning your code could be broken.
-Steps to web scraping:
  -Step 1: Send a request to the targeted website to collect the required data.
  -Step 2: Retrieve information from the targeted website in HTML or XML format.
  -Step 3: Parse information to the several parsers based on the data format.
  -Step 4: Store the parsed data in the desired format.

REQUEST:
-Use request to grab a page. This may fail if you have a firewall blocking your app.
-Object type will be an HTTP response
-Request object contains website information and the following attributes:
  -text: a string of text inside an html tag.
  -content: raw content of a website.

BEAUTIFULSOUP:
-Use beautiful soup to analyze a page and get elements from the website.
-We need to add a parser to interpret or render the information from the website.
-There are different parsers we can use:
  -html.parser -> Python-based, fast, and lenient.
  -lxml html -> it depends on C, fast and lenient.
  -lxml xml -> the only xml parser available and it also depends on C.
  -html5lib -> Python-based, it is slow and can create valid HTML5.
-Types of Objects in Beautiful Soup:
  -Tag: an XML or HTML tag in the web document. Tags have a lot of attributes and methods.
  -NavigableString: a string or set of characters that correspond to the text present within a tag.
  -BeautifulSoup: it represents the entire web document and supports navigating and searching the document tree.
  -Comment: the comment or information section of the document. It is a special type of string.
"""

import requests
import bs4



# -----------------REQUEST-----------------

# Requesting the website
re = requests.get("http://quotes.toscrape.com/")

# Get request status
re.raise_for_status()

# Get request object attributes
print(re.text)
print(re.content)
print('\n')






# -----------------BEAUTIFUL SOUP-----------------

# Fetch websites using different parsers
# Adding prettify() makes code cleaner so that it is readable to humans
soup = bs4.BeautifulSoup(re.text, "lxml")
soup2 = bs4.BeautifulSoup(re.content, "html.parser")
print(soup.prettify())
print('\n')

# Print tags from the website and view their attributes using attrs
# To do this use the syntax "soup.tag_name"
print(soup.div.h1)
print(soup.a)
print(soup.a.attrs)
print(soup.div.attrs)

# Retrieve information
# select() -> return a list of elements from a website by taking the following arguments
# select('tag')        - select all elements with the <tag>
# select('#id')        - select HTML element containing the indicated id attribute
# select('.class')     - select the HTML elements with the indicated CSS class. Spaces must be replaced for '.'
# select('div span')   - select any elements named <span> that are within an element named <div>
# select('div > span') - select any elements named <span> directly within an element named <div>
print(soup.select('head'))
print(soup.select('.author'))

# We can iterate over the list of selected elements, or just grab some of them
for name in soup.select('.author'):
    print(name.text)
print(soup.select('.author')[0:3])

# Alternatively, we can use getText() to get the text attribute
for quote in soup.select('.tag-item'):
    print(quote.getText().replace("\n", "").strip())
print("\n")


# Finding elements
# find()     -> return first match of an string passed as argument
# find_all() -> return all matches of an string passed as argument, in list format
print(soup.find('h1'))

# Find elements by HTML Class Name
print(soup.find("span", {"class": "text"}).text.replace("\n", ""))
for author in soup.find_all("small", class_="author"):
    print(author.text)

# Find all links in a website
for href in soup.find_all('a', href=True):
    print(href)






# -----------------BEAUTIFUL SOUP - IMAGES-----------------

# Working with images in Beautiful Soup
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
image_info = soup.select('.thumbimage')
computer = image_info[0]
print(computer)
print(computer['src'])  # printing id 'src'

# Grab image link with request. Sometimes we need to fulfill the link, like adding 'https'
image_link_recieved = '//upload.wikimedia.org/wikipedia/commons/b/be/Deep_Blue.jpg'
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
print(image_link.content)

# Save an image to a file
f = open('new_image.jpg', 'wb')
f.write(image_link.content)
f.close()
