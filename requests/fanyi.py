#_*_ coding:UTF-8 _*_
import io
import sys
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
if __name__ == '__main__':
	target = "http://fanyi.baidu.com/"
	req = requests.get(url = target)
	req.encoding = 'utf-8'
	print(req.text)