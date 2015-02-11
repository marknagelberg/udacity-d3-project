import csv

#The code below converts the raw prosper loan data into
#prosperLoanData_cleaned which focuses on the variables for analysis
with open('prosperLoanData.csv') as f:
    reader = csv.DictReader(f)
    with open('prosperLoanData_cleaned.csv', 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(['Year', 'Prosper Rating (Letter)',
                        'Estimated Return'])
        for line in reader:
            date = line['LoanOriginationDate'].split('/')
            month = int(date[0])
            day = int(date[1])
            year = int(date[2][0:-5])
            

            if year >= 2009 and year <= 2013 and line['EstimatedReturn'] != '':
                writer.writerow([year,line['ProsperRating (Alpha)'],
                                 float(line['EstimatedReturn'])])
