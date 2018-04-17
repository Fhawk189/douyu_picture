# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from json import loads
# from PIL import Image
# from io import BytesIO
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/62.0.3202.89 Safari/537.36'
}

url_num = '2'
url = 'https://www.douyu.com/gapi/rkc/directory/2_201/%s' % url_num
response = requests.get(url, headers=headers)
res = response.text
res = loads(res)
for num, i in enumerate(res['data']['rl']):
    img_response = requests.get(i['rs1'])
    Image = img_response.content
    Image_path = './pictures2/%s.png' % num
    fp = open(Image_path, 'wb')
    fp.write(Image)
    fp.close()
# soup = BeautifulSoup(response.text, 'html.parser')
# girl_list = soup.select('div[class="items items01 item-data clearfix"]')
# for girl in girl_list:
#     li_list = girl.select('li')
#     for li in li_list:
#         img_response = li.img['data-original']
#         Image = img_response.content
#         Image_path = './pictures2/%s.png' % num
#         fp = open(Image_path, 'wb')
#         fp.write(Image)
#         fp.close()
