from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_BAIDU(param):
    seo = SEO(param)
    seo.getVar()
    seo.run_sleep(60 * 10, 60 * 30)  # 启动延时 范围 默认 start=2 end=5
    seo.open_baidu_engine()


def baidu_run():
    # 变量配置 site 2
    name = 'b阿斯旺(北京)环保科技有限公司'
    max_page = 30  # 查询最大页数
    site_url_keyword = 'xjdean.com'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.aswater.com.cn/',
        'http://www.aswater.com.cn/',
        'http://www.aswater.com.cn/',
        'http://www.aswater.com.cn/',
        'http://www.aswater.com.cn/',
        'http://www.aswater.com.cn/page188',
        'http://www.aswater.com.cn/page188',
        'http://www.aswater.com.cn/page188',
        'http://www.aswater.com.cn/page196?article_id=214',
        'http://www.aswater.com.cn/page198',
        'http://www.aswater.com.cn/page197',
        'http://www.aswater.com.cn/page206',
        'http://www.aswater.com.cn/page207',
        'http://www.aswater.com.cn/page199',
        'http://www.aswater.com.cn/page191',
        'http://www.aswater.com.cn/page205',
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
