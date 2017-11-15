#coding:utf-8
import logging
from redis_cli import listener

def channel_4(pub):
    listener(pub, 'chan-4')
    logging.info("Msg recieved with success")
