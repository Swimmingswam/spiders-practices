import requests
url = 'https://www.amazon.cn/dp/B06XCCTS9M'
try:
	kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get(url,headers = kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[2000:3000])
except:
	print("爬取失败")
	print(r.status_code)