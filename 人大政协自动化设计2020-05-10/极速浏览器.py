#coding:utf-8
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time  
  
__browser_url = r'C:\Program Files (x86)\TSBrowser\TSBrowser.exe'  ##360浏览器的地址  
opt = Options()  
opt.binary_location = __browser_url  
  
driver = webdriver.Chrome(chrome_options=opt,executable_path="D:\\chromedriver.exe")  

driver.get('http://47.92.122.118:8000/#/login')  
driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN)  
time.sleep(3)  
driver.quit()  