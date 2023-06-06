#coding:utf-8
#=====================================================================
#=====本程序演示了WINREG操作WINDOWS注册表的所有常见操作
#=====作者:dengpeiyou QQ：86074731 2019.01.12
#=====================================================================
import ctypes
import winreg
import os

#===============================================================打开子键
key=None
try:
    key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"software")
except Exception as error_txt:
    #提示
    #ctypes.windll.user32.MessageBoxW(None,str(error_txt),'打开',0)
    ctypes.windll.user32.MessageBoxW(None,'打开注册表异常','打开',0)
    os._exit(0)

#如果打开则关闭
if key:
    winreg.CloseKey(key)

#================================================================新建(修改)子键
winreg.CreateKey(winreg.HKEY_CURRENT_USER,r'software\dengpeiyou')
winreg.CreateKey(winreg.HKEY_CURRENT_USER,r'software\dengpeiyou\testa')
#添加键值
list_keys=[('aa1',winreg.REG_SZ,'a001'),('aa2',winreg.REG_DWORD,64),('aa3',winreg.REG_SZ,'99999')]
key_a=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'software\dengpeiyou\testa',0,winreg.KEY_SET_VALUE)
#建立1+3个键值
winreg.SetValueEx (key_a, "", 0, winreg.REG_SZ,'55555')  #名称为空指定默认值
for i in range(len(list_keys)):
    winreg.SetValueEx(key_a, list_keys[i][0], 0, list_keys[i][1], list_keys[i][2])
winreg.CreateKey(winreg.HKEY_CURRENT_USER,r'software\dengpeiyou\testb')
winreg.CreateKey(winreg.HKEY_CURRENT_USER,r'software\dengpeiyou\testc')
winreg.CloseKey(key_a)

#=================================================================读取子值
key_a=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'software\dengpeiyou\testa',0,winreg.KEY_QUERY_VALUE)

#遍历方法一
#项数
countkey=winreg.QueryInfoKey(key_a)[1] #返回元组(子值数,项数,长整数)
keylist=[]
for i in range(countkey):
    name, key_value, value_type = winreg.EnumValue(key_a, i)
    keylist.append((name,key_value,value_type))
print(keylist)

#另一种遍历方法
try:
    i = 0
    while True:
        name, value, value_type = winreg.EnumValue(key_a, i)
        i += 1
        print("项名：%5s     值：%5s     类型:%1d" % (name, value, value_type))
except Exception as e:
    pass
    #print('查找完了')

winreg.CloseKey(key_a)
#==================================================================删除值和子键

key_name=r'software\dengpeiyou\testa'
key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,key_name,0,winreg.KEY_SET_VALUE)
#这句正确执行的前提是前面打开时加winreg.KEY_SET_VALUE参数，否则报错无法执行
winreg.SetValueEx(key, "aa3", 0, winreg.REG_SZ,'123456')  #修改一个存在的项值(如果不存在则新建)
try:
    winreg.DeleteValue(key,"aa1") #而删除值项相对简单
except FileNotFoundError:
    ctypes.windll.user32.MessageBoxW(None,'要删除的值不存在','提示',16) 

winreg.CloseKey(key)

#技术含量最大的一个函数，可以递归删除所有子键和值(包括自身)，请慎用!!!
def find_key(key_str):
    try:
        key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,key_str)
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(None,'打开注册表异常','提示',16)
        return
    
    countkey=winreg.QueryInfoKey(key)[0] #子键数
    #print("%s有%d个子键."%(key_str,countkey))
    if countkey!=0:
        for i in range(countkey-1,-1,-1):
            key_name=winreg.EnumKey(key,i) #取键名
            find_key(key_str+"\\"+key_name)
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_str)
    except FileNotFoundError:
        pass

str1=r'software\dengpeiyou'
#find_key(str1)


