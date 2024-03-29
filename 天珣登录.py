# Generated by Selenium IDE
import os
import time

import ddddocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tianxun:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt.add_argument("--disable-infobars")  # 关闭安全提示条
        opt.add_argument("--ignore-certificate-errors")
        opt.add_argument("--start-maximized")  # 启动即最大化
        opt.add_argument("--disable-popup-blocking")  # 禁用弹出拦截
        opt.add_argument("no-sandbox")  # 关闭沙盘
        opt.add_argument("disable-extensions")  # 扩展插件检测
        opt.add_argument("no-default-browser-check")  # 默认浏览器检测

        # 关闭弹出密码提示
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        opt.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=opt)
        self.vars = {}

    def __del__(self):
        self.driver.quit()

    def savePict1(self, filename, pictSelector):  # =============================================保存图片
        element = self.driver.find_element(By.CLASS_NAME, pictSelector)  # 定位验证码图片
        # 获取验证码图片在网页中的位置
        left = int(element.location['x'])  # 获取图片左上角坐标x
        top = int(element.location['y'])  # 获取图片左上角y
        right = int(element.location['x'] + element.size['width'])  # 获取图片右下角x
        bottom = int(element.location['y'] + element.size['height'])  # 获取图片右下角y

        # 通过Image处理图像
        self.driver.save_screenshot(filename)  # 截取当前窗口并保存图片
        im = Image.open(filename)  # 打开图片
        im = im.crop((left, top, right, bottom))  # 截图验证码
        im.save(filename)  # 保存验证

    def get_chkcode(self, filename, pictSelector):  # 获取验证码
        self.savePict1(filename, pictSelector)
        ocr = ddddocr.DdddOcr()
        with open(filename, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        return res

    def login(self):  # ===========================================================================登录主网页
        self.driver.get("https://25.213.45.246:8834/Auth/login?id={D13CE6B1-157B-A807-4BC5-84397F5B2DFC}")
        time.sleep(1)
        UserXpath = r'//input[@placeholder="帐 号"]'

        inputUserName = self.driver.find_element(By.XPATH, UserXpath)
        inputUserName.click()
        inputUserName.send_keys("yuanyang")
        PasswordXpath = r'//input[@placeholder="密 码"]'
        self.driver.find_element(By.XPATH, PasswordXpath).click()
        self.driver.find_element(By.XPATH, PasswordXpath).send_keys("*********")
        url = "el-image"
        pictFilenNme = "tempchkcode.png"
        retCode = self.get_chkcode(pictFilenNme, url)  # 获取验证码
        os.remove(pictFilenNme)
        inputCode = self.driver.find_element(By.XPATH, '//input[@placeholder="验证码"]')
        inputCode.click()
        inputCode.send_keys(retCode)
        LoginBtn = self.driver.find_element(By.XPATH, "//div[@class='login-button-div']/button")
        LoginBtn.click()

    def loginSuccess(self):
        time.sleep(2)
        ret = self.driver.find_elements(By.CSS_SELECTOR, 'div[ class ="yj-product-name-1"]')
        if len(ret) == 0:
            return  False
        else:
            return True

    def open_new_window(self):  # ===========================================打开一个新网页请求未受控设备列表
        self.driver.switch_to.new_window()
        self.driver.get("https://25.213.45.246:8834/Report/RepClient?selecttype=uncontrol")
        time.sleep(3)

    def process_pc(self):  # ==========================================================获取到未受控表格并点击
        pcTable = r'//table[@class="el-table__body"]/tbody/tr'
        unControlList = self.driver.find_elements(By.XPATH, pcTable)
        num = 0
        for i in range(len(unControlList)):
            pcName = unControlList[i].find_element(By.XPATH, ".//td[3]/div").text
            if len(pcName.strip()) < 1:
                unControlList[i].find_element(By.XPATH, ".//td[7]/div/span/button").click()  # 终端类型上单击
                time.sleep(2)
                terminalFullPath = '/html/body/div[%s]/div[1]/div[1]/div/div[8]/div/button/span' % (num + 3)
                num = num + 1
                self.driver.find_element(By.XPATH, terminalFullPath).click()  # 在弹出的右键菜单上选<其它设备>
                time.sleep(2)


if __name__ == "__main__":
    Page = Tianxun()
    Page.login()
    if not Page.loginSuccess():
        Page.login()
    Page.open_new_window()
    Page.process_pc()
    Page.__del__()
