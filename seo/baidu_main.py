from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_BAIDU(param):
    seo = SEO(param)
    seo.getVar()

    seo.open_baidu_engine(sleep_stop=[60 * 30, 60 * 40])


def baidu_run():
    # 变量配置 site 2
    name = 'b安徽中发环保科技有限公司'
    max_page = 30  # 查询最大页数
    site_url_keyword = 'ahzhongfa.com'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.ahzhongfa.com/page9',
        'http://www.ahzhongfa.com/page3',
        'http://www.ahzhongfa.com/page36',
        'http://www.ahzhongfa.com/page26',
        'http://www.ahzhongfa.com/page7',
        'http://www.ahzhongfa.com/',
    ]
    keywords = ['环保科技']

    run_times = 5 * 12 * 3  # 一个关键词的启动次数
    click_num = 1  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [30, 200]  # 目标页面停留时间范围

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((name, max_page, site_url_keyword, keyword, click_num, site_urls, sleep))
    # print(params)
    pool.map(SEO_BAIDU, params)  # 只能传一个参数


if __name__ == '__main__':
    baidu_run()
