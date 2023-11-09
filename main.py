import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("https://www.iris.ma/9-ordinateur")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("li", {"class", "col-xs-12"})

def details():
    for i in range(len(products)):
        title = products[i].find("h3", {"class", "product-title"})
        # getting href content Text
        link_href_content = title.find("a").contents[0]
        # product_price_shipping_details
        product_price_shipping_details = products[i].find(
            "div", {"class", "product-price-and-shipping"}
        )
        regular_price = product_price_shipping_details.find(
            "span", {"class", "regular-price"}
        ).contents[0]
        discount_amount = product_price_shipping_details.find(
            "span", {"class", "discount-amount"}
        ).contents[0]
        price = product_price_shipping_details.find(
            "span", {"class", "price"}
        ).contents[0]

        print(regular_price, discount_amount, price)


details()
