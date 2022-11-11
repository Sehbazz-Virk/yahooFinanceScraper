import investpy as inv
import pandas

def getData(company):
    pass

def getCompanyList():
    data = inv.get_stocks('Canada')
    stockList = data.loc[:,'symbol']
    print(stockList)

getCompanyList()