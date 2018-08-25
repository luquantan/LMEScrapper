import pdb
import pprint

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
print "Copper price is: " + str(LMEData.retrieveBidPriceCashFor(copperHTMLResponse()))
print "Alum price is: " + str(LMEData.retrieveBidPriceCashFor(alumHTMLResponse()))