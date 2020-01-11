import random
import time

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from faker import Faker
from multiprocessing.dummy import Pool

faker = Faker('zh_CN')


class SEO(object):
    def __init__(self, PARAMS):
        (self.name, self.maxPage, self.site_url_keyword, self.keyword, self.clickNum, self.site_urls,
         self.sleep) = PARAMS

        self.__current_page = 1
        self.__proxy = '127.0.0.1:24000'  # 代理ip
        self.__ua = self.RandomUserAgent()
        self.driver = None
        self.handle = None

    @staticmethod
    def Baidu_KeywordRank(searchTxt, site_url_keyword):
        try:
            doc = pq(searchTxt)
            divs = doc('.c-container')
            for index, div in enumerate(divs.items(), start=1):
                alink = div.children('h3').children('a')
                if not alink:
                    print('特殊数据！！！')
                    continue
                # print(alink.text())
                # href = alink.attr('href')
                # requests.packages.urllib3.disable_warnings()
                # href_data = requests.get(href.rstrip(), verify=False)
                # item_str = href_data.url

                item_str = div.find('.c-showurl').text()  # 这个方式 普通站点还是能找到 url （百度快照）

                if site_url_keyword in item_str:
                    return [index, item_str]
        except Exception as e:
            print(e)
            return None
        return None

    @staticmethod
    def Google_KeywordRank(searchTxt, site_url_keyword):
        try:
            doc = pq(searchTxt)
            divs = doc('.c-container')
            for index, div in enumerate(divs.items(), start=1):
                alink = div.children('h3').children('a')
                if not alink:
                    print('特殊数据！！！')
                    continue
                # print(alink.text())
                # href = alink.attr('href')
                # requests.packages.urllib3.disable_warnings()
                # href_data = requests.get(href.rstrip(), verify=False)
                # item_str = href_data.url

                item_str = div.find('.c-showurl').text()  # 这个方式 普通站点还是能找到 url （百度快照）

                if site_url_keyword in item_str:
                    return [index, item_str]
        except Exception as e:
            print(e)
            return None
        return None

    @staticmethod
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

    # 随机停留
    @staticmethod
    def random_sleep():
        sleep_t = random.randint(30, 60 * 2) / 10
        print(f'随机停留 {sleep_t} s')
        time.sleep(sleep_t)

    # 随机停留
    @staticmethod
    def test_random_sleep():
        sleep_t = random.randint(10, 20)
        print(f'test站点随机停留 {sleep_t} s')
        time.sleep(sleep_t)

    def getVar(self):
        print(self.__ua)
        # print(self.__proxy)

    # 启动延时
    @staticmethod
    def run_sleep(start=2, end=5):
        run_sleep_time = random.randint(start, end)
        print(f'延时{run_sleep_time} s')
        time.sleep(run_sleep_time)

    def print_log(self, msg):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        with open(self.name + "-log.txt", encoding='utf-8', mode="a") as f:
            f.write(self.name + '----' + msg + '    时间：' + now_time + '\n')  # 这句话自带文件关闭功能，不需要再写f.close()

    def init_selenium(self):

        option = Options()

        option.add_argument('--user-agent=%s' % self.__ua)
        # option.add_argument('--proxy-server=http://%s' % self.__proxy)
        # option.add_argument('--headless')
        # option.add_argument('--disable-gpu')

        # 禁止加载图片, css
        prefs = {
            'profile.default_content_setting_values.images': 2,
            'permissions.default.stylesheet': 2
        }
        # option.add_experimental_option('prefs', prefs)

        # window.navigator.webdriver的值为 true的问题，在右上角会弹出一个提示，不用管它，不要点击停用按钮。
        option.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome("\opt\chromedriver.exe", options=option)
        # self.driver = webdriver.Chrome(options=option)

        # self.driver.set_page_load_timeout(2)
        # self.driver.set_script_timeout(2)  # 这两种设置都进行才有效

    # 百度 当前页 随机点击 test 站点
    def baidu_click_test_site(self):
        ram3 = random.randint(0, 3)
        print(f'测试站点数：{ram3}')
        while ram3 > 0:
            print('点击test站点')
            ram3 -= 1
            items = self.driver.find_elements_by_css_selector('.c-container')
            random_test_num = random.randint(0, 6)
            items[random_test_num].find_element_by_css_selector('h3 a').click()

            self.baidu_open_new_tab_page()

            self.test_random_sleep()  # 测试站点随机停留

            self.driver.close()
            self.driver.switch_to.window(self.handle)
            time.sleep(1)

    # GOOGLE 当前页 随机点击 test 站点
    def google_click_test_site(self):
        ram3 = random.randint(1, 3)
        print(f'测试站点数：{ram3}')
        if ram3 >= 1:
            print('点击test站点')
            items = self.driver.find_elements_by_css_selector('.g')
            random_test_num = random.randint(0, 6)
            items[random_test_num].find_element_by_css_selector('.r > a').click()

            self.test_random_sleep()  # 测试站点随机停留

            self.driver.back()

            time.sleep(1)

    # 百度 跳新开标签页
    def baidu_open_new_tab_page(self):
        try:
            # 获取当前所有窗口句柄（窗口A、B）
            handles = self.driver.window_handles
            # 对窗口进行遍历
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != self.handle:
                    # 切换到新打开的窗口B
                    self.driver.switch_to.window(newhandle)
        except Exception as e:
            pass

    # 目标停留 停留
    def target_site_sleep(self):
        random_time = random.randint(self.sleep[0], self.sleep[1])
        print(f'目标停留{random_time} s')
        time.sleep(random_time)

    # 目标站点随机访问1-3个页面
    def random_open_1_3_page(self):
        ram2 = random.randint(1, 3)
        rad_s = random.sample(self.site_urls, 3)

        print(f'随机访问{ram2}个页面')
        self.driver.get(rad_s[1])
        self.target_site_sleep()  # 目标 随机停留
        if ram2 > 1:
            self.driver.get(rad_s[1])
            self.target_site_sleep()  # 目标 随机停留
        if ram2 > 2:
            self.driver.get(rad_s[2])
            self.target_site_sleep()  # 目标 随机停留

    # 百度
    def open_baidu_engine(self, url='https://www.baidu.com/', sleep_stop=[2, 5]):
        not_included = False
        if self.driver is None:
            self.init_selenium()
        self.driver.get(url)
        time.sleep(2)

        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'kw')))
        except Exception as e:
            pass

        try:
            # 获取当前窗口句柄（窗口A）
            self.handle = self.driver.current_window_handle
        except Exception as e:
            pass

        try:
            input_ele = self.driver.find_element_by_id('kw')
            input_ele.send_keys(self.keyword)
            time.sleep(1)
            submit_ele = self.driver.find_element_by_id('su')
            submit_ele.click()
            time.sleep(1)

        except Exception as e:
            pass

        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'page')))
        except Exception as e:
            pass

        while self.__current_page <= self.maxPage:
            try:
                source = self.driver.page_source
                doc = pq(source)
                rank = self.Baidu_KeywordRank(doc, self.site_url_keyword)
                if rank != None:
                    print(f'找到目标站点,页码：{self.__current_page}，信息：{rank}')
                    self.print_log(f'{self.keyword}({self.site_url_keyword}):目标,页码：{self.__current_page}，信息：{rank}')
                    time.sleep(0.5)
                    tindex = self.clickNum  # 制造点击量
                    while tindex > 0:
                        items = self.driver.find_elements_by_css_selector('.c-container')
                        items[rank[0] - 1].find_element_by_css_selector('h3 a').click()
                        tindex -= 1

                        self.baidu_open_new_tab_page()

                        # driver = window_handles_to_new(driver)

                        self.target_site_sleep()  # 目标 随机停留

                        print('目标模拟-第二步-跳出率')

                        self.random_open_1_3_page()  # 目标站点随机访问1-3个页面

                        self.driver.close()
                        self.driver.switch_to.window(self.handle)
                        self.random_sleep()  # 随机停留

                        self.baidu_click_test_site()  # 当前页 随机点击一个test 站点
                    break
                else:
                    print(f'第{self.__current_page}页，未找到目标')

                    self.baidu_click_test_site()  # 当前页 随机点击一个test 站点

                    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                    time.sleep(1)

                    page_ele = self.driver.find_element_by_id('page')
                    next_page_ele = page_ele.find_element_by_link_text('下一页>')
                    next_page_ele.click()
                    time.sleep(1)
                    self.__current_page += 1
            except Exception as e:
                pass
        if self.__current_page > self.maxPage:
            print(f'目标超出{self.maxPage}页')
            self.print_log(f'{self.site_url_keyword}-{self.keyword}: 目标超出{self.maxPage}页')
            # 直接请求目标域名
            if self.site_urls:
                self.random_open_1_3_page()  # 目标站点随机访问1-3个页面

                self.driver.get(url)
                self.random_sleep()  # 随机停留

                self.driver.quit()
                self.run_sleep(sleep_stop[0], sleep_stop[1])

        self.driver.quit()
        self.run_sleep(sleep_stop[0], sleep_stop[1])

    # GOOGLE
    def open_google_engine(self, url='https://www.google.com/', sleep_stop=[2, 5]):
        global not_included
        if self.driver is None:
            self.init_selenium()
        self.driver.get(url)
        time.sleep(2)

        try:
            try:
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'gLFyf')))
            except Exception as e:
                pass

            try:
                input_ele = self.driver.find_element_by_class_name('gLFyf')
                input_ele.send_keys(self.keyword)
                time.sleep(1)
                submit_ele = self.driver.find_element_by_class_name('gNO89b')
                submit_ele.click()
                time.sleep(1)

            except Exception as e:
                self.driver.quit()

            try:
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, 'navcnt')))
            except Exception as e:
                self.driver.quit()

            while self.__current_page <= self.maxPage:
                try:
                    source = self.driver.page_source
                    doc = pq(source)
                    rank = self.Google_KeywordRank(doc, self.site_url_keyword)
                    if rank != None:
                        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        print(f'找到目标站点,页码：{self.__current_page}，信息：{rank},当前时间：{now_time}')
                        self.print_log(
                            f'{self.keyword}({self.site_url_keyword}): 目标,页码：{self.__current_page}，信息：{rank}')
                        time.sleep(0.5)
                        tindex = self.clickNum  # 制造点击量
                        while tindex > 0:
                            items = self.driver.find_elements_by_css_selector('.g')
                            items[rank[0] - 1].find_element_by_css_selector('.r > a').click()
                            tindex -= 1

                            self.target_site_sleep()  # 目标 随机停留

                            self.random_open_1_3_page()  # 目标站点随机访问1-3个页面

                            self.driver.back()

                            self.random_sleep()  # 随机停留

                            self.google_click_test_site()  # 当前页 随机点击一个test 站点
                        break
                    else:

                        print(f'第{self.__current_page}页，未找到目标')

                        self.google_click_test_site()  # 当前页 随机点击一个test 站点

                        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                        time.sleep(1)

                        """
                            用来判断元素标签是否存在，
                        """
                        try:
                            self.driver.find_element_by_id('pnnext')
                        # 原文是except NoSuchElementException, e:
                        except NoSuchElementException as e:
                            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                            print('无 下一页')
                            self.print_log(f'{self.site_url_keyword}-{self.keyword}: 目标关键字未被收录')
                            not_included = True
                            break
                        else:
                            # 没有发生异常，表示在页面中找到了该元素，返回True
                            next_page_ele = self.driver.find_element_by_id('pnnext')
                            next_page_ele.click()
                            time.sleep(2)
                            self.__current_page += 1


                except Exception as e:
                    pass
            if not_included:
                pass
            elif self.__current_page > self.maxPage:
                print(f'目标超出{self.maxPage}页')

                # 直接请求目标域名
                if self.__current_page > self.maxPage:
                    print(f'目标超出{self.maxPage}页')
                    self.print_log(f'{self.site_url_keyword}-{self.keyword}: 目标超出{self.maxPage}页')

                    # 直接请求目标域名
                    if self.site_urls:
                        self.random_open_1_3_page()  # 目标站点随机访问1-3个页面

                        self.driver.get(url)
                        self.random_sleep()  # 随机停留
            self.driver.quit()
            self.run_sleep(sleep_stop[0], sleep_stop[1])
        except Exception as e:
            print(e)
            self.driver.quit()
            self.run_sleep(sleep_stop[0], sleep_stop[1])


# 下面是调用实例 百度和google

def SEO_BAIDU(param):
    seo = SEO(param)
    seo.getVar()
    seo.run_sleep(2, 60 * 10)  # 启动延时 范围 默认 start=2 end=5
    seo.open_baidu_engine()


def SEO_GOOGLE(param):
    seo = SEO(param)
    seo.getVar()
    seo.open_google_engine()


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

    run_times = 5 * 12  # 一个关键词的启动次数
    click_num = 3  # 单次启动 目标 点击次数
    pool = Pool(1)  # 进程
    sleep = [2, 10]  # 目标页面停留时间范围

    params = []
    for i in range(run_times):
        for keyword in keywords:
            params.append((max_page, site_url_keyword, keyword, click_num, site_urls, sleep))
    # print(params)
    pool.map(SEO_BAIDU, params)  # 只能传一个参数


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
    baidu_run()
    # google_run()
