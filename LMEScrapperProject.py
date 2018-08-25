import pdb
import pprint

import requests 
from bs4 import BeautifulSoup # For HTML parsing

# Purpose
# To automate the retrival of daily LME settlement prices from the LME wesbite

# LME Wesbite
LME_COPPER_URL = 'https://www.lme.com/Metals/Non-ferrous/Copper#tabIndex=0'
LME_ALUM_URL = 'https://www.lme.com/Metals/Non-ferrous/Aluminium#tabIndex=0'


# Getting response from the server


# Find out what date this data is valid for

def currentDate():


def validityDate(responseString):



# Find out what is the current closing price 