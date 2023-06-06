#-*- coding:utf-8 -*-

#"执行程序"

import ctypes,os;
import win32api,win32con

#os.system('notepad.exe')
#os.system(r'e:\xx.bat')

def shellexe():
    handler = None;
    operator = "open";
    fpath = r"C:\Windows\System32\calc.exe"
    fpath = r'e:\xx.bat'
    param = None
    dirpath = None
    ncmd = 1
    win32api.ShellExecute(handler,operator,fpath,param,dirpath,ncmd)
    



