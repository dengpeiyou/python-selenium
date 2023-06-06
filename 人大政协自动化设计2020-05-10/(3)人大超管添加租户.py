#coding=utf-8
from modules import *

if __name__ == '__main__':
    
    数据文件="人大权限数据.xlsx"

    url = "http://47.92.122.118:8000/#/login"
    driver=browser_init(url)                          #打开网址
    dpi=1
    user_login(driver,"xxhzj","JRKJ@jqrj*369")        #超管用户登录
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="el-submenu__title" ]').click()  #更多
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="el-menu--horizontal"]//li[contains(text(),"系统管理")]').click()  #系统管理

    #准备数据
    租户数据=ReadData(数据文件,'创建租户')
    资源=读取资源(数据文件,'关联资源')
    
    #添加租户(driver,租户数据)
    #添加用户管理员(driver,租户数据)

    #角色管理
    driver.find_element_by_xpath("//div[@id='app']/section/div/div/aside/ul/li[2]/span").click()
    time.sleep(1.5)
    #每页显示40条
    driver.find_element_by_xpath("//div[@id='app']/section/div/div/section/div/div[2]/div/div[3]/div/div/span[2]/div/div/span/span/i").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div/ul/li[5]/span").click()
    time.sleep(1)  
  

    #查找租户是否存在，不存在则添加
    租户列表=driver.find_elements_by_xpath("//div[@id='app']//table/tbody/tr/td[2]/div")
    存在=False
    for i in   range(len(租户列表)):
        if 租户列表[i].text==(租户数据[0]['管理员']):
            存在=True
            break
       
    #添加
    if 存在:
        print("你要添加的用户已经存在!")
        租户复选框=driver.find_element_by_xpath(f"//div[@id='app']//table/tbody/tr[{i+1}]/td[1]/div/label/span/span")
        租户复选框.click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//div[@class="grid-content bg-purple-dark"]/button[4]/span').click()
        time.sleep(6)
        资源大类列表=driver.find_elements_by_xpath('//div[@role="tree" and @class="el-tree"]/div/div[1]/span[1]')  
        for i in range(len(资源大类列表)):
            资源大类列表[i].click()
            time.sleep(0.2)
        
        
    else:
          print("找不到指定的用户!")

    sub_sele=driver.find_elements_by_xpath('//div[@role="tree" and @class="el-tree"]/div/div[2]/div') 
    for i in range(len(sub_sele)):
        check_button=sub_sele[i].find_element_by_xpath('./div/label/span/span')
        print(check_button.get_attribute('outerHTML'))
    k=0
    

    
   # driver.quit()
