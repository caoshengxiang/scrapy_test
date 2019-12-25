# 360搜索排名查询
# -*- coding=utf-8 -*-
import requests
from lxml import etree
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def ss360(keyword, num, search_url):
    search_datas = ''
    for x in range(1, num + 1):
        print(f"正在查询第{x}页搜索结果...")
        url = f"https://www.so.com/s?q={keyword}&pn={x}"
        html = requests.get(url, headers=headers).text
        doc = pq(html)
        alinks = doc('.res-list h3.res-title a')

        for index, link in enumerate(alinks.items(), start=1):
            try:
                url = link.attr('data-url')
                title = link.text()
                print(title)
                if search_url in url:
                    pm = (x - 1) * 10 + index
                    # print(f'第{x}页,排名：{pm},链接：{url}')
                    search_data = f'第{x}页,排名：{pm},链接：{url}'
                    search_datas = '%s%s%s' % (search_datas, search_data, '\n')
            except:
                pass
    print(search_datas)
    return search_datas


if __name__ == "__main__":
    search_datas = ''
    # keyword = input('请输入关键词>>')
    # num = int(input('请输入最大查询页数>>'))
    # search_website = input('请输入网址(建议输入不带www网址)>>')
    keyword = '星宇'
    num = 10
    search_website = 'www.xingyukj.com'
    search_datas = ss360(keyword, num, search_website)
    print('========================查询结果========================\n\n')
    print(f"输入的关键词{keyword}在 https://www.so.com  的排名：\n")
    print(search_datas)
    if not search_datas:
        print('排名在100+')
    print('\n\n========================查询结束========================\n')
