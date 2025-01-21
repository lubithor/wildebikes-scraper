import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.wildebikes.com/collections/bikes'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

products_data = []

products = soup.find_all('div', class_='product-index')
  
for product in products:

    name_tag = product.find('h4', class_='product-title')
    name = name_tag.text.strip() if name_tag else 'No Name'

    price_tag = product.find('div', class_='price__regular')
    price = price_tag.text.strip() if price_tag else 'No Price'

    products_data.append({'Product Name': name, 'Price': price})

csv_file_name = 'wildebike.csv'

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Product Name', 'Price'])
    writer.writeheader()
    for data in products_data:
        writer.writerow(data)

print(f'Data successfully written to {csv_file_name}')
