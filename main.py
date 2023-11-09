import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("https://www.iris.ma/")

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

title = soup.find_all("div", {"class", "product-description"})
print(title)
