import requests as req
import re
from bs4 import BeautifulSoup as bs


def get_html(url):
    r = req.get(url)
    return r.text


def get_data_cash(html):
    soup = bs(html, 'lxml')
    data = soup.getText()[2:len(soup.getText()) - 2].split("},{")
    for line in data:
        infs = line.split(",")
        d = {}
        for inf in infs:
            inf = inf.replace("\":", "\" : ")
            f = inf.split(' : ')
            d[f[0]] = f[1]
        print("За {} курс {} рублей за 1 {}".format(d["\"Date\""][1: -1],
                                                    d["\"Cur_OfficialRate\""],
                                                    d["\"Cur_Name\""][1: -1]))


def get_list_articles(html):
    soup = bs(html, 'lxml')
    articles = soup.find_all('article', {'class': ['post post_preview']})
    for art in articles:
        print(art.find('a', {'class': ['post__title_link']}).get_text())

# get_data_cash(get_html("http://www.nbrb.by/api/exrates/rates?periodicity=0"))
get_list_articles(get_html("https://habr.com/ru/top/monthly/"))
