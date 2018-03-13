'''
import requests
try:
	keyword = {'wd':'python'}
	url = 'http://www.baidu.com/s'
	r = requests.get(url,params=keyword)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print('爬取失败')
'''
import urllib.request
keyword = input("请输入搜索关键字：")
url = "http://www.baidu.com/s?wd="
try:
	urlall = url+keyword
	req = urllib.request.Request(urlall)
	#req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
	data = urllib.request.urlopen(req).read()
except:
	keyword_code = urllib.request.quote(keyword)
	urlall = url+keyword_code
	req = urllib.request.Request(urlall)
	#req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
	data = urllib.request.urlopen(req).read()
fhandle = open("C:\\Users\\acer\\Desktop\\pachong\\baidusou\\3.html","wb")
fhandle.write(data)
fhandle.close()