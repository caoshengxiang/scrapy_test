from seo.SEO import SEO
from multiprocessing.dummy import Pool


def SEO_GOOGLE(param):
    seo = SEO(param)
    seo.getVar()
    seo.run_sleep(60 * 10, 60 * 20)  # 启动延时 范围 默认 start=2 end=5
    seo.open_google_engine()


def google_run():
    # 变量配置
    name = 'g美食分享'
    max_page = 30  # 查询最大页数
    site_url_keyword = 'meishi12.com'
    site_urls = [  # 目标站点 子页面 随机1-3个，必须大于三
        'http://www.meishi12.com',
        'http://www.meishi12.com/meishi12/%B9%E3%B3%A1%C3%C0%CA%B3%CD%F2%BC%CE.html',
        'http://www.meishi12.com/meishi12/%B9%C5%B3%C7%C3%C0%CA%B3%C4%DA.html',
        'http://www.meishi12.com/meishi12/%C3%C0%CA%B3%C4%CF%C9%BD%C7%F8.html',
        'http://www.meishi12.com/meishi12/%C0%D6%D4%B0%C3%C0%CA%B3%BD%D6.html',
        'http://www.meishi12.com/meishi12/%C3%C0%CA%B3%C2%ED%CC%E3.html',
        'http://www.meishi12.com/meishi12/%C3%C0%CA%B3%C2%DE%BD%AD.html',
        'http://www.meishi12.com/meishi12/%C3%C0%CA%B3%C0%CF%B5%D7%D7%D3.html',
        'http://www.meishi12.com/meishi12/%C3%C0%CA%B3%CC%D8%B2%FA%E4%BB%CB%AE.html',
        'http://www.meishi12.com/meishi12/%BE%E7%BC%C7%C3%C0%CA%B3%CD%B8%C4%CF%D6%A6.html',
        'http://www.meishi12.com/meishi12/%CA%AF%C1%D6%CF%D8%CD%C6%BC%F6%C3%C0%CA%B3.html',
        'http://www.meishi12.com/meishi12/%C3%C0%CA%B3%BC%D2%BD%AD%B2%A8.html',
        'http://www.meishi12.com/meishi12/%C1%F4%D1%A7%C9%FA%C3%C0%CA%B3%CE%E4%B4%F3%B8%BD%BD%FC.html',
        'http://www.meishi12.com/meishi12/%BA%C5%BF%AA%B9%AB%D6%DA%B8%F6%C8%CB%D4%F5%C3%B4%C3%C0%CA%B3.html',
        'http://www.meishi12.com/meishi12/%C0%CF%CA%F3%D4%F5%C3%B4%D6%C6%D7%F7%BD%E1%BE%A7%C3%C0%CA%B3%B4%F3%D5%BD.html',
        'http://www.meishi12.com/meishi12/%C7%E9%C2%C2%B4%F3%C3%C0%CA%B3%D4%C3%B3%C7%C9%F2%D1%F4.html',
        'http://www.meishi12.com/meishi12/%C0%EF%B5%C4%C3%C0%CA%B3%C9%CC%B3%A1.html',
    ]
    keywords = ['美食']

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
