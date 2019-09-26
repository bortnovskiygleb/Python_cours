import requests as req
import re
from bs4 import BeautifulSoup as bs


def get_html(url):
    r = req.get(url)
    return r


def get_data_price(html):
    data = html.json()
    for i in range(len(data)):
        print("За {} курс {} рублей за 1 {}".format(
            data[i]["Date"],
            data[i]["Cur_OfficialRate"],
            data[i]["Cur_Name"])
            )


def get_list_articles(html):
    soup = bs(html, 'lxml')
    articles = soup.find_all('article', {'class': ['post post_preview']})
    for art in articles:
        print(art.find('a', {'class': ['post__title_link']}).get_text())

get_data_price(get_html("http://www.nbrb.by/api/exrates/rates?periodicity=0"))
# get_list_articles(get_html("https://habr.com/ru/top/monthly/"))
