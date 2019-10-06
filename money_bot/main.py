from class_bot import Money_bot
from bot_config import token
from utils import logg_this

test_bot = Money_bot(token)
money = test_bot.get_money()

answer = test_bot.get_message()
# logg_this(answer)
chat_id = answer['chat_id']
text = answer['text']

if text == '/course':
    test_bot.send_message(chat_id, money)

if text == '/write':
    test_bot.record_message_to_file()

if text == '/log':
    logg_this(answer)
