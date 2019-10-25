import requests
import os
import json

from bs4 import BeautifulSoup


class DownloadList():
    """自定义的一个获取笔趣阁上的榜单目录"""

    def __init__(self, path=None):
        self._path = path
        self._url = 'http://www.xbiquge.la/paihangbang/'
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/52.0.2743.116 Safari/537.36'
        }
        self._response = requests.get(self._url, self._headers)
        self._response.encoding = 'utf8'

    def get_novel_list(self):
        if self._response.status_code == 200:
            soup = BeautifulSoup(self._response.text, 'lxml')
            list_box = ['box b1', 'box b2', 'box b3', 'box b4']
            for box_name in list_box:
                for box in soup.find_all(class_=box_name):
                    novel_kind = box.h3.string
                    time_dic = {}
                    for ul in box.find_all('ul'):
                        time_kind = ul.li.text[:3]
                        time_dic[time_kind] = []
                        for li in ul.find_all('li')[1:-1]:
                            novel = {'title': li.text, 'link': li.a['href']}
                            time_dic[time_kind].append(novel)
                    yield time_dic

    def save_list(self, content):
        try:
            with open(self._path + '\\榜单.txt', 'a', encoding='utf8') as f:
                f.write(json.dumps(content, ensure_ascii=False) + '\n')
        except IOError as e:
            print(e)

    def read_list(self):
        try:
            with open(self._path + '\\榜单.txt', 'r', encoding='utf8') as f:
                for line in f:
                    print(type(json.loads(line)), json.loads(line))
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)

    def download_list(self):
        for item in self.get_novel_list():
            self.save_list(item)


if __name__ == '__main__':
    get_list = DownloadList(input('请输入保存地址：'))
    print('1、从网上爬取小说列表：')
    print('2、从本地读取小说列表:')
    print('3、退出')
    while True:
        choose = int(input('请输入操作：'))
        if choose == 1:
            get_list.download_list()
        elif choose == 2:
            get_list.read_list()
        elif choose == 3:
            exit(0)