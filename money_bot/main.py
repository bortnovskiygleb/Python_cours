from class_bot import Money_bot
from bot_config import token
from utils import logg_this
import re


def main():
    test_bot = Money_bot(token)
    money = test_bot.get_money()

    answer = test_bot.get_message()
    if answer is None:
        return
    # logg_this(answer)
    chat_id = answer['chat_id']
    text = answer['text']

    if text == '/course':
        test_bot.send_message(chat_id, money)

    if text == '/write':
        test_bot.record_message_to_file()

    if text == '/log':
        logg_this(answer)

    if 'messages ago' in text:
        pattern = r'\s?\d+\s?'
        count_messages = re.search(pattern, text).group().strip()
        test_bot.last_messsages_from_me(int(count_messages))

if __name__ == "__main__":
    main()
