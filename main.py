import random
import time
from base64 import b64decode
from json import loads
from socket import socket
from threading import Thread

from lxml import etree
import requests
import re

from http_server import localIp


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_type():
    a = 1234
    print(type(a))


def operate():
    print(9 / 2)
    print(9 % 2)
    print(9 // 2)
    print(9 ** 2)


def form():
    print("身高%.1f 重%.2f" % (175.55, 120.55))


def download_file():
    rsp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
    with open('baidu.png', 'wb') as file:
        file.write(rsp.content)


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        fileName = self.url[self.url.rfind('/') + 1:]
        rsp = requests.get(self.url)
        with open(fileName, 'wb') as f:
            f.write(rsp.content)


# 爬虫，豆瓣top250
def get_douban_favoutite():
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
            # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
            # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
        )
        print("status code ", resp.status_code)
        # 通过正则表达式获取class属性为title且标签体不以&开头的span标签并用捕获组提取标签内容
        pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
        titles = pattern1.findall(resp.text)
        # 通过正则表达式获取class属性为rating_num的span标签并用捕获组提取标签内容
        pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
        ranks = pattern2.findall(resp.text)
        # 使用zip压缩两个列表，循环遍历所有的电影标题和评分
        for title, rank in zip(titles, ranks):
            print(title, rank)
        # 随机休眠1-5秒，避免爬取页面过于频繁
        time.sleep(random.random() * 4 + 1)


def get_douban_xml():
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            headers={'User-Agent': 'BaiduSpider'}
        )
        tree = etree.HTML(resp.text)
        # 通过XPath语法从页面中提取电影标题
        title_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
        # 通过XPath语法从页面中提取电影评分
        rank_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]')
        for title_span, rank_span in zip(title_spans, rank_spans):
            print(title_span.text, rank_span.text)


def get_server():
    client = socket()
    client.connect((localIp, 6789))

    in_data = bytes()
    data = client.recv(1024)

    while data:
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode('utf-8'))
    print(f'my_dict {my_dict}')
    file_name = my_dict['fileName']
    file_data = my_dict['data'].encode('utf-8')
    with open("copy.png", 'wb') as f:
        f.write(b64decode(file_data))
    print('图片已保存')
    client.close()


if __name__ == '__main__':
    get_server()
