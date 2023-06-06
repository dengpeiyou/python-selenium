#coding=utf-8
import os
import time,subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def OpenURL(url,port):#以调试方式打开目标网站
    st=subprocess.STARTUPINFO
    st.dwFlags=subprocess.STARTF_USESHOWWINDOW
    st.wShowWindow=subprocess.SW_HIDE
    cmd_str=r'"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe" --remote-debugging-port='+str(port)+r' '+url
    CREATE_NO_WINDOW = 0x08000000
    ret=subprocess.Popen(cmd_str,shell=True,creationflags=CREATE_NO_WINDOW)
    time.sleep(1)#等待使子进程打开
    ret.kill()#关闭cmd窗口

def GetDriver(port):#以调试参数方式启动一个session实例接管打开的网站(要求前后端口一致且未占用)
    opt=Options()
    opt.add_experimental_option("debuggerAddress", "127.0.0.1:"+str(port))
    chrome_driver = r"C:\windows\system32\chromedriver.exe"           #设置chromedriver的实际存放位置
    driver = webdriver.Chrome(chrome_driver, options=opt)
    
    #print(driver.title)                                               #能正确显示标题视为操作成功
    
    return driver
url="http://portal.xj.ha.sgcc.com.cn/xx_yy/" 
port=9222
OpenURL(url,port)

b=GetDriver(port)
time.sleep(2)
ades=b.find_elements_by_xpath("//div/div[@onclick]")
for ad in ades:
    ad.click()
    time.sleep(0.5)

b.find_element_by_xpath('//div[@class="login"]/a').click() #登陆图标

for handle in b.window_handles:
    b.switch_to.window(handle)
    if "ISC-SSO" in b.title:
        break;
    
time.sleep(1)

InputUser=b.find_element_by_css_selector("#username")
InputUser.clear()
InputUser.send_keys("dengpeiyou")

InputUser=b.find_element_by_css_selector("#password")
InputUser.clear()
InputUser.send_keys("*******")

b.find_element_by_id('submit_login').click() #登陆按钮


Content=b.find_element_by_css_selector("a[url*="http://iscsso"]")
span>
#os.system("taskkill /F /im chromedriver.exe")
time.sleep(3)
b.quit()

