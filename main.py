#coding:utf-8
import asyncio
import redis
import tornado.ioloop
import tornado.web
from client_1 import channel_1
from client_2 import channel_2
from client_3 import channel_3
from client_4 import channel_4

def redis_instance():
    redis_cli = redis.StrictRedis(host='localhost', port=6379, db=0)
    return redis_cli.pubsub()
    
def main():
    pub = redis_instance()
    while True:
        # channel_1(pub)
        # channel_2(pub)
        # channel_3(pub)
        channel_4(pub)

if __name__ == "__main__":
    main()
