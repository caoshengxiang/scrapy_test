from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_BAIDU(param):
    seo = SEO(param)
    seo.getVar()
    seo.run_sleep(60 * 10, 60 * 20)  # 启动延时 范围 默认 start=2 end=5
    seo.open_baidu_engine()


def baidu_run():
    # 变量配置 site 2
    name = 'b稳力(天津)环保科技有限公司【官网】'
    max_page = 30  # 查询最大页数
    site_url_keyword = 'venlee.com'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.venlee.com.cn/',
        'http://www.venlee.com.cn/',
        'http://www.venlee.com.cn/',
        'http://www.venlee.com.cn/',
        'http://www.venlee.com.cn/zjwl.html',
        'http://www.venlee.com.cn/xcpfl.html',
        'http://www.venlee.com.cn/product/5/',
        'http://www.venlee.com.cn/product/8/',
        'http://www.venlee.com.cn/product/6/',
        'http://www.venlee.com.cn/intro/4.html',
        'http://www.venlee.com.cn/news/4/',
        'http://www.venlee.com.cn/news/7/',
        'http://www.venlee.com.cn/intro/14.html',
        'http://www.venlee.com.cn/intro/17.html',
        'http://www.venlee.com.cn/intro/19.html',
    ]
    keywords = ['环保科技']

    run_times = 5 * 12 * 3  # 一个关键词的启动次数
    click_num = 1  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [30, 300]  # 目标页面停留时间范围

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((name, max_page, site_url_keyword, keyword, click_num, site_urls, sleep))
    # print(params)
    pool.map(SEO_BAIDU, params)  # 只能传一个参数


if __name__ == '__main__':
    baidu_run()
