import requests
from bs4 import BeautifulSoup
from json import loads
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/62.0.3202.89 Safari/537.36'
}


def get_img_url():
    url = 'https://www.douyu.com/directory/game/yz'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    girl_list = soup.select('div[class="items items01 item-data clearfix"]')
    for girl in girl_list:
        li_list = girl.select('li')
        for li in li_list:
            yield li.img['data-original']


def download_pictures(img_url):
    for num, img in enumerate(img_url):
        img_response = requests.get(img)
        # response = requests.get('https://rpic.douyucdn.cn/live-cover/appCovers/2017/12/05/1977639_20171205204858_big.jpg')
        image = img_response.content
        image_path = './pictures/%s.png' % num
        fp = open(image_path, 'wb')
        fp.write(image)
        fp.close()


def get_next_url():
    url_num = 2
    while url_num != 4:
        url = 'https://www.douyu.com/gapi/rkc/directory/2_201/%s' % url_num
        response = requests.get(url, headers=headers)
        res = response.text
        res = loads(res)
        for num, i in enumerate(res['data']['rl']):
            img_response = requests.get(i['rs1'])
            image = img_response.content
            image_path = './pictures%s/%s.png' % (url_num, num)
            fp = open(image_path, 'wb')
            fp.write(image)
            fp.close()
        url_num += 1


def run():
    img_url = get_img_url()
    download_pictures(img_url)
    get_next_url()


if __name__ == '__main__':
    run()
