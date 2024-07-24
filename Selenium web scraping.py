from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = input("Enter the query: ")
file = 0
numberOfPages = 0

while numberOfPages <= 0:
    numberOfPages = int(input("Enter the number of pages: "))
    if numberOfPages < 1:
        print("Invalid number! Please enter a number higher than 1.")
        continue

for i in range(1, numberOfPages + 1):


    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1PZKYTMRV6AJY&sprefix=samsu%2Caps%2C299&ref=nb_sb_noss_2")

    # time.sleep(3)

    element  = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(element)} items found")

    for elems in element:
        d = elems.get_attribute("outerHTML")
        with open(f"Selenium\Code With Harry\data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
time.sleep(5)
driver.close()