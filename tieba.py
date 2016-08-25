#-*- coding: UTF-8 -*-
import urllib
import urllib2
import re
import sys
def open_url(url2):
	req = urllib2.Request(url2)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
	headers = {'User-Agent' : user_agent}
	try:page = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print e.reason
		
	html = page.read().decode('utf-8')
	return html
	
def get_img(html):
	p = re.compile(r'src="([^"]+\.jpg)"')
	imglist = p.findall(html)
	i = 1
	for each in set(imglist):
		filename = each[-8:]
		try:
			urllib.urlretrieve(each,filename,None)
			print "downloading" + str(i) + "个新垣结衣"
		except:
			print "Unexpected error:", sys.exc_info()[0]
		i+= 1
def start():
	for j in range(1,pages+1):
		url2 = url + str(j)
		get_img(open_url(url2))
		print '已经爬取了第 ' + str(j) + ' 页'
if __name__=='__main__':
	url = raw_input('输入网址，把pn=后面的数字去掉')
	pages = int(raw_input('该帖子有多少页？'))
	start()