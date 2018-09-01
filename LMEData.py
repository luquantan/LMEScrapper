import pandas as pd
import pdb
from bs4 import BeautifulSoup # For HTML parsing
import datefinder

def parseHTMLResponse(raw_html):
    return BeautifulSoup(raw_html, 'html.parser')

def getHTMLTable(html):
    return html.find("table") # defaults to the first table

def getTableHeader(table):
    data_header = []
    table_head = table.find('thead')
    rows = table_head.find_all('tr')
    for row in rows:
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols]
        data_header.append([ele for ele in cols if ele]) # Get rid of empty values
    return data_header

def getTableBody(table):
    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
    return data

def getLatestDate(html):
    date_tag = html.find('div' , attrs = {"class": "delayed-date left "})
    tag_string = date_tag.string
    date_generator = datefinder.find_dates(tag_string)
    for datetime in date_generator:
        latest_date = datetime
    return latest_date


def convertListToDataFrame(data_header, data):
    # Store Data as a Data Frame
    df = pd.DataFrame(data, columns=data_header[0])
    df.set_index('Contract', inplace = True)
    return df

def getColumnName(priceType):
    if priceType == 'bid':
        return 'Bid (US$ / Tonne)'
    elif priceType == 'offer':
        return 'Offer (US$ / Tonne)*'

def getRowName(contractType):
    if contractType == 'cash':
        return 'Cash'
    elif contractType == '3month':
        return '3-months'

def retrieveData(raw_html, priceType, contractType):
    html = parseHTMLResponse(raw_html)
    latest_date = getLatestDate(html)
    table = getHTMLTable(html)
    data_header = getTableHeader(table)
    data = getTableBody(table)
    df = convertListToDataFrame(data_header, data)
    colName = getColumnName(priceType)
    rowName = getRowName(contractType)
    return (latest_date, df[colName][rowName])

def retrieveBidPriceCashFor(raw_html):
    return retrieveData(raw_html, 'bid', 'cash')
