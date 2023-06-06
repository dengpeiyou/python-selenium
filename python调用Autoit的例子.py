# -*- coding: utf-8 -*-

#如果这个测试能运行，代表Pyautoit安装成功

import autoit
import time

autoit.run("notepad.exe")
time.sleep(2)
autoit.win_activate("无标题 - 记事本")
autoit.send("{LSHIFT}")
time.sleep(2)
autoit.send("#Process finished with exit code 0.",1)
time.sleep(2)
autoit.win_close("无标题 - 记事本")
autoit.win_activate("记事本")
time.sleep(2)
autoit.control_click("记事本","保存(&S)")
time.sleep(2)
autoit.win_activate("另存为")
autoit.control_set_text("另存为","[CLASS:Edit; INSTANCE:1]","myTest.txt")
time.sleep(2)
autoit.control_click("另存为","保存(&S)")
