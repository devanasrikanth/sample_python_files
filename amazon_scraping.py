
"""
This script takes as input a csv file which has list of items from amazon with their price.
The script reads each row for the url and the price and
checks whether the price today on the website url is same as the price that we already have

If the prices are different, script writes the details to a
different file, which is used to update the price on our website.
"""
import csv
import urllib
from bs4 import BeautifulSoup


def checkPrice(item_url, item_price, items=None):
    """
    This function gets called for each row which contains url and price.
    This function parses the url for the current price on amazon and
    if the current price is different to what we already have, then writes the details
    to a dictionary
    """
    print "Checking price for url : ", item_url
    print "Existing price of item : ", item_price
    try:
        htmltext = urllib.urlopen(item_url).read()
    except:
        print "Do nothing and move onto next url"

    soup = BeautifulSoup(htmltext)
    #priceLarge tag contains the current price of the item on amazon
    newprice = soup.find('b', {"class": "priceLarge"})
    # If the tag is not found, then do not write anything
    if newprice is not None:
        print "Current price of item is : ", newprice.string
        if items is None:
            items = []
        # if the current price is not equal to existing price, then write onto dict
        if round(float(item_price)) != round(float(newprice.string[1:])):
            items.append({'url': item_url, 'price': newprice.string[1:]})


items = []  # Contains the dictionary of items that changed value
# Open the file CSV containing the list of amazon URL's for the items with their price
with open('amazon_url.csv', 'rb') as csvfile:

    # Keep each item and price in a dictionary
    reader = csv.DictReader(csvfile)
    for row in reader:
        checkPrice(row['url'], row['price'], items)

fieldnames = ['url', 'price', ]
with open('changed_items.csv', 'wb') as changes:
    writer = csv.DictWriter(changes, delimiter=',', fieldnames=fieldnames)
    # Write the fieldnames onto the file
    writer.writerow(dict((fn, fn) for fn in fieldnames))
    # Write url and price of changed items onto file.
    for row in items:
        writer.writerow(row)
