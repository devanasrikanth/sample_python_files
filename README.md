sample_python_files
===================

This repo contains two files amazon_scraping.py and coolstuffinoneplace.py

amazon_scraping.py
------------------
This script takes as input a csv file which has list of items from amazon with their price.
The script reads each row for the url and the price and
checks whether the price today on the website url is same as the price that we already have

If the prices are different, script writes the details to a
different file, which is used to update the price on our website.

This script is used in the coolstuffinoneplace.co.uk website.

coolstuffinoneplace.py
----------------------
This file consists a sample of functions that are written for landing page and gadgets tag on coolstuffinoneplace.co.uk

def homepage:  This function returns the list of items to display on the landing page.
                On the landing page, we will be displaying only the latest 3 items with high ranking 
                from the past 2 weeks and any other items before that based on the rank.
                This function gets called each time everytime user scrolls on the page.
                
                The database request to get all the items is called only once.
                Each time user scrolls on the page, we use the items from the list
                that are already retrieved and display them
                
def gadget_category : This function returns the list of items classes as gadgets.
                      This function gets called when user clicks on the gadgets tab on the menu.
