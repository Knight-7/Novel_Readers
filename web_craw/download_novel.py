import requests
import re
import os

from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin


class DownloadNovel():
    """自定义的一个从笔趣阁爬取小说的类"""

    def __init__(self, title, url, path=None):
        self._title = title
        self._url = url
        self._novel_path = path
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/52.0.2743.116 Safari/537.36'
        }
        self._response = requests.get(self._url, headers=self._headers)
        self._response.encoding = 'utf8'
        if self._response.status_code == 200:
            self._soup = BeautifulSoup(self._response.text, 'lxml')
        if self._novel_path is not None:
            self._novel_path = os.path.join(self._novel_path + self._title)

    def get_novel_chapter(self):
        pattern = re.compile("<dd>.*?'(.*?)' >(.*?)</a>.*?</dd>", re.S)
        results = re.findall(pattern, self._response.text)
        return results

    def get_novel_image(self):
        self._soup = BeautifulSoup(self._response.text, 'lxml')
        img_src = self._soup.find_all('img')[1]['src']
        img_content = requests.get(img_src, headers=self._headers)
        if img_content.status_code == 200:
            self.write_to_local(self._title, img_content.content, 2)
            return self._title + '.jpg'

    def get_novel_introduction(self):
        box_con = self._soup.find(class_='box_con')
        ps = box_con.find_all('p')
        inf = []
        for i in range(len(ps)):
            if i == 0 or i == 5:
                inf.append(ps[i].string)
        return inf

    def get_novel_text(self, url):
        response = requests.get(url, headers=self._headers)
        response.encoding = 'utf8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            html_text = soup.prettify()
            pattern = re.compile('<br/>(.*?)<br/>|"content">(.*?)<br/>', re.S)
            results = pattern.findall(html_text)
            novel = results[0][1].strip() + '\n'
            for result in results[1:-2]:
                novel += result[0].strip() + '\n'
            return novel

    def write_to_local(self, chapter_title, content, save_type=1):
        if self._novel_path is not None:
            try:
                chapter_path = os.path.join(self._novel_path, chapter_title)
                if save_type == 1:
                    with open(chapter_path + '.txt', 'a', encoding='utf8') as f:
                        f.write(content)
                elif save_type == 2:
                    with open(chapter_path + '.jpg', 'wb') as f:
                        f.write(content)
            except FileNotFoundError:
                print('目录不存在')
            except FileExistsError:
                print('目录已经存在')
        else:
            if save_type == 1:
                with open(chapter_title + '.txt', 'a', encoding='utf8') as f:
                    f.write(content)
            elif save_type == 2:
                with open(chapter_title + '.jpg', 'wb') as f:
                    f.write(content)

    def make_dir(self):
        if self._novel_path is not None:
            try:
                os.mkdir(self._novel_path)
                return 1
            except FileExistsError:
                print('目录已存在，无法创建')
                return 0
            except FileNotFoundError:
                print('没有找到目录')
                return 0
        else:
            return 1

    def download(self):
        if self.make_dir():
            self.get_novel_image()
            for item in self.get_novel_title():
                print(f'正在下载----{item["title"]}')
                novel = self.get_novel_text(item['link'])
                self.write_to_local(item['title'], novel)
                sleep(0.2)


if __name__ == '__main__':
    """douluodalu = DownloadNovel("圣墟", "http://www.xbiquge.la/13/13959/")
    print(douluodalu.get_novel_chapter()[0: 30])
    print(type(douluodalu.get_novel_chapter()))"""
    test_str = '第一章 一二三'
    print(test_str[: test_str.index(' ')])