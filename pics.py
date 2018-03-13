'''import requests
path = 'D:/abj.jpg'
url = 'http://image.nationalgeographic.com.cn/2018/0104/20180104120546447.jpg'
r = requests.get(url)
try:
	with open(path,'wb') as f:
		f.write(r.content)
		f.close()
	print('保存成功')
except:
	print('保存失败')
'''
import requests
import os
url = 'http://image.nationalgeographic.com.cn/2018/0104/20180104120546447.jpg'
root = 'D://pics//'
path = root + url.split('/')[-1]
r = requests.get(url)
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print('保存成功')
	else:
		print('文件已存在')
except:
	print('爬取失败')
	print(r.status_code)
