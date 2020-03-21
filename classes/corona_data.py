"""
** Personal Project **
This is a personal project for providing updates regarding the COVID-19 outbreak.
Date: 21st March, 2020
Coded by: Abiskar Timsina

"""

# importing necessary modules
import requests as req
from bs4 import *
import sys

class corona_data_scrapper:

    def data_scrapper(self,up_url):
        url = up_url
        temp_list = []
        soup = BeautifulSoup(url, 'lxml')
        body = soup.find('div', class_="table-scroll")
        table_row = body.table.tbody.find_all('tr')

        for exit_control, data in enumerate(table_row):
            table_row_data = data.find_all('td')
            for ind_data_row in table_row_data:
                temp_format1 = ind_data_row.text.replace('\n', ' ')
                temp_list.append(temp_format1)
            print(temp_list)
            print()
            temp_list = []
            if (exit_control == 4):
                break

    def main(self):
        try:
            unparsed_url = req.get("https://virusncov.com/").text
            self.data_scrapper(unparsed_url)
        except:
            print('The bot cannot retrieve the requested info. Check your connection and try again later.')
            sys.exit()




class corona_news_scrapper:

    # initializing the url and parsing the data.
    def news_scrapper(self,unparsed_input_url):
        unparsed_url = unparsed_input_url
        temp_list = []
        url = BeautifulSoup(unparsed_url, 'lxml')

        # finding the required headings
        main_heading = url.find_all('div', class_='col-sm-8')

        # iterating over all the latest news articles.
        for article_no, headings in enumerate(main_heading):
            title = headings.h2
            format1 = str(article_no + 1) + ". " + str(title.text)
            print(format1)
            sub_topics = headings.find_all('p')
            for sub_topic in sub_topics:
                temp_list.append(sub_topic.text)
            format2 = "- " + str(temp_list[1])
            print(format2)
            temp_list = []
            print()

    def main(self):
        try:
            target_url = req.get('https://myrepublica.nagariknetwork.com/category/coronavirus', timeout=5).text
            self.news_scrapper(target_url)
        except:
            print('The bot cannot retrieve the requested info. Check your connection and try again later.')
            sys.exit()


