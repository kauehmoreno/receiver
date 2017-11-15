#coding:utf-8
import logging
from redis_cli import listener

def channel_2(pub):
    listener(pub, 'chan-2')
    logging.info("Msg recieved with success")
