from bs4 import BeautifulSoup as BS
import requests

def getPage():
    ticker = input("Enter a ticker as yahoo finance expects it: ")
    
    url = f"https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    
    page = requests.get(url, headers=headers)
    return page

def parsePage(page):
    soup = BS(page, 'html.parser')
    PEpattern = 'Trailing P/E'
    PElabel = soup.find('span', text = PEpattern)
    val = PElabel.parent.next_sibling.text
    print(val)
    
    
if __name__ == "__main__":
        page = getPage()
        parsePage(page.text)
    
