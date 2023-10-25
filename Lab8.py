import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://nike.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract and print the page title
    title = soup.title.string
    print(f"Title: {title}")

    # Example: Find and print all the links on the page
    links = soup.find_all('a')
    for link in links:
        print(f"Link: {link.get('href')}")


else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
