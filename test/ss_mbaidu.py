import requests, urllib, json
from pyquery import PyQuery as pq
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'}


def curl(url, retries=3, num=1):
    try:
        html = requests.get(url, headers=headers, timeout=5).text
    except:
        html = None
        if retries > 0:
            print('请求失败，重试第%s次' % num)
            return curl(url, retries - 1, num + 1)
    return html


def baidu_urls(kw):
    urls = []
    ranks = []
    for i in range(0, 50, 10):
        url = 'https://m.baidu.com/s?word={}&pn={}'.format(urllib.parse.quote(kw), i)
        try:
            html = curl(url)
            doc = pq(html)
            divs = doc('.result').items()
            for div in divs:
                datalog = div.attr('data-log')
                if datalog:
                    datalog = datalog.replace('\'', '"')
                    data = json.loads(datalog)
                    url = data.get('mu', '404.html')
                    urls.append(url)
                    rank = i + int(data.get('order'))
                    ranks.append(rank)
        except:
            continue
    return zip(urls, ranks)


def mobrank(kw, domain):
    print(kw)
    datas = baidu_urls(kw)
    for url, rank in datas:
        if domain in url:
            return kw, url, rank
    return kw, '404.html', '50+'


if __name__ == '__main__':
    kws = [kw.rstrip() for kw in open('keywords.txt', encoding='utf-8-sig')]
    datas = []
    from multiprocessing.dummy import Pool as ThreadPool

    pool = ThreadPool(25)  # 开启25个线程
    results = pool.map(partial(mobrank, domain='xysydata.com'), kws)  # 这里传入带查询的域名
    pool.close()
    pool.join()

    for kw, url, rank in results:
        data = '{}\t{}\t{}'.format(kw, url, rank)
        datas.append(data + '\n')
        print(data)

    with open('results.txt', 'w', encoding='utf-8') as f:  # 将查询结果写入TXT文件
        f.writelines(datas)
