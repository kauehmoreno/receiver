#coding:utf-8
import redis
import logging

def listener(pub, chan):
    pub.subscribe(chan)
    msg = pub.get_message()
    if msg:
        if not isinstance(msg.get('data'), int):
            logging.error(msg.get('channel').decode('utf-8'))
            logging.error(chan)
            if msg.get('channel') == bytes(chan, 'utf-8'):
                logging.error(msg)
                with open('{}.txt'.format(chan), 'w') as f:
                    f.write(str(msg.get('data')))
                # f.close()
    # else:
        # logging.error('Waiting for msg')
