#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
 

exe_url=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9233'


options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9233")
driver = webdriver.Chrome(options=options)
 
# 测试打印页面标题
print(driver.title)


#执行的动作: close()方法关闭当前窗口。
#quit()方法退出驱动程序实例，关闭所有打开的相关窗口。
sleep(3)
driver.close()

#用于测试close之后的窗口的关闭情况
print(driver.window_handles)

sleep(3)
driver.quit()

