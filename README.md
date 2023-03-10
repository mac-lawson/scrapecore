# scrapecore
scrapecore is a python framework for web scrapping and GPT training

## content.py
This file contains two functions CONTENT and CONTENT_LIST that fetch the HTML content of a webpage using the requests library, parse the HTML content using the beautifulsoup4 library, and then extract and print or return the strings found on that page.

##### Dependencies
This file requires the following Python libraries to be installed:
```
requests
beautifulsoup4
```
You can install these libraries using pip, by running the following command in your terminal:
```
pip install requests beautifulsoup4
```
##### Function Descriptions
- CONTENT(url)
```
This function takes a single argument, url, which is a string representing the URL of the webpage to fetch. It then fetches the HTML content of the webpage using the requests library, parses the HTML content using the beautifulsoup4 library, extracts all the strings found on the webpage, and prints them to the console.
```
- CONTENT_LIST(url)
```
This function takes a single argument, url, which is a string representing the URL of the webpage to fetch. It then fetches the HTML content of the webpage using the requests library, parses the HTML content using the beautifulsoup4 library, extracts all the strings found on the webpage, and returns them as a list.
```
## google.py
This file uses the requests and BeautifulSoup libraries to search Google for a given term and extract the search result links.

##### Function Descriptions

- URI(term): 
```
This function takes a search term as input and prints the search result links to the console.
```
- URI_LIST(term): 
```
This function takes a search term as input and returns a list of search result links.
Both functions use the same process to retrieve the search result links. The URL used for the search is constructed by appending the search term to the Google search query URL. The user-agent is set in the headers to mimic a browser request. The response is then processed using BeautifulSoup to find all the search result links in the HTML content. Finally, the links are printed or returned as a list, depending on the function used.
```