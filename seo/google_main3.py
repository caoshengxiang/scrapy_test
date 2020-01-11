from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_GOOGLE(param):
    seo = SEO(param)
    seo.getVar()
    seo.open_google_engine(sleep_stop=[60 * 30, 60 * 40])


def google_run():
    # 变量配置
    name = 'g众创商城'
    max_page = 30  # 查询最大页数
    site_url_keyword = 'www.e-store.cn'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.e-store.cn/',
        'http://www.e-store.cn/',
        'http://www.e-store.cn/',
        'http://www.e-store.cn/',
    ]
    keywords = ['众创']

    run_times = 5 * 12  # 一个关键词的启动次数
    click_num = 1  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [30, 300]  # 目标页面停留时间范围

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((name, max_page, site_url_keyword, keyword, click_num, site_urls, sleep))
    # print(params)
    pool.map(SEO_GOOGLE, params)  # 只能传一个参数


if __name__ == '__main__':
    google_run()

    # 西安蓝深环保科技有限公司-【官网】
