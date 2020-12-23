import reqeusts


def send_msg_to_me(msg):
    r = requests.post(BOT_MSG_URL, data={'chat_id': CHAT_ID, 'text': msg})
    return r


if __name__ == '__main__':
    with open('tmp.txt') as f:
        for l in f:
            send_msg_to_me(l.strip())
