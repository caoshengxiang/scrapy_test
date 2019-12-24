# 360搜索排名查询
# -*- coding=utf-8 -*-
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def ss360(keyword, num, search_url):
    search_datas = ''
    for x in range(1, num + 1):
        print(f"正在查询第{x}页搜索结果...")
        url = f"https://www.so.com/s?q={keyword}&pn={x}"
        html = requests.get(url, headers=headers).text
        # print(html)
        con = etree.HTML(html)
        # print(con)
        title = con.xpath('//h3[@class="res-title "]/a/text()')
        # print(title)
        # print(len(title))

        datas = con.xpath('///h3/a')
        # print(len(datas))
        for data in datas:
            # print(data)
            try:
                data_res = data.attrib['data-res']
                # pos=re.findall('"pos":(.+?),',data_res,re.S)
                # print(pos[0])
                data_res = eval(data_res)  # 转换为字典数据
                pos = data_res['pos']
                print(pos)
            except:
                pos = ''
            try:
                data_url = data.attrib['data-url']
            except:
                data_url = data.attrib['href']
            if "http://e.360.cn/static/" not in data_url and "javascript:" not in data_url:
                print(data_url)
                print('\r')
            if search_url in data_url:
                pm = (x - 1) * 10 + pos
                print(f'第{x}页,排名：{pos}/{pm},链接：{data_url}')
                search_data = f'第{x}页,排名：{pos}/{pm},链接：{data_url}'
                search_datas = '%s%s%s' % (search_datas, search_data, '\n')
    print(search_datas)
    return search_datas


if __name__ == "__main__":
    search_datas = ''
    keyword = input('请输入关键词>>')
    num = int(input('请输入最大查询页数>>'))
    search_website = input('请输入网址(建议输入不带www网址)>>')
    search_datas = ss360(keyword, num, search_website)
    print('========================查询结果========================\n\n')
    print(search_datas)
    print('\n\n========================查询结束========================\n')
