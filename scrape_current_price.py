from bs4 import BeautifulSoup
import requests
import re #imports regular expression in Python

url = "https://seekingalpha.com/symbol/MU"

result = requests.get(url).text

doc = BeautifulSoup(result, 'html.parser')

current_price = doc.find('span',{'data-test-id':'symbol-price'})
print(current_price.text)

#<span jsname="vWLAgc" class="IsqQVc NprOob wT3VGc">49.88</span>

# <div id="sdp-price-chart-price-change" class="css-gg4vpm"><div><div class="css-1tqud6q"><span class="css-hw40uo">-$1.37 (-2.69%)</span><span class="css-o58iq6">Today</span></div><div class="css-1tqud6q"></div></div></div>

#<span class="ktG blcD buK bu1 bu6" data-test-id="symbol-price">$<!-- -->49.41</span>