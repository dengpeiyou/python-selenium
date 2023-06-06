#coding:utf-8
import win32api, win32con


#取出用户DPI
#HKEY_CURRENT_USER\Control Panel\Desktop\LogPixels
def DPI():
    reg_root = win32con.HKEY_CURRENT_USER
    reg_path = r"Control Panel\Desktop"
    reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
     
    #读取键值
    key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
    value, key_type = win32api.RegQueryValueEx(key, 'LogPixels')
    win32api.RegCloseKey(key)
    return value/96

#该参数决定是否使用用户DPI
#HKEY_CURRENT_USER\Software\Microsoft\Windows\DWM\UseDpiScaling
def user_DPI():
    reg_root = win32con.HKEY_CURRENT_USER
    reg_path = r"Software\Microsoft\Windows\DWM"
    reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
     
    #读取键值
    key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
    value, key_type = win32api.RegQueryValueEx(key, 'UseDpiScaling')
    win32api.RegCloseKey(key)
    return value



def screen_xy(sys_dpi=1):
    if user_DPI():
        x=int(win32api.GetSystemMetrics(win32con.SM_CXSCREEN)*sys_dpi)
        y=int(win32api.GetSystemMetrics(win32con.SM_CYSCREEN)*sys_dpi)
    else:
        x=int(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
        y=int(win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
    return (x,y)

scr=screen_xy(DPI())
print("当前用户的DPI比例是:",DPI())
print('屏幕实际的分辨率:',scr)

