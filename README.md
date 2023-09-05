Personal Projects

## Discounted Cash Flow Valuator: ##
While I was taking Professor Damodaran's Equity Valuation class, I realized that most of the work for a DCF could be automated. He emphasizes that valuations are more of an art than a science—which I agree with—however, the artful part is correctly estimating each assumption (market beta, growth estimates, margins, etc...). The actual projections and discounting is purely manual work, no nuance required. 

So I decided to build a DCF tool that pulls Damodaran's artfully derived assumptions (industry betas, risk premiums, country risk factors, etc...) from his website to discount cash flows input by a user. The program lets anyone with a base year cash flow statement and certain key assumptions (revenue growth, EBIT margins...) quickly create a DCF Model and export as an Excel sheet.

This is the architecture of the project: <br />
- Frontend: React<br />
- API: Spring<br />
- Backend Server: Java<br />
- Database: mySQL



## Webscraper: ##
I built this tool to scrape key data from business broker websites. Previously, I was tasked with manually 
compiling the following info from the broker sites:
1. Company website
2. Gross Revenue Estimate
3. Listed Price
4. City
5. Owner name
6. Owner email
7. Owner phone #
8. Broker name
9. Broker email
10. Broker phone #

This tool saved me and the other analysts countless number of hours of menial labor. 
*Note* BizBuySell has updated their website and changed/removed HTML classes/id for certain information, program does not work like it should


