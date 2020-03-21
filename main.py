"""
** Personal Project **
This is a personal project for providing updates regarding the COVID-19 outbreak.
Date: 21st March, 2020
Coded by: Abiskar Timsina

"""
from classes.corona_data import *


obj_corona_data = corona_data_scrapper()
obj_corona_news = corona_news_scrapper()

while (1):
    a = input ("Welcome to Webscrepper: ")
    if (a == "!news"):
        obj_corona_news.main()
    elif (a == "!update"):
        obj_corona_data.main()
    else:
        continue
