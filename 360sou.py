import requests
try:
	keyword = {'q':'python'}
	url = 'http://www.so.com/s'
	r = requests.get(url,params=keyword)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print('爬取失败')