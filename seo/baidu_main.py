from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_BAIDU(param):
    seo = SEO(param)
    seo.getVar()
    seo.run_sleep(2, 60 * 10)  # 启动延时 范围 默认 start=2 end=5
    seo.open_baidu_engine()


def baidu_run():
    # 变量配置 site 2
    max_page = 30  # 查询最大页数
    site_url_keyword = 'www.scjxhbkj.com'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.scjxhbkj.com/',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=8',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=25',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=50',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=52',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=32',
    ]
    keywords = ['环保科技']

    run_times = 5 * 12 * 3  # 一个关键词的启动次数
    click_num = 3  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [10, 30]  # 目标页面停留时间范围

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((max_page, site_url_keyword, keyword, click_num, site_urls, sleep))
    # print(params)
    pool.map(SEO_BAIDU, params)  # 只能传一个参数


if __name__ == '__main__':
    baidu_run()


    # 四川俊西环保科技有限公司
    # 找到目标站点,页码：21，信息：[9, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：22，信息：[5, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：22，信息：[3, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：21，信息：[9, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：22，信息：[1, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：23，信息：[1, 'www.scjxhbkj.com/'],当前时间：2020-01-03 11:35:09
    # 找到目标站点,页码：22，信息：[1, 'www.scjxhbkj.com/'],当前时间：2020-01-03 13:54:42