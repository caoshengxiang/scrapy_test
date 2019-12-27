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

            print(title)
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
    (maxPage, site, keyword, clickNum, not_keyword_site) = PARAMS
    current_page = 1
    proxy = '127.0.0.1:24000'  # 代理ip
    print(proxy)
    ua = RandomUserAgent()
    print(ua)

    ops = Options()

    ops.add_argument('--user-agent=%s' % ua)
    # ops.add_argument('--proxy-server=http://%s' % proxy)
    # driver = webdriver.Chrome(path=r"/root/chromedriver", options=ops)
    driver = webdriver.Chrome(options=ops)

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
                    print(f'找到目标站点,页码：{current_page}，信息：{rank}')
                    time.sleep(0.5)
                    tindex = clickNum  # 制造五次点击量
                    while tindex > 0:
                        items = driver.find_elements_by_css_selector('.g')
                        items[rank[0] - 1].find_element_by_css_selector('.r > a').click()
                        tindex -= 1

                        ###################### 模拟
                        random_time = random.randint(20, 300)
                        print(f'目标停留{random_time} s')
                        time.sleep(random_time)  # 目标站点停留
                        ######################

                        driver.back()

                        time.sleep(1)
                    break
                else:
                    ###################### 模拟
                    items = driver.find_elements_by_css_selector('.f')
                    random_test_num = random.randint(0, 6)
                    items[random_test_num].find_element_by_css_selector('r a').click()

                    random_test_time = random.choice([0.2, 0.5, 0.8, 1, 1.5, 1.8, 2])
                    print(f'test站点停留{random_test_time} s')
                    time.sleep(random_test_time)  # test站点停留
                    driver.back()

                    time.sleep(0.2)
                    ###################### 模拟

                    print(f'第{current_page}页，未找到目标')
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
                    driver.get(not_keyword_site)
                    ###################### 模拟
                    random_time = random.randint(20, 300)
                    print(f'目标停留{random_time} s')
                    time.sleep(random_time)  # 目标站点停留
                    ######################
                    tindex -= 1

                    ###################### 模拟-个性化
                    random_height = random.randint(30, 200)
                    driver.execute_script(f"window.scrollTo(0,{random_height})")
                    time.sleep(0.5)
                    # target_bar = driver.find_elements_by_css_selector('.weui-tabbar a')
                    # target_bar = driver.find_elements_by_css_selector('a')
                    # target_bar_len = len(target_bar)
                    # target_index = random.randint(0, target_bar_len)
                    # target_bar[target_index].click()
                    time.sleep(0.5)
                    ###################### 模拟-个性化

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    # 变量配置
    max_page = 5  # 查询最大页数
    site = 'bbc.com'  # 目标域名,不包含 httt:\\ 和 www 的域名，如 baidu.com
    not_keyword_site = 'https://www.bbc.com/zhongwen/simp'  # 再运行目标内无关键字，直接访问目标站点
    keywords = ['中文网']  # 关键字
    run_times = 2  # 一个关键词的启动次数
    click_num = 1  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程

    start_time = time.time()

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((max_page, site, keyword, click_num, not_keyword_site))
    # print(params)
    pool.map(SEO_GOOGLE, params)  # 只能传一个参数

    end_time = time.time()

    second = end_time - start_time

    print_str = f'花费时间{second / 60} min'
    print(print_str)
