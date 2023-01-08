#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import urllib.request
from slacker import Slacker

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TOKEN-SLACK-BOT = os.environ.get("TOKEN-SLACK-BOT")
SLACK_CHAT = os.environ.get("SLACK_CHAT")
TIMERSLEEP = os.environ.get("TIMERSLEEP")
PAUSE = os.environ.get("PAUSE")
FAIL_CHECK = os.environ.get("FAIL_CHECK")
REQ_TIMEOUT = os.environ.get("REQ_TIMEOUT")

slack = Slacker(TOKEN-SLACK-BOT)

site_pages = [
'https://yandex.ru',
'https://google.com'
]

def check_pages(pages):
    fail_c = int(0)
    failed_pages = []

    while True:
        try:
            for page_url in pages:
                code = urllib.request.urlopen(page_url, timeout=REQ_TIMEOUT).getcode()
                t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
                if (code not in [200, 301]):
                    failed_pages.append(page_url)
		    slack.chat.post_message(SLACK_CHAT, 'Error: ' + t_error + "{0} - {1}".format(page_url, code))
        except OSError as e:
            t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000 ", time.gmtime())
            fail_c += 1
            if fail_c == FAIL_CHECK:
		slack.chat.post_message(SLACK_CHAT, 'Error socket: ' + t_error  + str(e))
		fail_c = 0
            time.sleep(PAUSE)
	except KeyboardInterrupt:
	    # User interrupt the program with ctrl+c
	    exit()
	
if __name__ == "__main__":
    check_pages(site_pages)
