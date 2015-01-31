#The following code uses pandas to convert the result of the above code into
#aggregated data. The purpose of this is to shrink the size of the data so
#it can be analyzed in D3. Attempts to aggregate the raw data (~75,000 entries)
#resulted in the browser crashing.

import pandas as pd
import numpy as np
import csv

data = pd.read_csv('prosperLoanData_cleaned.csv')
grouped_by_year = data.groupby(["Year", "Prosper Rating (Letter)"])
grouped_all_years = data.groupby(["Prosper Rating (Letter)"])
grouped_by_year_output = grouped_by_year.agg([np.mean, np.min, np.max])
grouped_all_years_output = grouped_all_years.agg([np.mean, np.min, np.max])

#Print to csv the avg/min/max return data for each individual year
grouped_by_year_output.to_csv("prosperLoanData_aggregated1.csv")

#Print to csv the avg/min/max return data across all years
grouped_all_years_output.to_csv("prosperLoanData_aggregated2.csv")
