#coding=utf-8
import time,sys,os


PyPath=os.path.dirname(sys.executable) #获取python安装位置
filename=PyPath+r"\Lib\site-packages\selenium\webdriver\common\service.py"

f=open(filename,"r+")  
lines=f.readlines()   #先读到一个列表里


#判断75行是否修改过(没修改则进行修改)
if not ("creationflags" in lines[75]):
    lines[75]=lines[75][0:-2]+",creationflags=134217728)\n"

#把修改过的数据写入
f=open(filename,"w+")
f.writelines(lines)


#关闭文件真正写入
f.close()
print("修改成功!!!")
time.sleep(1)
