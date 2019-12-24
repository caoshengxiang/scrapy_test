# -*- coding: utf-8 -*-
import logging
import time

import scrapy
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from scrapy_test.items import ScrapyTestItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def __init__(self):
        pass
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # No_Image_loading = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", No_Image_loading)
        # epath = "/usr/bin/chromedriver"
        # # chrome_options.binary_location = r"D:\soft\googlechrome\Application\77.0.3865.120\chrome.exe"
        # # epath = "D:/work/chromedriver.exe"
        # self.driver = webdriver.Chrome(executable_path=epath, chrome_options=chrome_options)

        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # No_Image_loading = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", No_Image_loading)
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # self.driver = webdriver.Chrome()

    def parse(self, response):
        # self.driver.get('https://www.baidu.com')
        # time.sleep(5)
        #
        # action = ActionChains(self.driver)
        # s_kw_wrap = self.driver.find_element_by_id('kw')
        # action.move_to_element(s_kw_wrap).perform()
        # time.sleep(0.5)
        # action.click(s_kw_wrap).perform()
        # time.sleep(0.5)
        # action.send_keys_to_element(s_kw_wrap, 'python').perform()
        # time.sleep(1)
        # btn = self.driver.find_element_by_id('su')
        # action.click(btn).perform()
        #
        # time.sleep(10)

        time.sleep(10)
        item = ScrapyTestItem()
        item['name'] = response.text
        yield item
