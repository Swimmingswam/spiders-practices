import re
import urllib.request
url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%AD%E5%B1%B1&kw=%E5%89%8D%E7%AB%AF&isadv=0&sg=4ebb3271edc94e21b03d25bd2d81d443&p=1"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.add_header = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8")
data= str(data)
namepat = '<a style="font-weight: bold" par="ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=4ebb3271edc94e21b03d25bd2d81d443&amp;(.*?)</a>'
moneypat = '<td class="zwyx">(.*?)</td>'
addresspat = '<td class="gzdd">(.*?)</td>'
companypat = '<a href="http://company.zhaopin.com/CC(.*?)</a>'
namelist = re.compile(namepat,re.S).findall(data)
moneylist = re.compile(moneypat,re.S).findall(data)
addresslist = re.compile(addresspat,re.S).findall(data)
companylist = re.compile(companypat,re.S).findall(data)
for i in range(0,5):
		print("------------------")
		print("职位是："+namelist[i])
		print("薪资是："+moneylist[i])
		print("地址是："+addresslist[i])
		print("公司是："+companylist[i])
#http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%AD%E5%B1%B1&kw=%E5%89%8D%E7%AB%AF&isadv=0&sg=4ebb3271edc94e21b03d25bd2d81d443&p=2
#https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%AD%E5%B1%B1&kw=%E5%89%8D%E7%AB%AF&p=1&isadv=0
#<a style="font-weight: bold" par="ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=4ebb3271edc94e21b03d25bd2d81d443&amp;so=1" href="http://jobs.zhaopin.com/207959039273160.htm" target="_blank">急聘WEB<b>前端</b>开发助理/学徒接受应届生+双休</a>
#<td class="gsmc"><a href="http://company.zhaopin.com/CC207959039.htm" target="_blank">佛山海联中兴企业管理中心</a>
'''
import re
import urllib.request
#url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%AD%E5%B1%B1&kw=%E5%89%8D%E7%AB%AF&isadv=0&sg=4ebb3271edc94e21b03d25bd2d81d443&p=1"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.add_header = [headers]
urllib.request.install_opener(opener)
namepat = '<a style="font-weight: bold" par="ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=4ebb3271edc94e21b03d25bd2d81d443&amp;(.*?)</a>'
moneypat = '<td class="zwyx">(.*?)</td>'
addresspat = '<td class="gzdd">(.*?)</td>'
companypat = '<a href="http://company.zhaopin.com/CC(.*?)</a>'
def getdata(url,page):
	url = url + str(page)
	data = urllib.request.urlopen(url).read().decode("utf-8")
	data= str(data)
	return data
for i in range(1,6):
	url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=%E5%89%8D%E7%AB%AF&isadv=0&sg=db4fc9a3f17543d19488e697918a1629&p='
	print("--------"+"第"+str(i)+"页"+"----------")
	data = getdata(url,i)
	print(1)
	namelist = re.compile(namepat,re.S).findall(data)
	moneylist = re.compile(moneypat,re.S).findall(data)
	addresslist = re.compile(addresspat,re.S).findall(data)
	companylist = re.compile(companypat,re.S).findall(data)
	print(2)
	for j in range(0,5):
		print("职位是："+namelist[j])
		print("薪资是："+moneylist[j])
		print("地址是："+addresslist[j])
		print("公司是："+companylist[j])
'''
'''
# coding:utf-8
from urllib import request,parse
import json
from pandas import DataFrame
from lxml import etree
import random
import math
import time

def get_city_list():
    base_url = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E6%B7%B1%E5%9C%B3'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'Cookie': 'user_trace_token=20170823172848-77f8f03e-87e5-11e7-9ed0-525400f775ce; LGUID=20170823172848-77f8f6f1-87e5-11e7-9ed0-525400f775ce; JSESSIONID=ABAAABAACBHABBI08566127D8146453353170657FD7089A; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=CD839C2A99BB2E8F; login=true; unick=%E5%BC%A0%E5%8F%88%E4%BA%AE; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=44; TG-TRACK-CODE=search_code; SEARCH_ID=201ece3cee414cfdb6e8461e5484ff28; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.943013801.1503976181; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504012158,1504059663,1504116125,1504140367; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504140876; _ga=GA1.2.279566316.1503480294; LGSID=20170831085014-59a334e8-8de6-11e7-9f82-525400f775ce; LGRID=20170831085842-887351d7-8de7-11e7-9f97-525400f775ce',
                'Host': 'www.lagou.com',
                'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E5%85%A8%E5%9B%BD',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                }
    req=request.Request(base_url,headers=headers,method='GET')
    response=request.urlopen(req)
    html=response.read().decode('utf-8')
    selector=etree.HTML(html)
    city1=selector.xpath('//li[@class="hot"]/a/text()')
    city2=selector.xpath('//li[@class="other"]/a/text()')
    city=city1+city2
    city.pop(0)
    city.pop(-1)
    return city

def page_counts(totalCount):
    pages=math.ceil(totalCount/float(15))
    if pages>30:
        pages=30
    return pages

def get_html(url,header,pn=1):
    formdata = {'first': 'true', 'pn': pn, 'kd': '数据分析'}
    data = bytes(parse.urlencode(formdata), encoding='utf-8')
    req = request.Request(url, data, header, method='POST')
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    #time.sleep(5)
    return html

def get_city_pages(url,header):
    referer = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city={a}'
    cities = get_city_list()
    print(cities)
    data=[]
    for eachCity in cities:
        scity = parse.quote(eachCity)
        url1 = url.format(b=str(scity))
        #header.pop('Referer')
        referer1 = referer.format(a=scity)
        header['Referer'] = referer1
        html = get_html(url1,header)
        # 转化为json
        jdict = json.loads(html)
        jcontent = jdict['content']
        jpositionResult = jcontent['positionResult']
        totalCount = jpositionResult['totalCount']
        data.append([totalCount,url1,referer1])
    return data

if __name__ == '__main__':
    iplist=['14.153.53.123:3128','113.105.146.77:8086','219.135.164.250:8080','219.128.75.149:8123']
    proxy_support=request.ProxyHandler({'http':random.choice(iplist)})
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)
    json_url = 'https://www.lagou.com/jobs/positionAjax.json?city={b}&needAddtionalResult=false&isSchoolJob=0'
    json_headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Length': '55',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
               'Cookie':'user_trace_token=20170823172848-77f8f03e-87e5-11e7-9ed0-525400f775ce; LGUID=20170823172848-77f8f6f1-87e5-11e7-9ed0-525400f775ce; JSESSIONID=ABAAABAACBHABBI08566127D8146453353170657FD7089A; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=CD839C2A99BB2E8F; login=true; unick=%E5%BC%A0%E5%8F%88%E4%BA%AE; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=44; _gid=GA1.2.943013801.1503976181; _ga=GA1.2.279566316.1503480294; LGSID=20170831085014-59a334e8-8de6-11e7-9f82-525400f775ce; LGRID=20170831085859-92c5f026-8de7-11e7-9f98-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504012158,1504059663,1504116125,1504140367; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504140893; TG-TRACK-CODE=search_code; SEARCH_ID=318e5a8812994350a50e589a318bd332; index_location_city=%E6%B7%B1%E5%9C%B3',
               'Host': 'www.lagou.com',
               'Origin': 'https://www.lagou.com',
               'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E6%B3%89%E5%B7%9E',
               'X-Anit-Forge-Code': '0',
               'X-Anit-Forge-Token': 'None',
               'X-Requested-With': 'XMLHttpRequest'
               }

    positionName = []#职位名称
    positionLables=[]#职位标签
    firstType=[]#职位类型1
    secondType=[]#职位类型2
    bussinessZones=[]#工作地段
    district=[]#工作区域
    city = []#所在城市
    education=[]#教育背景
    workYear=[]#工作年限
    salary = []#薪酬
    companyName = []#公司名字
    companySize = []#公司规模
    companyStage=[]#发展状况
    industryField=[]#经营范围
    totalCounts=[]#城市职位数量
    positionIds= []  # 职位ID
    data=get_city_pages(json_url,json_headers)
    for totalCount,url,refer in data:
        pages=page_counts(totalCount)
        json_headers['Referer']=refer
        while pages>0:
            if pages>9:
                json_headers['Content-Length']=56
            else:
                json_headers['Content-Length']=55
            html=get_html(url,json_headers,pn=pages)
            jdict = json.loads(html)
            jcontent = jdict['content']
            jpositionResult = jcontent['positionResult']
            jresult = jpositionResult['result']
            for each in jresult:
                positionName.append(each['positionName'])
                positionLables.append(each['positionLables'])
                firstType.append(each['firstType'])
                secondType.append(each['secondType'])
                bussinessZones.append(each['businessZones'])  # 工作地段
                district.append(each['district'])  # 工作区域
                city.append(each['city'])
                education.append(each['education']) # 教育背景
                workYear.append(each['workYear'])  # 工作年限
                salary.append(each['salary'])
                companyName.append(each['companyFullName'])
                companySize.append(each['companySize'])
                companyStage.append(each['financeStage'])  # 发展状况
                industryField.append(each['industryField']) # 经营范围
                totalCounts.append(totalCount)
                positionId=each['positionId']
                positionIds.append(positionId)
            pages = pages - 1
    positionData = {'positionName': positionName, 'positionLables': positionLables, 'positionType1':firstType,'postionType2':secondType,'bussinessZones':bussinessZones,'district':district,'city':city,'education':education,'workYear':workYear,'salary': salary, 'companyName': companyName, 'companySize': companySize, 'financeStage':companyStage,'industryField':industryField,'cityPositionCounts': totalCounts,'positionID':positionIds}
    frame = DataFrame(positionData)
    frame.to_csv('LagouPositionSociety.csv', index=False, na_rep='NULL')
'''
