#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, urllib, socket
from slacker import Slacker

slack = Slacker('TOKEN-SLACK-BOT')

TIMERSLEEP = 15
PAUSE = 60

site_pages = [
'https://google.com',
'https://yandex.ru'
]

failed_pages = [];

def check_pages (pages):
	while True:
		try:
			for page_url in pages:
				code = urllib.request.urlopen(page_url, timeout=15).getcode()
				time.sleep(TIMERSLEEP)
				t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
				if (code not in [200, 301]):
					failed_pages.append(page_url)
					slack.chat.post_message('#checkpages', 'Error: ' + t_error + "{0} - {1}".format(page_url, code))
		except socket.error as e:
			t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
			slack.chat.post_message('#checkpages', 'Error socket: ' + t_error)
			time.sleep(PAUSE)

check_pages(site_pages)
