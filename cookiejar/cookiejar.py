import urllib.request
import urllib.parse

import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LV1Vv"  #登录成功后的页面url
postdata = urllib.parse.urlencode({
	"username":"weisuen",
	"password":"aA123456"
	}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0")

cjar = http.cookiejar.CookieJar()
#创建处理器：urllib.request.HTTPCookieProcessor(cjar)
#创建opener对象：urllib.request.build_opener()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将opener安装为全局对象
urllib.request.install_opener(opener)
2
file = opener.open(req)
data = file.read()
file = open("C:\\Users\\acer\\Desktop\\pachong\\cookiejar\\5.html",'wb')
file.write(data)
file.close()
url2 = "http://bbs.chinaunix.net/"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("C:\\Users\\acer\\Desktop\\pachong\\cookiejar\\6.html",'wb')
fhandle.write(data2)
fhandle.close()

