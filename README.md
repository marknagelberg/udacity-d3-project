Summary

The visualization analyzes data on loans, taken from the peer-to-peer lending marketplace called Prosper. It focuses on two main pieces of data on loans originated from 2009 to 2013: prosper rating, which provides a measure of loan risk; and estimated return to lenders, which is essentially the interest rate received by lenders after costs and losses.


Design

When exploring the many variables in the raw Prosper loan data, I thought "what information would I be most interested in if I was thinking of lending money through Prosper?" I came to the conclusion that the most valuable information would be the amount they can expect to make from loans, i.e. the median estimated return. 

Another key piece of information would be the credit risk of who I am lending the money to, as this will be a key determinant of returns. This is why I included the "Prosper Loan Rating" on the horizontal axis, as these values represent measures of credit risk. The main piece of information I wanted to draw to the eye was how the median estimated return changes as credit risk decreases. 

Another key piece of information I encoded is the "spread" of expected returns. As a result, I included 5th and 95th percentile estimated return for each prosper loan rating. This is important to know as a lender, because a higher spread of returns means more risk that would not be communicated by median returns alone. Higher spread means opportunity for big returns, but also big losses. 

I also included the number of loans for each category. Some people may find this interesting to get some further background on the data and understand how robust particular observations are. For example, a reader may be a bit more skeptical of a particular observation when we are talking about a relatively small number of loans.

Finally, I included various years, so the reader could see how estimated returns change over time and understand the robustness of the direct relationship between estimated return and creditworthiness. 

A few key stories emerge from the data:

- The central story is that, as you would expect, there is a clear and consistent direct relationship between creditworthiness and estimated return - higher risk loans tend to yield higher estimated returns to compensate lenders for the increased risk. This is fairly consistent across all years. 

- Loans to less creditworthy borrowers tend to have a much larger spread (maximum return - minimum return) than loans to more creditworthy borrowers. This makes sense, as it explains the tradeoff you have to make when lending to less creditworthy borrowers. The average estimated return is bigger, but there is a chance for bigger losses.

- The spread of loan returns appears to decline fairly consistently over the years from 2009 to 2013. This may be due to the economic downturn of 2009, when lenders likely had to deal with many more defaults that increased down-side risks to loans, thus decreasing minimum expected returns. At the same time, lenders likely expected to be compensated for these risks with higher interest rates, thus increasing maximum estimated returns.

When developing the visualization, my first step was downloading the Prosper loan data and exploring it in Tableau to look for interesting relationships. I ultimately converged on the relationship between effective return and loan risk (see the screenshot of the preliminary graph in "First Exploratory Version in Tableau (December 2014).PNG"). To improve this preliminary version of the visualization, I wanted to change the y axis to percentage, change the x axis values to something more meaningful, add a title, make the graph a bit less "busy", and make the main message of the graph more clear. Also, when flipping through the years, I wanted to ensure the axis always remained the same to allow easy comparison across years. I also had to perform some data aggregation, since the data set used in Tableau had ~75,000 entries, which caused the web browser to crash when using dimple.js or d3.js. 

I chose a scatterplot for average, minimum, and maximum estimated returns, as viewing these points along a common scale is the best visual encoding to ensure the viewer can descern differences in return across risk categories. Color is used to help the reader distinguish between average, minimum, and maximum estimated returns. I made average returns a line chart, since this is the focus of the visualization and I wanted the lines to emphasize how returns change as loan risk decreases.


Feedback

After coding and iterating on the design many times on my own, I came up with the version illustrated in "Version Before Feedback (June 30 2015).PNG", which I was quite happy with. I shared the visualization on my website at http://www.marknagelberg.com/udacity_data_viz_project/ and I received the following feedback from several economist colleagues and some family: 

- Having the years at the top is confusing and it seems like they would be more suitable on the bottom.

- It is not clear that it is possible to click on the years to get different results. The cursor over the buttons is a "text" cursor, rather than a cursor that would indicate you can click on it.

- Red would be more suitable color for the minimum values, because intuitively we think of low returns as being "in the red".

- It was unclear why I chose to make a line chart for only average returns, and not also minimum/maximum returns.

- The visualization did not render properly in Firefox (it was getting cut off). 

In response to these comments, I swapped the minimum/maximum colors, changed css styling and html structure so the viz works in Firefox, changed the mouseover cursor for the years to a "pointing hand", and moved the years buttons to the bottom of the chart. I explained to my colleague that the reason I only had a line graph for average returns was because I didn't want the chart to be too cluttered and I wanted to focus on the change in average returns. He changed his mind and said that I should leave it as-is. This version of the visualization is given by "index_first_submission.html".

After submitting this version of the visualization, my Udacity reviewer pointed out that all of the data that I reported is not robust to outliers (minimum return, average return, maximum return), and therefore may not provide particularly useful information about the distribution of loans for each risk category. Furthermore, they suggested including information on the number of loans. In response, I reprocessed the data to report on the 5th percentile, median, and 95th percentile instead of min, average, and max. I also added a second axis with a light bar chart in the background illustrating the number of loans.


Resources

- I used Tableau data visualization software to conduct exploratory data analysis on the raw loan data.

- To perform data cleaning and aggregation, I used Python along with the pandas, numpy, and csv packages.

- As a starting point, I built my visualization off of the code for the d3.js visualizations provided in the course. Ultimately, I changed almost all of the code, but it provided a useful starting point.

- To better learn how dimple.js works and get examples for specific functionality, I examined many of the examples provided on the dimple.js site (http://dimplejs.org/examples_index.html). 