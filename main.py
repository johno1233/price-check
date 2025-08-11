# To Do
# 1. Get user input for a product (product specificity is a must)
# 2. Search the interwebs for said product: Maybe start w/ a set of predetermined sites (amazon, ebay, walmart, etc)
# 3. return pricing information: This includes website url, price, and price rank (1 being the lowest price) 
#       3a. If pricing is on FB market place/Ebay/Other used market places, denote USED
# 4. Output the results in a table w/ headers Item, Seller, URL, Price
# 5. Once this is all working, wrap it up in a nice GUI to make it user friendly

from bs4 import BeautifulSoup # our html parser
import requests # our html requester

def has_class_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

product = input("Enter a product name: ")

# amazon handles searches via: https://www.amazon.com/s?k=gloves
#turn this into a dictionary later on to handle multiple websites searching from

url = f"https://www.amazon.com/s?k={product}"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8', 'Accept-Language': 'en-US,en;q=0.5'}

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text, 'html.parser')

# Price information for amazon is stored: 
# <span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$0.24</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">0<span class="a-price-decimal">.</span></span><span class="a-price-fraction">24</span></span></span>
#span_tags = soup.find_all("div") # gets all instances of the "span" tag in req.text
#print(span_tags)
all_class = soup.find_all(has_class_no_id)

