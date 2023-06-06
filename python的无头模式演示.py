#本示例演示如果用CHrome无头模式打开并抓取百度首页标题
#coding:utf-8
from selenium import webdriver
opt=webdriver.ChromeOptions()
opt.add_argument('disable-infobars')
opt.add_argument('--start-maximized')
opt.add_argument('--headless')
opt.add_argument('--disable-gpu') # 谷歌文档加它避免bug

b=webdriver.Chrome(options=opt)

b.get("http://www.baidu.com")
print(b.title)
b.quit()
