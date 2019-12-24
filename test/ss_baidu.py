# 关键字，公司网址，查询网址
import re
import time

import requests
from pyquery import PyQuery as pq

s = requests.session()
s.keep_alive = False

# site_baidu = u"http://www.baidu.com/s?wd=%s&pn=%d0"
# site_360 = "https://hao.360.cn/"

# 查询排名
i = 0
# word = u"体检行业爆丑闻"
# site = "https://baijiahao.baidu.com"
site_baidu = u"http://www.baidu.com/s?wd=%s&pn=%d0"


def KeywordRank(searchTxt, site):
    global i
    try:
        doc = pq(searchTxt)
        divs = doc('.result')
        for div in divs.items():
            alink = div.find('a')
            href = alink.attr('href')
            requests.packages.urllib3.disable_warnings()
            href_data = requests.get(href.rstrip(), verify=False)
            item_str = href_data.url
            i = i + 1
            if site in item_str:
                return i
    except Exception as e:
        print(e)

        return None
    return None


# content:要搜索的关键词, page:要搜索的页码
def BaiduSearch(content, page):
    try:
        header = {
            'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.62 Safari/537.36',
            'Cookie': 'BAIDUID=A6771F0A0975E69CA947DC04DE0150AA:FG=1; BIDUPSID=A6771F0A0975E69CA947DC04DE0150AA; PSTM=1563167941; BD_UPN=12314753; BDUSS=ZlVXM5RGZ0a2M4UlFXfjY0Yi1sdE85cXdNOU1adUJWZXNUMlpmNHdTNmpIUU5lRVFBQUFBJCQAAAAAAAAAAAEAAABJifc5xOO9zM7SuMSx5MrAvecAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKOQ212jkNtdbH; MSA_WH=375_667; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; B64_BOT=1; H_WISE_SIDS=136721_140021_138807_138876_114745_139148_120206_138878_137985_131247_132551_118891_118873_118845_118824_118792_138165_107318_138882_139450_139284_139296_136862_138147_139624_139592_136196_139304_137104_139273_139398_139691_139431_133847_137734_137468_134046_139124_131423_139397_138904_139246_139098_136413_110085_127969_139160_138837_139883_139511_128201_138312_139732_138944_139927_139221_138754; FC_MODEL=-1_0_0_0_0_0_0_0_0_0_0_-1_1_0_1_0_0_1575885890083_1575885884178%7C1%230_-1_-1_1_1_1575885890083_1575885884178%7C1; lsv=globalTcss_b6d710f-wwwTcss_1a9246b-searchboxcss_591d86b-globalBcss_aad48cc-wwwBcss_777000e; SE_LAUNCH=5%3A26284839; MSA_PBT=146; MSA_ZOOM=1056; wpr=7; BD_HOME=1; H_PS_PSSID=1445_21079_30211_30423_30283_22157; delPer=0; BD_CK_SAM=1; PSINO=6; COOKIE_SESSION=4513_0_4_4_10_1_0_0_4_1_0_0_67925_0_4_0_1577156462_0_1577156458%7C9%23102838_15_1576663116%7C9; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=05d72nTalrDJIuF1aVjWRwiqln%2FEU5XkIejNDiZ8xjCtbX%2Bm0SWhnR2RxkY'
        }
        url = site_baidu % (content, page)
        data = requests.get(url, headers=header)
        return data.text
    except Exception as e:
        return None


if __name__ == "__main__":
    # keyword = input(u"请输入你要查询的关键字:")
    # site = input("请输入您要查询的网址:")
    keyword = '星宇'
    site = 'starlux-airlines'

    # 最多查到第 10 页
    page = 0
    while (page < 10):
        searchTxt = BaiduSearch(keyword, page)
        rank = KeywordRank(searchTxt, site)
        if None != rank:
            print(u"输入的关键词排在 baidu 第 %d 名" % (rank + page * 10))
            print(rank)
            break
        page = page + 1
        time.sleep(0.2)
    if page >= 10:
        print(page)
        print('排名在100+')
