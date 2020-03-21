import requests as req
from bs4 import *

url = req.get('https://myrepublica.nagariknetwork.com/category/coronavirus').text
empty_list = []
page = BeautifulSoup(url,'lxml')

main_heading = page.find_all('div', class_ ='col-sm-8')

for heading in main_heading:
    title = heading.h2
    print(title.text)
    sub_t = heading.find_all('p')
    for sub_topic in sub_t:
        empty_list.append(sub_topic.text)
    formatting = "> "+ str(empty_list[1])
    print(formatting)
    empty_list = []
    print()

