#this file allows you to export the scraped data to a CSV file using pandas and beautiful soup

from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text()

        l = soup.find("a")
        link = (f"https://amazon.in/" + l['href'])

        p = soup.find("span", attrs={"class": "a-price-whole"})
        price = p.get_text()

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
    except Exception as e:
        print(e)


df = pd.DataFrame(data=d)
df.to_csv("data.csv")
