from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_GOOGLE(param):
    seo = SEO(param)
    seo.getVar()
    seo.run_sleep(2, 60 * 10)  # 启动延时 范围 默认 start=2 end=5
    seo.open_google_engine()


def google_run():
    # 变量配置
    max_page = 20  # 查询最大页数
    site_url_keyword = 'lanshn.com'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.lanshn.com/index.html',
        'http://www.lanshn.com/index.html',
        'http://www.lanshn.com/index.html',
        'http://www.lanshn.com/aboyt/gsjj/',
        'http://www.lanshn.com/aboyt/gsjj/',
        'http://www.lanshn.com/aboyt/zzry/',
        'http://www.lanshn.com/xwzx/qyxw/',
        'http://www.lanshn.com/xwzx/qyxw/',
        'http://www.lanshn.com/jjfa2/',
        'http://www.lanshn.com/hxjs/',
        'http://www.lanshn.com/xwzx/qyxw/124.html',
    ]
    keywords = ['环保科技']

    run_times = 5 * 12  # 一个关键词的启动次数
    click_num = 3  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [2, 10]  # 目标页面停留时间范围

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((max_page, site_url_keyword, keyword, click_num, site_urls, sleep))
    # print(params)
    pool.map(SEO_GOOGLE, params)  # 只能传一个参数


if __name__ == '__main__':
    google_run()

    # 西安蓝深环保科技有限公司-【官网】
    # 找到目标站点,页码：10，信息：[2, 'http://www.lanshn.com/index.html']
    # 找到目标站点,页码：10，信息：[7, 'http://www.lanshn.com/index.html']
    # 找到目标站点,页码：10，信息：[8, 'http://www.lanshn.com/index.html'],当前时间：2020-01-03 10:24:41
    # 找到目标站点,页码：9，信息：[1, 'http://www.lanshn.com/index.html'],当前时间：2020-01-03 14:57:05