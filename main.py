#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, urllib, socket
from slacker import Slacker

slack = Slacker('TOKEN-SLACK-BOT')

TIMERSLEEP = 10

site_pages = [
'https://google.com',
'https://yandex.ru'
]

failed_pages = [];

def check_pages (pages):
  while True:
		time.sleep(TIMERSLEEP)
		try:
			for page_url in pages:
				code = urllib.request.urlopen(page_url).getcode()
				t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
				if (code not in [200, 301]):
					failed_pages.append(page_url)
					slack.chat.post_message('#checkpages', 'Error: ' + t_error + "{0} - {1}".format(page_url, code))
		except socket.error as e:
			t_error = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
			slack.chat.post_message('#checkpages', 'Error socket: ' + t_error)

check_pages(site_pages)
