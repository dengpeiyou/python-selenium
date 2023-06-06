#先用如下命令打开一个处于调试状态的浏览器(如果打开错误把chrome地址添加到系统变量)
#chrome.exe --remote-debugging-port=9999 --user-data-dir="d:\temp\selenum\AutomationProfile" 
import os,time,re,subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#======================================================================================================判断元素是否存在
def isElementExist(driver,element_xpath):
    flag=True
    try:
        driver.find_element_by_xpath(element_xpath)
        return flag
    except:
        flag=False
        return flag


#======================================================================================================以调试方式打开目标网站
st=subprocess.STARTUPINFO
st.dwFlags=subprocess.STARTF_USESHOWWINDOW
st.wShowWindow=subprocess.SW_HIDE
cmd_str=r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9999 --user-data-dir="d:\temp\selenum\AutomationProfile" http://111cpzj.com/ '
CREATE_NO_WINDOW = 0x08000000
ret=subprocess.Popen(cmd_str,shell=True,creationflags=CREATE_NO_WINDOW)
time.sleep(1)#等待使子进程打开
ret.kill()#关闭cmd窗口

#要求前后端口一致且未占用
#======================================================================================================以调试参数方式启动一个session实例接管打开的网站
opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
chrome_driver = r"C:\windows\system32\chromedriver.exe"           #设置chromedriver的实际存放位置
driver = webdriver.Chrome(chrome_driver, options=opt)
driver.implicitly_wait(30)
print(driver.title)                                               #能正确显示标题视为操作成功

#======================================================================================================开始具体的操作
#去4个广告
time.sleep(1)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='手机投注'])[1]/following::span[2]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='立即注册'])[1]/following::a[7]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='立即注册'])[1]/following::a[10]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='立即注册'])[1]/following::span[1]").click()

#登录
username=driver.find_element_by_xpath('//*[@class="login-before clear-fix"]/div/div[1]/input[1]')
password=driver.find_element_by_xpath('//*[@class="login-before clear-fix"]/div/div[1]/input[2]')
login_btn=driver.find_element_by_xpath('//*[@class="login-before clear-fix"]/div/div[2]/button[1]')

username.clear()
username.send_keys("sijiehua1")

password.clear()
password.send_keys("sijiehua123")
time.sleep(1)
login_btn.click()
time.sleep(4)


#选中游戏
driver.find_element_by_link_text(u"快乐飞艇").click()
time.sleep(2)
driver.find_element_by_link_text(u"排名1~10").click()


#取出期数
qi=driver.find_element_by_xpath('//div[@class="title-wrap"]/div/div[2]/span[1]').get_attribute("innerHTML")

#取出时间标题字符串
time_type=driver.find_element_by_xpath('//*[@class="time-title"]').get_attribute("innerHTML")
print(time_type)

#取出倒计时秒数
back_time=driver.find_element_by_xpath('//*[@class="time-wrap"]').get_attribute("innerHTML")
p = re.compile(r'<div.*?>\n\s+(.+?)\n\s+</div>',re.M|re.S|re.DOTALL)
time_strings="".join(p.findall(back_time))
time_sec=int(time_strings[2:4])*60+int(time_strings[4:6])

if ("投注截止" in time_type) and (time_sec>20):
    print("第"+qi+"期,离投注截止还有"+str(time_sec)+"秒。可以下注")


list_2=[]
for i in range(1,10+1):
    list_2.append("(.//*[normalize-space(text()) and normalize-space(.)='冠军'])[1]/following::input["+str(i)+"]")

time.sleep(3)

for k in list_2:
    driver.find_element_by_xpath(u''+str(k)).click()
    driver.find_element_by_xpath(u''+str(k)).clear()
    driver.find_element_by_xpath(u''+str(k)).send_keys("10")


time.sleep(10)
exit_a=driver.find_element_by_xpath('//label[@class="text exit"]/a')
exit_a.click()

handles = driver.window_handles
#print(handles)  # 输出句柄集合
driver.close()
os.system('taskkill /im chromedriver.exe /F')
driver.quit()
