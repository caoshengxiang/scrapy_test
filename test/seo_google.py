import json
import time
import random
from functools import partial

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from multiprocessing.dummy import Pool
from selenium.webdriver.chrome.options import Options


def KeywordRank(searchTxt, site):
    try:
        doc = pq(searchTxt)
        divs = doc('.g')
        for index, div in enumerate(divs.items(), start=1):

            alink = div.find('div.r > a')
            title = div.find('div.r > a > h3')
            if not alink:
                print('特殊数据！！！')
                continue

            print(title.text())
            item_str = alink.attr('href')

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


def window_handles_to_last(driver):
    try:
        # 获取当前所有窗口句柄（窗口A、B）
        handles = driver.window_handles
        handles_len = len(handles)
        if handles_len > 1:
            driver.switch_to.window(handles[handles_len - 1])
        else:
            pass
    except Exception as e:
        pass


# driver, 初始handle
def window_handles_to_new(driver, handle):
    try:
        # 获取当前所有窗口句柄（窗口A、B）
        handles = driver.window_handles
        # 对窗口进行遍历
        for newhandle in handles:
            # 筛选新打开的窗口B
            if newhandle != handle:
                # 切换到新打开的窗口B
                driver.switch_to.window(newhandle)
        return driver
    except Exception as e:
        return driver


def SEO_GOOGLE(PARAMS):
    (maxPage, site, keyword, clickNum, not_keyword_site, sleep, about_sites) = PARAMS
    current_page = 1
    proxy = '127.0.0.1:24000'  # 代理ip
    print(proxy)
    ua = RandomUserAgent()
    print(ua)

    # sleep_run = random.randint(60 * 2, 60 * 10)
    sleep_run = random.randint(1, 3)
    print(f'延迟{sleep_run} s 启动')
    time.sleep(sleep_run)

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

    # driver.get('http://httpbin.org/ip')
    # time.sleep(1)

    driver.get('https://www.google.com/')
    time.sleep(1)
    try:
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'gLFyf')))
        except Exception as e:
            pass

        try:
            input_ele = driver.find_element_by_class_name('gLFyf')
            input_ele.send_keys(keyword)
            time.sleep(1)
            submit_ele = driver.find_element_by_class_name('gNO89b')
            submit_ele.click()
            time.sleep(1)

        except Exception as e:
            pass

        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'navcnt')))
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
                        items = driver.find_elements_by_css_selector('.g')
                        items[rank[0] - 1].find_element_by_css_selector('.r > a').click()
                        tindex -= 1

                        ###################### 模拟
                        random_time = random.randint(sleep[0], sleep[1])
                        print(f'目标停留{random_time} s')
                        time.sleep(random_time)  # 目标站点停留
                        ######################

                        ###################### 模拟-个性化
                        ram2 = random.randint(1, 3)
                        rad_s = random.sample(about_sites, 3)

                        driver.get(rad_s[1])
                        time.sleep(random.randint(sleep[0], sleep[1]))
                        driver.back()
                        time.sleep(random.choice([0.5, 0.6, 0.8, 0.9]))
                        if ram2 > 1:
                            driver.get(rad_s[1])
                            time.sleep(random.randint(sleep[0], sleep[1]))
                            driver.back()
                            time.sleep(random.choice([0.5, 0.6, 0.8, 0.9]))
                        if ram2 > 2:
                            driver.get(rad_s[2])
                            time.sleep(random.randint(sleep[0], sleep[1]))
                            driver.back()
                            time.sleep(random.choice([0.5, 0.6, 0.8, 0.9]))
                        print(f'随机访问{ram2}个页面')
                        ###################### 模拟-个性化

                        driver.back()

                        time.sleep(random.choice([0.5, 0.6, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2]))

                        ###################### 模拟
                        ram4 = random.randint(1, 3)
                        if ram4 > 0:
                            items = driver.find_elements_by_css_selector('.g')
                            random_test_num = random.randint(0, 6)
                            items[random_test_num].find_element_by_css_selector('.r > a').click()
                            random_test_time = random.choice([1, 1.5, 1.8, 2, 2.1, 2.5, 2.7, 3])
                            print(f'test 2站点停留{random_test_time} s')
                            time.sleep(random_test_time)  # test站点停留
                            driver.back()
                            time.sleep(
                                random.choice([0.5, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2, 2.2, 2.4, 2.6, 2.7, 2.8, 3]))
                        ###################### 模拟
                    break
                else:

                    print(f'第{current_page}页，未找到目标')
                    ###################### 模拟
                    ram3 = random.randint(1, 3)
                    if ram3 >= 1:
                        print('点击test站点')
                        try:
                            items = driver.find_elements_by_css_selector('.g')
                            random_test_num = random.randint(0, 6)
                            items[random_test_num].find_element_by_css_selector('.r > a').click()
                            time.sleep(3)
                        except Exception as e:
                            print(e)

                        random_test_time = random.choice([0.2, 0.5, 0.8, 1, 1.5, 1.8, 2])
                        print(f'test站点停留{random_test_time} s')
                        time.sleep(random_test_time)  # test站点停留
                        driver.back()

                        time.sleep(random.choice([0.2, 0.5, 0.8, 1, 1.5, 1.8]))
                    ###################### 模拟
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(0.5)

                    """
                        用来判断元素标签是否存在，
                    """
                    try:
                        driver.find_element_by_id('pnnext')
                    # 原文是except NoSuchElementException, e:
                    except NoSuchElementException as e:
                        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                        print('无 下一页')
                        break
                    else:
                        # 没有发生异常，表示在页面中找到了该元素，返回True
                        next_page_ele = driver.find_element_by_id('pnnext')
                        next_page_ele.click()
                        time.sleep(2)
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
                        driver.back()
                    ###################### 模拟-个性化
                    driver.get('https://www.google.com/')
                    time.sleep(
                        random.choice([0.5, 0.6, 0.8, 0.9, 1, 1.2, 1.4, 1.5, 1.8, 2, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8]))

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    # 变量配置
    max_page = 20  # 查询最大页数
    site = 'lanshn.com'
    not_keyword_site = [
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
    # 西安蓝深环保科技有限公司-【官网】
    # 找到目标站点,页码：10，信息：[2, 'http://www.lanshn.com/index.html']
    # 找到目标站点,页码：10，信息：[7, 'http://www.lanshn.com/index.html']
    # 找到目标站点,页码：10，信息：[8, 'http://www.lanshn.com/index.html'],当前时间：2020-01-03 10:24:41
    # 找到目标站点,页码：9，信息：[1, 'http://www.lanshn.com/index.html'],当前时间：2020-01-03 14:57:05

    run_times = 5 * 12  # 一个关键词的启动次数
    click_num = 3  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [4, 100]  # 目标页面停留时间范围
    about_sites = [  # 目标站点 子页面 随机1-3个， about_sites必须大于三
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

    start_time = time.time()

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((max_page, site, keyword, click_num, not_keyword_site, sleep, about_sites))
    # print(params)
    pool.map(SEO_GOOGLE, params)  # 只能传一个参数

    end_time = time.time()

    second = end_time - start_time

    print_str = f'花费时间{second / 60} min'
    print(print_str)
