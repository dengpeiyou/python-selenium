import ctypes, sys,os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    print("现在是管理员")
else:
    print("现在不是管理员")
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    print("获取管理员成功!")
    
print("现在正以管理员权限运行了")
os.system('e:\\xx.bat')

