# -*- coding: utf-8 -*-

#import urllib2
import urllib
import re

# 构造headers
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
           'Refer': 'http://image.baidu.com/search/index'}

url = 'http://image.baidu.com/search/index'
params = {'tn': 'baiduimage',
          'ps': '1',
          'ct': '201326592',
          'lm': '-1',
          'cl': '2',
          'nc': '1',
          'ie': 'utf-8',
          'word': '妹子'}

imgUrl = 'http://image.baidu.com/search/acjson'
imgParam = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': 201326595,
    'is': '',
    'fp': 'result',
    'queryWord': '汽车',
    'cl': '2',
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': -1,
    'z': '',
    'ic': '',
    'word': '汽车',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '',
    'istype': '',
    'qc': '',
    'nc': 1,
    'fr': '',
    'pn': '60',
    'rn': '60',
    'gsm': '1e',
    '1480836955942': ''}

# 编码参数
data = urllib.urlencode(params)
imgData = urllib.urlencode(imgParam)

# 构造GET请求URL
requestUrl = url+'?'+data
imgRequestUrl = imgUrl+'?'+imgData

# 请求数据
request = urllib.Request(requestUrl)
response = urllib.urlopen(request)
result = response.read()
result = result.replace('\\', '')
# 抽取地址
urls = re.findall(r'http://[^"]+jpg', result, re.I)
print(len(urls))
for item in urls:
    print(item)

print('that is all')
