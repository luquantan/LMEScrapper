import pdb
import pprint
import pandas as pd

import LMENetworkManager as NetworkManager
import LMEData



# Purpose
# To automate the retrival of daily LME settlement prices from the LME wesbite

# LME Wesbite
LME_COPPER_URL = 'https://www.lme.com/Metals/Non-ferrous/Copper#tabIndex=0'
LME_ALUM_URL = 'https://www.lme.com/Metals/Non-ferrous/Aluminium#tabIndex=0'

# Getting response from the server

def copperHTMLResponse():
    return NetworkManager.getHTMLFor(LME_COPPER_URL)

def alumHTMLResponse():
    return NetworkManager.getHTMLFor(LME_ALUM_URL)


# Find out what date this data is valid for

# Find out what is the current closing price 
# print "Copper price is: " + str(LMEData.retrieveBidPriceCashFor(copperHTMLResponse()))
# print "Alum price is: " + str(LMEData.retrieveBidPriceCashFor(alumHTMLResponse()))

copperData = LMEData.retrieveBidPriceCashFor(copperHTMLResponse())
alumData = LMEData.retrieveBidPriceCashFor(alumHTMLResponse())

copperStrings = ("Copper Date", "Copper Bid Price")
alumStrings = ("Alum Date", "Alum Bid Price")

copperDataList = list((copperStrings, copperData))
alumDataList = list((alumStrings, alumData))

copperDataFrame = pd.DataFrame(copperDataList)
alumDataFrame = pd.DataFrame(alumDataList)

copperDataFrame.to_csv('copper.csv', index=False)
alumDataFrame.to_csv('alum.csv', index=False)

import pdb
pdb.set_trace()


print "done"