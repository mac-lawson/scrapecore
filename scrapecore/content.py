import requests
from bs4 import BeautifulSoup


def CONTENT(url):
    # Fetch the HTML content of the webpage using requests
    response = requests.get(url)
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract all the strings found on the webpage
    strings = []
    for string in soup.stripped_strings:
        strings.append(str(string))
    
    # Return the list of strings found on the webpage
    for single in strings:
        print(single)

def CONTENT_LIST(url):
    # Fetch the HTML content of the webpage using requests
    response = requests.get(url)
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract all the strings found on the webpage
    strings = []
    for string in soup.stripped_strings:
        strings.append(str(string))
    
    # Return the list of strings found on the webpage
    print(strings)

CONTENT("https://meadhallschool.org")
    
    