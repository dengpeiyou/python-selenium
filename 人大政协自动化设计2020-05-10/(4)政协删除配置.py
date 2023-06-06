#coding=utf-8
from modules import *


#===================================================================================================================================
if __name__ == '__main__':
    
    数据="政协权限数据.xlsx"

    url = "http://117.158.91.116:8003/#/login"
    driver=browser_init(url)                          #打开网址
    dpi=1
    user_login(driver,"wbqzx","111111")               #登录
    
    #更多
    time.sleep(3)
    driver.find_element_by_xpath('//div[@class="el-submenu__title" ]').click()  
    #【系统管理】
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="el-menu--horizontal"]//li[contains(text(),"系统管理")]').click()  
    time.sleep(1) 
     #读数据
    角色列表=ReadData(数据,"角色权限")  
    工作台组件=ReadData(数据,"工作台")  

    starttime = datetime.datetime.now()
    tip=显示气泡("任务处理中...")    


    #1.删除工作台
    tip.showMsg("删除工作台..."," ")
    删除工作台组件(driver,工作台组件)

    #2.删除角色
    tip.showMsg("删除角色..."," ")
    删除角色(driver,角色列表)
    
    endtime = datetime.datetime.now()
    user_time="删除配置共耗时{0}秒".format((endtime - starttime).seconds)
    print(user_time)
    
    tip.showMsg("任务处理完成!!!", user_time)
    time.sleep(3)
    关闭气泡(tip)
    
    driver.quit()
