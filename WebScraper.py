# Web scraper 
# Finds the following information from bizbuysell.com
"""
1. listing url
2. location
3. sale price
4. owner name
5. owner email
6. owner phone #
7. broker name
8. broker phone #
9. broker email
"""

# to implement: filter by company ARR 

# input the bizbuysell page, pre-filtered by geographic location, industry, price range, revenue, etc...
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv

# URL of the target page
base_url = "https://www.bizbuysell.com/california/agriculture-businesses-for-sale/?q="
encoded_query = "bHQ9MzAsNDAsODA%3D"
url = base_url + urllib.parse.unquote(encoded_query)

# Send an HTTP GET request and get the page content
response = requests.get(url)
page_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Find all the listings on the page
listings = soup.find_all("li", class_="listing-row")

csv_file = open("business_listings.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Company URL", "location", "Owner Name", "Sale Price"])

# Loop through each listing and extract the required information
for listing in listings:
    company_url = listing.find("a", class_="diamond")["href"]
    location = listing.find("p", class_="location")
    sale_price = listing.find("p", class_="asking-price").get_text(strip=True)
    # website updated owner and broker fields
   
    csv_writer.writerow([company_url, location, sale_price])

csv_file.close()
print("Data has been scraped and saved to business_listings.csv")