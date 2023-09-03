# Web scraper 
# Finds the following information from bizbuysell.com
"""
1. company website
2. owner name
3. owner email
4. owner phone #
5. broker name
6. broker phone #
7. broker email
"""

# to implement: filter by company ARR 

# input the bizbuysell page, pre-filtered by geographic location, industry, price range, revenue, etc...
import requests
from bs4 import BeautifulSoup
import urllib.parse

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

# Loop through each listing and extract the required information
for listing in listings:
    company_url = listing.find("a", class_="listing-row-link")["href"]
    owner_name = listing.find("div", class_="listing-owner").get_text(strip=True)
    sale_price = listing.find("div", class_="listing-price").get_text(strip=True)

    print("Company URL:", company_url)
    print("Owner Name:", owner_name)
    print("Sale Price:", sale_price)
    print("=" * 40)  # Print a separator between listings
