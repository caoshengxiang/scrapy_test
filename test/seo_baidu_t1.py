import json
import time
import random
from functools import partial

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from multiprocessing.dummy import Pool
from selenium.webdriver.chrome.options import Options
from faker import Faker
faker=Faker('zh_CN')


def KeywordRank(searchTxt, site):
    try:
        doc = pq(searchTxt)
        divs = doc('.c-container')
        for index, div in enumerate(divs.items(), start=1):
            alink = div.children('h3').children('a')
            if not alink:
                print('特殊数据！！！')
                continue
            print(alink.text())
            # href = alink.attr('href')
            # requests.packages.urllib3.disable_warnings()
            # href_data = requests.get(href.rstrip(), verify=False)
            # item_str = href_data.url

            item_str = div.find('.c-showurl').text()  # 这个方式 普通站点还是能找到 url （百度快照）

            if site in item_str:
                return [index, item_str]
    except Exception as e:
        print(e)

        return None
    return None


def RandomUserAgent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    # 从列表中随机抽选出一个ua值
    return random.choice(user_agent_list)


def SEO_BAIDU(PARAMS):
    (maxPage, site, keyword, clickNum, not_keyword_site, sleep, about_sites) = PARAMS
    current_page = 1
    proxy = '127.0.0.1:24000'  # 代理ip
    print(proxy)
    ua = RandomUserAgent()
    # ua = faker.chrome()
    print(ua)

    sleep_run = random.randint(60 * 2, 60 * 10)
    # sleep_run = random.randint(1, 3)
    print(f'延迟{sleep_run} s 启动')

    option = Options()

    option.add_argument('--user-agent=%s' % ua)
    # option.add_argument('--proxy-server=http://%s' % proxy)
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')

    # 禁止加载图片
    prefs = {
        'profile.default_content_setting_values.images': 2
    }
    option.add_experimental_option('prefs', prefs)

    # window.navigator.webdriver的值为 true的问题，在右上角会弹出一个提示，不用管它，不要点击停用按钮。
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    # driver = webdriver.Chrome(path=r"/root/chromedriver", options=ops)
    driver = webdriver.Chrome(options=option)

    # times_getip = 30
    # while times_getip > 0:
    #     driver.get('http://httpbin.org/ip')
    #     time.sleep(1)
    #     times_getip -= 1
    # time.sleep(300)

    driver.get('https://www.baidu.com/')
    time.sleep(1)
    try:
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'kw')))
        except Exception as e:
            pass

        try:
            # 获取当前窗口句柄（窗口A）
            handle = driver.current_window_handle
        except Exception as e:
            pass

        try:
            input_ele = driver.find_element_by_id('kw')
            input_ele.send_keys(keyword)
            time.sleep(1)
            submit_ele = driver.find_element_by_id('su')
            submit_ele.click()
            time.sleep(1)

        except Exception as e:
            pass

        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'page')))
        except Exception as e:
            pass

        while current_page <= maxPage:
            try:
                source = driver.page_source
                doc = pq(source)
                rank = KeywordRank(doc, site)
                if rank != None:
                    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    print(f'找到目标站点,页码：{current_page}，信息：{rank},当前时间：{now_time}')
                    time.sleep(0.5)
                    tindex = clickNum  # 制造点击量
                    while tindex > 0:
                        items = driver.find_elements_by_css_selector('.c-container')
                        items[rank[0] - 1].find_element_by_css_selector('h3 a').click()
                        tindex -= 1

                        try:
                            # 获取当前所有窗口句柄（窗口A、B）
                            handles = driver.window_handles
                            # 对窗口进行遍历
                            for newhandle in handles:
                                # 筛选新打开的窗口B
                                if newhandle != handle:
                                    # 切换到新打开的窗口B
                                    driver.switch_to.window(newhandle)
                        except Exception as e:
                            pass
                        # driver = window_handles_to_new(driver)

                        ###################### 模拟
                        random_time = random.randint(sleep[0], sleep[1])
                        print(f'目标停留{random_time} s')
                        time.sleep(random_time)  # 目标站点停留
                        ###################### 模拟

                        print('目标模拟-第二步-跳出率')

                        ###################### 模拟-个性化
                        ram2 = random.randint(1, 3)
                        rad_s = random.sample(about_sites, 3)

                        driver.get(rad_s[1])
                        time.sleep(random.randint(sleep[0], sleep[1]))
                        if ram2 > 1:
                            driver.get(rad_s[1])
                            time.sleep(random.randint(sleep[0], sleep[1]))
                        if ram2 > 2:
                            driver.get(rad_s[2])
                            time.sleep(random.randint(sleep[0], sleep[1]))
                        print(f'随机访问{ram2}个页面')
                        ###################### 模拟-个性化

                        driver.close()
                        driver.switch_to.window(handle)
                        time.sleep(random.choice([0.5, 0.6, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2]))

                        ###################### 模拟
                        ram4 = random.randint(1, 3)
                        if ram4 > 0:
                            items = driver.find_elements_by_css_selector('.c-container')
                            random_test_num = random.randint(0, 6)
                            items[random_test_num].find_element_by_css_selector('h3 a').click()
                            try:
                                # 获取当前所有窗口句柄（窗口A、B）
                                handles = driver.window_handles
                                # 对窗口进行遍历
                                for newhandle in handles:
                                    # 筛选新打开的窗口B
                                    if newhandle != handle:
                                        # 切换到新打开的窗口B
                                        driver.switch_to.window(newhandle)
                            except Exception as e:
                                pass
                            random_test_time = random.choice([1, 1.5, 1.8, 2, 2.1, 2.5, 2.7, 3])
                            print(f'test 2站点停留{random_test_time} s')
                            time.sleep(random_test_time)  # test站点停留
                            driver.close()
                            driver.switch_to.window(handle)
                            time.sleep(
                                random.choice([0.5, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2, 2.2, 2.4, 2.6, 2.7, 2.8, 3]))
                        ###################### 模拟
                    break
                else:
                    ###################### 模拟
                    ram3 = random.randint(1, 3)
                    if ram3 >= 1:
                        items = driver.find_elements_by_css_selector('.c-container')
                        random_test_num = random.randint(0, 6)
                        items[random_test_num].find_element_by_css_selector('h3 a').click()
                        try:
                            # 获取当前所有窗口句柄（窗口A、B）
                            handles = driver.window_handles
                            # 对窗口进行遍历
                            for newhandle in handles:
                                # 筛选新打开的窗口B
                                if newhandle != handle:
                                    # 切换到新打开的窗口B
                                    driver.switch_to.window(newhandle)
                        except Exception as e:
                            pass
                        random_test_time = random.choice([0.5, 0.8, 1, 1.5, 1.8, 2, 2.1, 2.2, 2.4])
                        print(f'test站点停留{random_test_time} s')
                        time.sleep(random_test_time)  # test站点停留
                        driver.close()
                        driver.switch_to.window(handle)
                        time.sleep(0.2)
                    ###################### 模拟

                    print(f'第{current_page}页，未找到目标')
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(
                        random.choice([0.5, 0.6, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8]))
                    page_ele = driver.find_element_by_id('page')
                    next_page_ele = page_ele.find_element_by_link_text('下一页>')
                    next_page_ele.click()
                    time.sleep(1)
                    current_page += 1
            except Exception as e:
                pass
        if current_page > maxPage:
            print(f'目标超出{maxPage}页')

            # 直接请求目标域名
            tindex = clickNum  # 制造五次直接访问击量
            if not_keyword_site:
                while tindex > 0:
                    driver.get(random.choice(not_keyword_site))
                    ###################### 模拟
                    random_time = random.randint(sleep[0], sleep[1])
                    print(f'目标停留{random_time} s')
                    time.sleep(random_time)  # 目标站点停留
                    ######################
                    tindex -= 1

                    ###################### 模拟-个性化
                    random_height = random.randint(sleep[0], sleep[1])
                    driver.execute_script(f"window.scrollTo(0,{random_height})")
                    time.sleep(0.5)
                    for i in range(1, 3):
                        driver.get(random.choice(not_keyword_site))
                        time.sleep(random.randint(sleep[0], sleep[1]))
                    ###################### 模拟-个性化
                    driver.get('https://www.baidu.com/')
                    time.sleep(
                        random.choice([0.5, 0.6, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8]))

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    # 变量配置
    # max_page = 30  # 查询最大页数
    # site = 'xysydata.com'  # 目标域名,不包含 httt:\\ 和 www 的域名，如 baidu.com
    # not_keyword_site = ['http://www.xysydata.com/#/']  # 再运行目标内无关键字，直接访问目标站点
    # keywords = ['星宇数云 数据采集', '星宇数云', '星宇数云科技', '星宇数云数据分析', '星宇数云ERP OA', '星宇数云 网络爬虫',
    #             '星宇数云 数据清洗']  # 关键字
    # run_times = 3  # 一个关键词的启动次数
    # click_num = 20  # 单次启动 目标 点击次数
    # pool = Pool(1)  # 进程
    # sleep = [30, 300] # 目标页面停留时间范围
    # about_sites = [] # 目标站点 子页面 随机1-3个， about_sites必须大于三

    # 变量配置 site 2
    max_page = 30  # 查询最大页数
    site = 'www.scjxhbkj.com'
    not_keyword_site = [
        'http://www.scjxhbkj.com/',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=8',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=25',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=50',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=52',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=32',
    ]
    keywords = ['环保科技']
    # 四川俊西环保科技有限公司
    # 找到目标站点,页码：21，信息：[9, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：22，信息：[5, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：22，信息：[3, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：21，信息：[9, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：22，信息：[1, 'www.scjxhbkj.com/']
    # 找到目标站点,页码：23，信息：[1, 'www.scjxhbkj.com/'],当前时间：2020-01-03 11:35:09
    # 找到目标站点,页码：22，信息：[1, 'www.scjxhbkj.com/'],当前时间：2020-01-03 13:54:42

    run_times = 5*12  # 一个关键词的启动次数
    click_num = 3  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [4, 100]  # 目标页面停留时间范围
    about_sites = [  # 目标站点 子页面 随机1-3个， about_sites必须大于三
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=8',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=25',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=50',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=52',
        'http://www.scjxhbkj.com/index.php?m=content&c=index&a=lists&catid=32',
    ]

    start_time = time.time()

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((max_page, site, keyword, click_num, not_keyword_site, sleep, about_sites))
    # print(params)
    pool.map(SEO_BAIDU, params)  # 只能传一个参数

    end_time = time.time()

    second = end_time - start_time

    print_str = f'花费时间{second / 60} min'
    print(print_str)
