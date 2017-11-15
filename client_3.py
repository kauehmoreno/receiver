#coding:utf-8
import logging
from redis_cli import listener

def channel_3(pub):
    listener(pub, 'chan-3')
    logging.info("Msg recieved with success")
