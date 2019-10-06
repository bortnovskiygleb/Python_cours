import requests
import json
from mon import *
from time import sleep
from first_crawling import *

token = '736784921:AAEhR9Mug25wjZyKEQiz45v200TwjhpsoeA'
URL = 'https://api.telegram.org/bot' + token + '/'
global last_upd
last_upd = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    if r.status_code != 200:
        print("Error conect")
        return None
    return r.json()


def get_message():
    data = get_updates()
    if data is None:
        return None
    try:
        last_obj = data['result'][-1]
        update_id = last_obj['update_id']

        global last_upd
        if last_upd != update_id:
            last_upd = update_id

            chat_id = last_obj['message']['chat']['id']
            message_text = last_obj['message']['text']

            message = {'chat_id': chat_id,
                       'text': message_text}
            return message
        return None
    except KeyError:
        print("Key erros")
        return 'error'


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    while True:
        answer = get_message()
        if answer == 'error':
            return
        if answer is not None:
            text = answer['text']
            if text == '/mon':
                data = get_money()
                st = 'Сегодня {} курс:\n'.format(data[0]["Date"])
                for i in range(len(data)):
                    st = st + "{} рублей за 1 {}".format(
                            data[i]["Cur_OfficialRate"],
                            data[i]["Cur_Name"])
                    st = st + '\n'
                send_message(answer['chat_id'], st)
            elif text == '/usd':
                data = get_money()
                for i in range(len(data)):
                    if data[i]["Cur_Abbreviation"] == "USD":
                        st = 'За {} курс {} рублей за 1 {}'.format(
                            data[i]["Date"],
                            data[i]["Cur_OfficialRate"],
                            data[i]["Cur_Name"])
                        send_message(answer['chat_id'], st)
            elif text == '/eur':
                data = get_money()
                for i in range(len(data)):
                    if data[i]["Cur_Abbreviation"] == "EUR":
                        st = 'За {} курс {} рублей за 1 {}'.format(
                            data[i]["Date"],
                            data[i]["Cur_OfficialRate"],
                            data[i]["Cur_Name"])
                        send_message(answer['chat_id'], st)
            elif '/rate_date' in text:
                date = text.split(' ')[1]
                data = get_money_on_date(date)
                st = 'За {} курс:\n'.format(data[0]["Date"])
                for i in range(len(data)):
                    st = st + "{} рублей за 1 {}".format(
                            data[i]["Cur_OfficialRate"],
                            data[i]["Cur_Name"])
                    st = st + '\n'
                send_message(answer['chat_id'], st)
            elif text == '/habr_articles':
                data = get_list_articles(
                    get_html("https://habr.com/ru/top/monthly/"))
                st = "Список заголовков статей с хабра за месяц:\n"
                for i in range(len(data)):
                    num = i + 1
                    st = st + str(num) + '. ' + data[i] + '\n'
                send_message(answer['chat_id'], st)
        else:
            continue
            sleep(5)
    # up = get_updates()
    # send_message(m['chat_id'], 'What do you need?')

    # with open('bot_updates.json', 'w') as f:
    #     json.dump(up, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
