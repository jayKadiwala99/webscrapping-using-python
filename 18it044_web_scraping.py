from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

source = requests.get('https://www.amazon.in/s?k=mobile&qid=1627188631&ref=sr_pg_1').text
soup = BeautifulSoup(source,'html')


name = []
price = []
string = ""

for i in soup.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
  string = i.text
  name.append(string.strip())

print(name)

for i in soup.find_all('span',class_='a-price-whole'):
  price.append(i.text)


df = pd.DataFrame({'Product Name':name, 'Price':price})
df.to_csv('Webscrap.csv', index=False ,encoding='utf-8')
