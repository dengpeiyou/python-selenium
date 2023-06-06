#coding=utf-8
import os

def findSubStrIndex(initstr,substr,time):  # 找字符串substr在str中第time次出现的位置
    times = initstr.count(substr)
    if (times == 0) or (times < time):
        pass
    else:
        i = 0
        index = -1
        while i < time:
            index = initstr.find(substr, index+1)
            i+=1
        return index


def RenameIndex(path,filename):
    index1=findSubStrIndex(filename, ".", 1)
    index2=findSubStrIndex(filename, ".", 2)
    if index1!=None and index2!=None:
        str1=filename[:index1]
        PreStr='%04d.' % int(str1)
        str2=filename[index1+1:]
        NewFileName=PreStr+str2
        os.rename(os.path.join(path, filename),os.path.join(path,NewFileName))

import os

path =os.getcwd()
for file in os.listdir(path):
    RenameIndex(path,file)
