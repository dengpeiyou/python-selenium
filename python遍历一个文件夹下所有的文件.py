#os.walk(rootdir[,Ture or False),如果第二个参数是False则从最深层目录开始遍历
#os.walk:遍历指定目录下的所有文件和文件夹,返回一个三元组
#root,为当前目录，dirs为当前子录，filse是当前目录 下的所有文件

import os

filelist=[]
sourcepath=r"d:\aa"
for root,dirs,files in os.walk(sourcepath):
    for sourcepath in files:
        path=os.path.join(root,sourcepath)
        filelist.append(path)

for file in filelist:
    print(file)


#只列出当前目录根目录下的文件
print("开始执行第二段程序：")
sourcepath=r"d:\aa"
for root,dir,files in os.walk(sourcepath):
    if root!=sourcepath:
        break
    for file in files:
        path=os.path.join(root,file)
        print(path)


#只列里当前目录下的所有的文件
print("第三段程序开始执行:")
sourcepath=r"d:\aa"

#files = (file for file in os.listdir(sourcepath) if os.path.isfile(os.path.join(sourcepath, file)))

for file in os.listdir(sourcepath):
    file=os.path.join(sourcepath, file)
    if os.path.isfile(file):  #如果这里改成os.path.isdir()那就是只列出当前目录的文件夹
        print(file)



#只列里当前目录下的所有的文件
print("第四段程序开始执行:")
sourcepath=r"d:\aa"
files=[x for x in filter(os.path.isfile, [os.path.join(sourcepath,fName) for fName in os.listdir(sourcepath)])]

#一次情把一个列表添加到一个指定列表
filelist.clear()
filelist.extend(files)
print(filelist)


