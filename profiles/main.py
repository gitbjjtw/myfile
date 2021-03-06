import requests
import os


def send_msg_to_me(msg):
    CHAT_ID = os.environ['TG_CHAT_ID']
    TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
    BOT_MSG_URL = 'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'.format(BOT_TOKEN=TG_BOT_TOKEN)

    r = requests.post(BOT_MSG_URL, data={'chat_id': CHAT_ID, 'text': msg})


if __name__ == '__main__':
    send_msg_to_me('refresh proxy config file')

    with open('tmp.txt') as f:
        for l in f:
            send_msg_to_me(l.strip())

    send_msg_to_me('done')
