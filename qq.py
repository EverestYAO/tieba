from urllib.request import Request, urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup
import re

print('https://v.qq.com/x/page/h03425k44l2.html\n \
https://v.qq.com/x/cover/dn7fdvf2q62wfka/m0345brcwdk.html\n \
http://v.qq.com/cover/2/2iqrhqekbtgwp1s.html?vid=c01350046ds')
url = input('请输入网址:')
if re.search(r'vid=',url) :
    patten =re.compile(r'vid=(.*)')
    vid=patten.findall(url)
    vid=vid[0]

else:
    newurl = (url.split("/")[-1])
    vid =newurl.replace('.html', ' ')



changeurl='http://vv.video.qq.com/geturl?vid={vid}&otype=xml&platform=1&ran=0%2E9652906153351068'.format(vid=vid.strip())
req = Request(changeurl)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
req.add_header('User-Agent', user_agent)
try:
    response = urlopen(changeurl)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code:', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason:', e.reason)
html = response.read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('url'):
    print(link.get_text())


