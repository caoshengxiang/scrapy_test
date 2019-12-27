from functools import partial

from selenium import webdriver
from multiprocessing.dummy import Pool


def spider(url, msg):
    print(msg)
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    html = driver.page_source
    print(html)
    driver.close()
    driver.quit()


def run(x):
    url = 'https://www.baidu.com/s?wd=今天有哪些美女&pn={}'
    pages = []
    for i in range(0, x * 10, 10):
        page = url.format(i)
        pages.append(page)
    print(pages)
    pool = Pool(5)
    result = pool.map(partial(spider, msg='test'), pages)
    pool.close()
    pool.join()
    return result


if __name__ == '__main__':
    run(10)
