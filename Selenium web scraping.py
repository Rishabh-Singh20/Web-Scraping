#this file allows you to scrape the data from the desired Amazon product page(s)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = input("Enter the query: ")
file = 0
numberOfPages = 0

#this while loops stops user from entering the value less than 1
while numberOfPages < 1:
    numberOfPages = int(input("Enter the number of pages: "))
    if numberOfPages < 1:
        print("Invalid number! Please enter a number higher than 1.")
        continue

for i in range(1, numberOfPages + 1):

    #looks on the amazon for the desired product
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1PZKYTMRV6AJY&sprefix=samsu%2Caps%2C299&ref=nb_sb_noss_2")

    
    #searches for the all the similar elements having same class name
    element  = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(element)} items found")

    #gets data and exports them to an html file 
    for elems in element:
        d = elems.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
time.sleep(3)
driver.close()
