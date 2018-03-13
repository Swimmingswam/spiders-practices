# -*- coding: utf-8 -*- 
import requests
import re
def getHTMLText(url):    #获得整个html页面
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  #文本解析编码替换整体解析编码
        return r.text
    except:
     return("")
def parsePage(ilt,html):   #解析每一个html页面
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)  #定义获取价格信息列表
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)   #定义获取商品名称信息列表
        for i in range(len(plt)):   #键值信息关联
            price = eval(plt[i].split(':')[1])  #获取价格部分
            title = eval(tlt[i].split(':')[1])  #获取名称部分
            ilt.append([price,title])
    except:
        print("")
def printGoodsList(ilt):   #将爬取的信息输出到屏幕
    tplt = "{:4}\t{:8}\t{:16}"   #定义展示模板
    print(tplt.format('序号','价格','商品名称'))   #打印表头
    count = 0  #定义输出信息计数器
    for g in ilt:
        count = count + 1   #商品打印序列号
        print(tplt.format(count,g[0],g[1]))    
def main():    #综合上面的主函数
    goods = '书包'   #搜索关键字
    depth = 2   #设置爬取页面数
    start_url = 'https://s.taobao.com/search?q='+'goods'  #爬取的url
    infoList = []   #定义输出结果
    for i in range(depth):  #对单个页面进行处理
        try:
            url = start_url+'&s='+str(44*i)  #修饰url
            html = getHTMLText(url)  #获得网页
            parsePage(infoList,html)  #解析网页
        except:
            continue   #遇到错误就直接进行下一遍历
        printGoodsList(infoList)  #打印出结果
main()   #启动主函数爬取信息