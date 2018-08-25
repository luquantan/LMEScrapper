import pandas as pd
import pdb

html = BeautifulSoup(raw_html, 'html.parser')

# Get Table Object
table = html.find("table") # defaults to the first table

## Get Table Headers
data_header = []
table_head = table.find('thead')
rows = table_head.find_all('tr')

for row in rows:
    cols = row.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    data_header.append([ele for ele in cols if ele]) # Get rid of empty values


# Get Table Body
data = []
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values


# Store Data as a Data Frame
df = pd.DataFrame(data, columns=data_header[0])
df.set_index('Contract', inplace = True)

# Retrieve Bid Price
print df['Bid (US$ / Tonne)']['Cash']

print "done"