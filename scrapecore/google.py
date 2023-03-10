import requests
from bs4 import BeautifulSoup

def URI(term):
    # Set the URL and user-agent
    url = f"https://www.google.com/search?q={term}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # Send a GET request to the URL and get the response
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object and find all the search result links
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find_all("div", class_="yuRUbf")

    # Print the search result links
    for result in search_results:
        link = result.find("a")["href"]
        print(link)
        
def URI_LIST(term):
    # Set the URL and user-agent
    url = f"https://www.google.com/search?q={term}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # Send a GET request to the URL and get the response
    response = requests.get(url, headers=headers)

    # Create a BeautifulSoup object and find all the search result links
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find_all("div", class_="yuRUbf")

    # Print the search result links
    # for result in search_results:
    #     link = result.find("a")["href"]
    #     print(link)
    print(search_results)
        
        
