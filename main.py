from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("https://www.iris.ma/9-ordinateur?page=3")

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

products = soup.find_all("li", {"class", "col-xs-12"})

product_data = []


def details():
    for i in range(len(products)):
        title = products[i].find("h3", {"class", "product-title"})
        # getting href content Text
        link_href_content = title.find("a").contents[0]
        # product_price_shipping_details
        product_price_shipping_details = products[i].find(
            "div", {"class", "product-price-and-shipping"}
        )
        regular_price = (
            product_price_shipping_details.find("span", {"class", "regular-price"})
            .contents[0]
            .text.strip()
        )
        discount_amount = (
            product_price_shipping_details.find("span", {"class", "discount-amount"})
            .contents[0]
            .text.strip()
        )
        price = (
            product_price_shipping_details.find("span", {"class", "price"})
            .contents[0]
            .text.strip()
        )

        # product-description
        product_description = products[i].find("div", {"class", "product-detail"})
        product_description_Txt_Content = product_description.find("p").text.strip()

        # product-image-url
        product_image_url = products[i].find(
            "img", {"class", "thumbnail_product_listgrid"}
        )["data-src"]
        product_data.append(
            {
                "productTitle": link_href_content,
                "regularPrice": regular_price,
                "discountPrice": discount_amount,
                "Price": price,
                "productDesc": product_description_Txt_Content,
                "productImage": product_image_url,
            }
        )

        keys = product_data[0].keys()

        with open(
            "product_details.csv", "w", encoding="utf-8", newline=""
        ) as output_filter:
            dict_writer = csv.DictWriter(output_filter, keys)
            dict_writer.writeheader()
            dict_writer.writerows(product_data)
            print("data saved successfully...")


details()
