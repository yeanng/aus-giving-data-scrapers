
import requests
from bs4 import BeautifulSoup

def scrape_acnc_profile(abn):
    url = f"https://www.acnc.gov.au/charity/{abn}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return {
        "abn": abn,
        "name": soup.title.string.strip() if soup.title else "Unknown",
        "url": url
    }

if __name__ == "__main__":
    print(scrape_acnc_profile("60822848760"))  # Example: Paul Ramsay Foundation
