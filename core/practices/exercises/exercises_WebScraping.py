import re
import bs4
import requests



# Exercise 1:
# Website: http://books.toscrape.com/index.html

# Figure out the URL structure to go through every page
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Scrap every page in the catalogue
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, "lxml")

# Figure out what tag/class represents the Star rating
# Our class/tag will be .star-rating.Two, let's check it out
products = soup.select('.product_pod')
example = products[0]
print('star-rating Two' in str(example))  # dirty way
print(example.select('.star-rating.Two'))  # better way

# We inspect html code to check the tag that contains the title
print(example.select('a'))
print(example.select('a')[1]['title'])

# Now, we use a for loop to grab filter the title for all two stars books and save result into a list
two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:  # check if .star-rating.Two exists
            two_star_titles.append(book.select('a')[1]['title'])






# Exercise 2 - Complete the required tasks
# Website: http://quotes.toscrape.com/

# Use requests library and BeautifulSoup to connect to the website and get the HMTL text from the homepage
base_url = 'http://quotes.toscrape.com/'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, "lxml")

# Get the names of all the authors on the first page
# We can use a set to save all names and avoid having an author twice or more times
authors = set()
for names in soup.select('.author'):
    authors.add(names.getText())
print(authors)
print('\n')

# Create a list of all the quotes on the first page
quotes = list()
for quote in soup.select('.text'):
    quotes.append(quote.getText())
print(quotes)
print('\n')

# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags,
# perhaps check the span.
tags = soup.select('.tag-item')
for tag in tags:
    print(tag.text)
print('\n')

# Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/
# Loop through all the pages and get all the unique authors on the website
# Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check
# that your loop is on the last page with quotes.
# For debugging purposes, I will let you know that there are only 10 pages, so the last page is
# http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know
# the amount of pages beforehand, perhaps use try/except for this, its up to you!
url = 'http://quotes.toscrape.com/page/'
all_authors = set()

for page in range(1, 10):
    scraping_url = url+str(page)
    res = requests.get(scraping_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for names in soup.select('.author'):
        all_authors.add(names.getText())
print(all_authors)






# Exercise 3:
# Website: http://www.simplilearn.com/

# View and print the Simplilearn web page content in a good format
base_url = 'http://www.simplilearn.com/'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.prettify())
print('\n')

# Close result content
res.close()

# View the head of the website
print(soup.select('head'))
# alternatively print(soup.head)
print('\n')

# View the title of the website
print(soup.select('title'))
# alternaively print(soup.title)
print('\n')

# Find all the links in the website
for href in soup.find_all('a', href=True):
    print(href)






# Exercise 4:
# Website: http://www.simplilearn.com/

# View and print the Simplilearn web page content in a good format
base_url = 'http://www.simplilearn.com/'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
res.close()
print(soup.prettify())
print('\n')

# View the title
print(soup.select('title'))
print('\n')

# Print all the href links present in the Simplilearn webpage
for href in soup.find_all('a', href=True):
    print(href)
print('\n')

# Search and print the resource headers of the Simplilearn webpage
for header in soup.find_all(re.compile('^h[1-6]$')):
    print(header.text)
print('\n')

# Search resource topics
new_url = 'https://www.simplilearn.com/resources'
res = requests.get(new_url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
topics = soup.select('.show-focus span')
for topic in topics:
    print(topic.text)
