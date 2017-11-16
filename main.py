#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import urllib
import urllib.request

from slacker import Slacker

slack = Slacker('TOKEN-SLACK-BOT')

TIMERSLEEP = 5
PAUSE = 20

site_pages = [
'https://yandex.ru',
'https://google.com'
]

failed_pages = []

def check_pages(pages):
    fail_c = int(0)

    while True:
        try:
            for page_url in pages:
                code = urllib.request.urlopen(page_url, timeout=15).getcode()
                t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
                if (code not in [200, 301]):
                    failed_pages.append(page_url)
		    slack.chat.post_message('#checkpages', 'Error: ' + t_error + "{0} - {1}".format(page_url, code))
        except OSError as e:
            t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000 ", time.gmtime())
            fail_c += 1
            if fail_c == 3:
		slack.chat.post_message('#checkpages', 'Error socket: ' + t_error  + str(e))
		fail_c = 0
            time.sleep(PAUSE)

check_pages(site_pages)
