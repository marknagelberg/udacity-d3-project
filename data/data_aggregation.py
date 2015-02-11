#The following code uses pandas to convert the result of the above code into
#aggregated data. The purpose of this is to shrink the size of the data so
#it can be analyzed in D3. Attempts to aggregate the raw data (~75,000 entries)
#resulted in the browser crashing.

import pandas as pd
import numpy as np
import csv

data = pd.read_csv('prosperLoanData_cleaned.csv')
grouped_by_year = data.groupby(["Year", "Prosper Rating (Letter)"])
grouped_all_years = data.loc[:,["Prosper Rating (Letter)", "Estimated Return"]].groupby(["Prosper Rating (Letter)"])

pieces_by_year = [grouped_by_year.quantile(.05), grouped_by_year.mean(), grouped_by_year.median(), grouped_by_year.quantile(.95), grouped_by_year.size()]
concat_pieces_by_year = pd.concat(pieces_by_year, axis = 1)

concat_pieces_by_year.columns = ['5th Percentile', 'Average', 'Median', '95th Percentile', 'Number of Loans']
print concat_pieces_by_year

pieces_all_years = [grouped_all_years.quantile(.05), grouped_all_years.mean(), grouped_all_years.median(), grouped_all_years.quantile(.95), grouped_all_years.size()]
concat_pieces_all_years = pd.concat(pieces_all_years, axis = 1)
concat_pieces_all_years.insert(loc = 0, column = 'Year', value = "All Years")

concat_pieces_all_years.columns = ['Year', '5th Percentile', 'Average', 'Median', '95th Percentile', 'Number of Loans']
print concat_pieces_all_years

#Print to csv the data for each individual year
concat_pieces_by_year.to_csv("prosperLoanData_aggregated1.csv")

#Print to csv the data across all years
concat_pieces_all_years.to_csv("prosperLoanData_aggregated2.csv")
