#coding:utf-8
import logging
from redis_cli import listener

def channel_1(pub):
    listener(pub, 'chan-1')
    logging.info("Msg recieved with success")
