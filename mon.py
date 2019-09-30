import requests
import json


def get_money():
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    response = requests.get(url).json()
    return response


def get_money_on_date(date):
    date = date.split('-')
    url = 'http://www.nbrb.by/api/exrates/rates?ondate={year}-{month}-{day}&periodicity=0'.format(
        day=date[0],
        month=date[1],
        year=date[2]
    )
    response = requests.get(url).json()
    return response


# get_money()
