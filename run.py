#!/usr/bin/python3.9
# coding:utf-8

import os
import sys
import twitter
import logging
import configparser
import numpy

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

def main():
    blocklist = numpy.loadtxt('blocklist.txt', comments="#", dtype=str, delimiter='\n')
    twitter_api = twitter.Api(consumer_key=config['API']['CONSUMER_KEY'], consumer_secret=config['API']['CONSUMER_SECRET'], access_token_key=config['API']['ACCESS_KEY'], access_token_secret=config['API']['ACCESS_SECRET'], input_encoding='utf-8')
    for blocktarget in blocklist:
        try:
            blocked = twitter_api.CreateBlock(screen_name=blocktarget)
            print ('Blocked user: [ @%s ].' % blocktarget)
        except:
            pass

if __name__ == '__main__':
    main()