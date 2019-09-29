import requests
import json

token = '736784921:AAEhR9Mug25wjZyKEQiz45v200TwjhpsoeA'
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'text': message_text}
    return message


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    up = get_updates()
    m = get_message()
    send_message(m['chat_id'], 'What do you need?')

    with open('bot_updates.json', 'w') as f:
        json.dump(up, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
