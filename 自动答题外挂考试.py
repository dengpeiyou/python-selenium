#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


        
#登录考试系统
def login():
    
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option("excludeSwitches", ['enable-automation'])
    opt.add_argument("--disable-infobars")          #关闭安全提示条
    opt.add_argument("--start-maximized")         #启动即最大化
    opt.add_argument("--disable-popup-blocking")  #禁用弹出拦截 
    opt.add_argument("no-sandbox")                #关闭沙盘
    opt.add_argument("disable-extensions")        #扩展插件检测
    opt.add_argument("no-default-browser-check")  #默认浏览器检测
    
    #关闭弹出密码提示
    prefs = {"":""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    opt.add_experimental_option("prefs", prefs)
    
    driver=webdriver.Chrome(options=opt)
    driver.set_window_position(500,0) # 位置 500,50
    driver.set_window_size(800,1000) # 分辨率 800*600
    
    driver.get("https://b.u.mgd5.com/c/vxpa/7jgw/index.html")
    driver.implicitly_wait(15)
    driver.find_element_by_xpath("//img[contains(@src,'https://cdn3.u.mgd5.com/c/vxpa/7jgw/images/6059dfc74fc92d30dc58e0fc.png')]").click()
    driver.find_element_by_xpath("//select").click()
    
    #选择单位
    Select(driver.find_element_by_xpath("//select")).select_by_visible_text(u"国网河南省电力公司")
    driver.find_element_by_xpath("//select").click()
    driver.find_element_by_xpath("//select[2]").click()
    Select(driver.find_element_by_xpath("//select[2]")).select_by_visible_text(u"新乡供电公司")
    driver.find_element_by_xpath("//select[2]").click()
    driver.find_element_by_xpath("//select[3]").click()
    Select(driver.find_element_by_xpath("//select[3]")).select_by_visible_text(u"原阳县供电公司")
    driver.find_element_by_xpath("//select[3]").click()
    
    #点击提交
    driver.find_element_by_xpath("//div[2]/div/div/div/div[2]/div/div").click()
    return  driver

#依次点击题库
def  ClickAnser(driver):
    isBegin=False
    Number=0
    while Number<10:
        try:
            x=driver.find_elements_by_xpath("//*[@fill='rgba(139,195,74,1)']/../../..")
            for x1 in x:
                if "display: block" in x1.get_attribute('style'):
                    x1.click() 
                    Number=Number+1
                    isBegin=True
                    time.sleep(random.random()+0.2)
        except:
            pass
    
        if not isBegin: continue
    
        try:
            x=driver.find_elements_by_xpath("//*[@src='https://cdn1.u.mgd5.com/c/vxpa/7jgw/images/5e58b966ecb65e45704dbbaf.webp']/..")
            for x1 in x:
                if "display: block" in x1.get_attribute('style'):
                    x1.click()        
                    time.sleep(random.random()+0.2)
        except:
            pass
        time.sleep(random.random()+0.8)

#提交信息
def submit(driver,user,phone,company):
    time.sleep(1)
    driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(user)
    driver.find_element_by_xpath("//input[@type='tel']").click()
    driver.find_element_by_xpath("//input[@type='tel']").clear()
    driver.find_element_by_xpath("//input[@type='tel']").send_keys(phone)
    driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(company)
    driver.find_element_by_xpath("//img[contains(@src,'https://cdn3.u.mgd5.com/c/vxpa/7jgw/images/587732fdaeece10a990cf324.png')]").click()

if __name__ == '__main__':
   
    UserList=[]
    UserList.append(["邓沛友","18237383593","国网原阳县供电公司"])
    UserList.append(["朱志斌","13903738928","国网原阳县供电公司"])
    
    #UserList.append(["史鹏恩","13569426060","国网原阳县供电公司"])
    #UserList.append(["孙国敏","18749116226","国网原阳县供电公司"])
    #UserList.append(["鲁敏","18738500016","国网原阳县供电公司"])
    #UserList.append(["李彦坤","13938724312","国网原阳县供电公司"])
    #UserList.append(["刘通阳","13462248088","国网原阳县供电公司" ])
    #UserList.append(["宋佩佩","15893830970","国网原阳县供电公司"])
    #UserList.append(["娄世金","13613901399","国网原阳县供电公司"])


    循环次数=50 #循环次数
    for j in range(循环次数):
        #这是第一个for循环的语句
        j=j+1        
        for UserMsg in UserList:
            driver=login()  #登录
            ClickAnser(driver) #点击答案
            submit(driver,UserMsg[0],UserMsg[1],UserMsg[2])
            
            time.sleep(2)
            driver.quit()
            print("%s答题第%d次完毕！"  % (UserMsg[0],j))
