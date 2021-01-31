#_*_ coding:UTF-8 _*_
import io
import sys
import requests
from lxml import etree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
if __name__ == '__main__':
	target = "https://www.vbiquge.com/15_15338/"
	req = requests.get(url = target)
	req.encoding = 'utf-8'
	html=req.text
	xiaoshuo_main = etree.HTML(html)
	xiaoshuo_contain = xiaoshuo_main.xpath('//div[@id="list"]/dl/dd/a');
	for i in xiaoshuo_contain:
		print(i.xpath('text()')[0],'------>','https://www.vbiquge.com/15_15338'+i.xpath('./@href')[0])
#	xiaoshuo_head = xiaoshuo_main.xpath('//div[@id="list"]/dl/dd/a/text()')
#	xiaoshuo_href = xiaoshuo_main.xpath('//div[@id="list"]/dl/dd/a/@href')
#	for i,j in xiaoshuo_head,xiaoshuo_href:
#		print(i),print(j)
#print(xiaoshuo_head)
	