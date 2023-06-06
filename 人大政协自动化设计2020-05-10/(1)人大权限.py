#coding=utf-8
from modules import *

if __name__ == '__main__':
    
    人大路由代码={"提交建议":"work1","提交网上监督":"work2","发起活动":"work3","发起会议":"work4","提交报告":"work5",\
          "通知公告":"work6","用户管理":"work7","角色管理":"work8","组织管理":"work9","资源管理":"work10",\
          "字典管理":"work11","机构设置":"work12","联系人管理":"work13","意见反馈":"work14","常见问题":"work15",\
          "登录统计":"work16","设备管理":"work17","设备WEB管理":"work18","设置区域管理":"work19","短信提醒":"work20",\
          "代表之家信息":"work21","代表之家评价":"work22","发起建议评议":"work23","建议催办":"work24","添加代表":"work25",\
          "发起履职评价":"work26","届次管理":"work27","使用指南":"work28"}
    
    RGB色值=["#0BBBBB","#BEA3F4","#639ED8","#BEA3F4","#639ED8","#0BBBBB","#0BBBBB","#BEA3F4",
           "#639ED8","#BEA3F4","#639ED8","#0BBBBB","#0BBBBB","#BEA3F4","#639ED8","#BEA3F4","#639ED8","#0BBBBB"]
    数据文件="人大权限数据.xlsx"

    url = "http://47.92.122.118:8000/#/login"
    driver=browser_init(url)                          #打开网址
    dpi=1
    user_login(driver,"xxhzj","JRKJ@jqrj*369")
    #user_login(driver,"xxhzj","111111")               #超管用户登录
    
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="el-submenu__title" ]').click()  #更多

    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="el-menu--horizontal"]//li[contains(text(),"系统管理")]').click()  #系统管理
    time.sleep(1.5)
    租户按钮=driver.find_element_by_xpath('//ul[@class="el-menu-vertical-demo left_menu hideBar el-menu"]/li/span[text()="租户管理"]')
    driver.execute_script("arguments[0].scrollIntoView();",租户按钮)
    租户按钮.click()  
    time.sleep(1)
    
    添加=driver.find_element_by_xpath('//div[@class="grid-content bg-purple-dark"]/button/span[text()="添加"]/..')
    添加.click()
    time.sleep(1)

   
    角色列表=ReadData(数据文件,"角色权限")          #从excel表读数据
    角色数量=len(角色列表)
    工作台组件=ReadData(数据文件,"工作台")          #从excel表读数据
    tip=显示气泡("任务处理中...")
    starttime = datetime.datetime.now()
   
    tip.showMsg("添加角色..."," ")
    添加角色(driver,角色列表)    #添加角色
   
    tip.showMsg("为角色添加组件..."," ")
    添加组件(driver,角色列表)    #为角色添加组件
   
    tip.showMsg("为工作台添加组件..."," ")
    添加工作台组件(driver,工作台组件,人大路由代码,RGB色值) #为工作台添加组件

    endtime = datetime.datetime.now()
    user_time="软件设置权限决共花了{0}秒".format((endtime - starttime).seconds)
    print(user_time)
    tip.showMsg("任务处理成!!!", user_time)
    time.sleep(3)
    关闭气泡(tip)
    
    driver.quit()
