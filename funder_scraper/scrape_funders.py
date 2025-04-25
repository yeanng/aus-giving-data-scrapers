
import requests
from bs4 import BeautifulSoup

def scrape_paul_ramsay():
    url = "https://paulramsayfoundation.org.au/impact"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [tag.get_text(strip=True) for tag in soup.find_all("h2")]
    return titles

if __name__ == "__main__":
    print(scrape_paul_ramsay())
