# Web scraper 
# Finds the following information from bizbuysell.com
"""
1. company website
2. owner name
3. sale price
4. owner email
5. owner phone #
6. broker name
7. broker phone #
8. broker email
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
csv_writer.writerow(["Company URL", "Owner Name", "Sale Price", "Owner Phone", "Owner Email", "Broker Name", "Broker Email"])

# Loop through each listing and extract the required information
for listing in listings:
    company_url = listing.find("a", class_="listing-row-link")["href"]
    owner_name = listing.find("div", class_="listing-owner").get_text(strip=True)
    sale_price = listing.find("div", class_="listing-price").get_text(strip=True)
    owner_phone = listing.find("div", class_="listing-phone").get_text(strip=True)
    owner_email = listing.find("div", class_="listing-email").get_text(strip=True)
    broker_name = listing.find("div", class_="listing-broker-name").get_text(strip=True)
    broker_email = listing.find("div", class_="listing-broker-email").get_text(strip=True)

    csv_writer.writerow([company_url, owner_name, sale_price, owner_phone, owner_email, broker_name, broker_email])

csv_file.close()
print("Data has been scraped and saved to business_listings.csv")