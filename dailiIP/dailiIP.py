def use_proxy(proxy_addr,url):
	import urllib.request
	proxy = urllib.request.ProxyHandler({'http':proxy_addr})
	opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(url).read().decode("utf-8")
	return data
proxy_addr = "139.196.122.166:8080"
url = "http://www.baidu.com"
use_proxy(proxy_addr,url)
print(len(data))

