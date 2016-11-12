#-*- coding: UTF-8 -*-
from urllib.request import Request, urlopen
from urllib.error import URLError,HTTPError
import re
import sys





url = 'http://www.toutiao.com/a6349423666450743554/'
req = Request(url)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
req.add_header('User-Agent' ,user_agent)
try:
	response = urlopen(req)
except HTTPError as e:
	print ('The server couldn\'t fulfill the request.')
	print ('Error code:',e.code)
except URLError as e:
	print('We failed to reach a server.')
	print('Reason:',e.reason)
html = response.read().decode('utf-8')



