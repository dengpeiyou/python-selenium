#coding=utf-8
from modules import *

def  删除工作台组件(driver,工作台组件):    
    #左侧【主页组件管理】
    time.sleep(1.5)
    主页组件=driver.find_element_by_xpath('//ul[@class="el-menu-vertical-demo left_menu hideBar el-menu"]/li/span[text()="主页组件管理"]')
    driver.execute_script("arguments[0].scrollIntoView();",主页组件)
    主页组件.click()        
    
    #数据行数
    rows=driver.find_elements_by_xpath(f'//div[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr')
    row_count=len(rows)
    
    time.sleep(1)
    #逐行进行处理(正序处理)
    j=1
    for row_index in range(row_count):
        time.sleep(1.5)
        row=driver.find_element_by_xpath(f'//div[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[{row_index+1}]')
        编辑组件=row.find_element_by_xpath('./td[3]/div/button/span[contains(text(),"编辑组件")]/..')

        #角色列表-->【编辑组件】点击
        编辑组件.click()   
        time.sleep(1)          

        #如果工作台【编辑组件】按钮不在，程序立刻返回
        if not 工作台(driver):
            #如果没有工作台点【取消】退出检查下一个
            ComponentManageCancel=driver.find_element_by_xpath('//div[@role="dialog" and @aria-label="组件管理"]/div[3]/span/button[1]')
            ComponentManageCancel.click()   
            time.sleep(0.5)
            continue    #如果没有工作台取消后执行下一个


        #【工作台】-->【编辑组件】(查找有3个按钮的表格行，看哪个是工作台编辑)
        #组件列表-->【编辑组件】点击
        driver.find_element_by_xpath('//div[@role="dialog" and @aria-label="组件管理"]//table/tbody/tr/td[7]/div[count(button)=3]/button[1]').click()
        time.sleep(0.5)
        
        j=j+1
        
        #如果有工作台(循环处理添加所有工作台组件)
        trs=driver.find_elements_by_xpath('//div[@role="dialog" and @aria-label="工作台组件管理"]//tbody/tr[@class="el-table__row"]') 
        for k in range(len(trs)):
            删除按钮=trs[0].find_element_by_xpath('//td[6]/div/button[2]') 
            删除按钮.click()
            time.sleep(0.3)
        #for循环结束            
                        
        #工作台组件管理【确定】
        try:
            PlatManagetOK=driver.find_element_by_xpath('//div[@role="dialog" and @aria-label="工作台组件管理"]/div[3]/span/button') 
            PlatManagetOK.click() 
            time.sleep(0.5)
        except:
            pass
        #组件管理【确定】
        try:
            driver.find_element_by_xpath('//div[@role="dialog" and @aria-label="组件管理"]/div[3]/span/button[2]').click()  
            time.sleep(0.5)
        except:
            pass


#===================================================================================================================================33.为角色添加组件
def 删除角色(driver,角色列表):
    time.sleep(1)
    主页组件=driver.find_element_by_xpath('//ul[@class="el-menu-vertical-demo left_menu hideBar el-menu"]/li/span[text()="主页组件管理"]')
    driver.execute_script("arguments[0].scrollIntoView();",主页组件)
    主页组件.click()  
    
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="el-input el-input--mini el-input--suffix"]/span').click()     #点击每页显示列数
    time.sleep(0.5)
    
    driver.find_element_by_xpath('//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[last()]').click() #选最大页数
    time.sleep(1)
    
    
    i=0
    #倒序遍历所有角色(取出列表里的每个字典进行处理)
    #for_A循环开始
    time.sleep(0.5)
    
    tres=driver.find_elements_by_xpath('//table[@class="el-table__body"]/tbody/tr')
    first_row=driver.find_elements_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]//tr')[0]
    for i in  range(len(tres)):
        time.sleep(0.8)
        #获取【删除】按钮
        删除按钮=first_row.find_element_by_xpath('./td[3]/div/button[3]')
        删除按钮.click()   #点击[删除按钮]
        time.sleep(0.5)
        #点击提示里的【确定】按钮
        driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()   
        i=i+1  #处理指针上移一行
    #for_A循环结束





#===================================================================================================================================
if __name__ == '__main__':
    
    政协路由代码={'提交提案':'work1','提交社情民意':'work2','发起活动':'work3','发起会议':'work4','提交报告':'work5',\
        '通知公告':'work6','用户管理':'work7','角色管理':'work8','组织管理':'work9','资源管理':'work10',\
        '字典管理':'work11','机构设置':'work12','联系人管理':'work13','意见反馈':'work14','常见问题':'work15',\
        '登录统计':'work16','设备管理':'work17','设备WEB管理':'work18','设置区域管理':'work19','短信提醒':'work20',\
        '委员之家信息':'work21','委员之家评价':'work22','发起提案评议':'work23','提案催办':'work24','添加委员':'work25',\
        '发起履职评价':'work26','届次管理':'work27','使用指南':'work28'}

    RGB色值=["#0BBBBB","#BEA3F4","#639ED8","#BEA3F4","#639ED8","#0BBBBB","#0BBBBB","#BEA3F4",
           "#639ED8","#BEA3F4","#639ED8","#0BBBBB","#0BBBBB","#BEA3F4","#639ED8","#BEA3F4","#639ED8","#0BBBBB"]    


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
    
    #01.添加角色
    tip.showMsg("添加角色..."," ")
    #政协添加角色(driver,角色列表)   
    
     #02.为角色添加组件
    tip.showMsg("为角色添加组件..."," ")
    #政协添加组件(driver,角色列表)   

    
    #03.为工作台添加组件
    tip.showMsg("为工作台添加组件..."," ")
    #添加工作台组件(driver,工作台组件,政协路由代码,RGB色值) 
    #删除工作台组件(driver,工作台组件)
    #删除角色(driver,角色列表)
    
    endtime = datetime.datetime.now()
    user_time="软件设置权限决共耗时{0}秒".format((endtime - starttime).seconds)
    print(user_time)
    
    tip.showMsg("任务处理完成!!!", user_time)
    time.sleep(3)
    关闭气泡(tip)
    
    driver.quit()
