from bs4 import BeautifulSoup
import requests

url = "https://www.investopedia.com/financial-edge/0911/top-6-websites-for-finding-financial-stats.aspx"

result = requests.get(url)

print(result.text)