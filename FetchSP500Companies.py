import pandas as pd

# Fetch the S&P 500 constituents
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
tables = pd.read_html(url)

# Get the table containing the constituents
constituents_table = tables[0] #0 assumes it is the first table on the page

# Extract the ticker symbols from the table
sp500_symbols = constituents_table['Symbol'].to_list()

# Print list of symbols
print(sp500_symbols)