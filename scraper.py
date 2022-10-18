from bs4 import BeautifulSoup as BS
import requests

def getPage(ticker):
    
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
    
def getStats(page):
    soup = BS(page, 'html.parser')

    PEpattern= 'Trailing P/E'
    PEval = -1.0
    PEvalString = soup.find('span', text = PEpattern).parent.next_sibling.text

    if (PEvalString == "N/A"):
        print("PE not given")
        PEfound = False
    else:
        PEfound = True
        PEval = float(PEvalString)
        print("PE: ", PEval)
    
    PBpattern = 'Price/Book'
    PBval = -1.0
    PBvalString = soup.find('span', text = PBpattern).parent.next_sibling.text

    if (PBvalString == "N/A"):
        PBfound = False
        print("PB not given")
    else:
        PBfound = True
        PBval = float(PBvalString)
        print("PB: ", PBval)
    
    if (PEfound & PBfound):
        PEPBV = PEval * PBval
        print("PE * PBV: %.2f" % PEPBV)
    return
    
if __name__ == "__main__":
        ticker = ""
        while (ticker != "exit"):
            ticker = input("ENTER A TICKER OR ENTER exit TO EXIT: ")
            if (ticker != "exit"):
                page = getPage(ticker)
                if (page.status_code != 200):
                    print("An error occured. Page get results in " + page.status_code)
                else:
                    if ('lookup' in page.url):
                        print("Ticker not found. make sure you did not spell it wrong")
                    else:
                        getStats(page.text)
    
