import os
import xlwings as xw

##====================================01.获取目录下的所有文件
def GetFileList(path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            GetFileList(cur_path, all_files)
        else:
            all_files.append(cur_path)
 
    return all_files
##====================================02.应用初始化
def AppInit():
    app=xw.App(visible=True,add_book=False)
    app.display_alerts=False
    app.screen_updating=False
    return app
##====================================03.获取工作薄中工作表的名称列表
def SheetNameList(wb):
    SheetNum =len(wb.sheets)                                  #Sheet数
    sheetList = [wb.sheets[i].name for i in range(0,SheetNum)]  #Sheet名称
    return sheetList
##====================================04.获取工作薄中某一列的数据
def GetColData(st,ColNumber,HeadRows=1):
    #ColNumber:获取第几列数据
    #HeadRows:标题行数
    rows = st.used_range.last_cell.row  #行数
    return st.range((HeadRows+1,ColNumber),(rows,ColNumber)).value
##====================================05.获取工作薄中某一行的数据
def GetRowData(st,RowNumber,HeadRows=1):
    #RowNumber:获取第几行数据
    #HeadRows:标题行数
    Cols = st.used_range.last_cell.column  #列数
    return st.range((HeadRows+RowNumber,1),(HeadRows+RowNumber,Cols)).value
##=====================================06.遍历工作表所有的数据
def CheckTable(wb):
    info = wb.used_range
    nrows = info.last_cell.row  #行数
    ncolumns = info.last_cell.column #列数
    for j in range(1,1+nrows):
        for i in range(ord('A'),ord('A')+ncolumns):
            print(st[chr(i)+str(j)].value,end="\t")
            pass
        print('\n')
##=====================================07.删除一行数据
def DeleteRow(wb,nRow,HeadRows=1):
    wb.range('A%s' % (nRow+HeadRows)).api.EntireRow.Delete() 
##=====================================08.删除一列数据
def DeleteCol(wb,nCol):
    wb.range((1,nCol)).api.EntireColumn.Delete()   
#写操作
#CurrentSheet.range('B1').value=['1','2','3'] #给横向的连续单元格赋值
#CurrentSheet.range('B1').options(transpose=True).value=['a2','b2','c2'] #给纵向的连续单元格赋值
#CurrentSheet.cells(10,10).value = 'Hello Xlwings' #给指定的单元格赋值


# # 是否筛选
# if wb.sheets[0].api.AutoFilterMode == True:
#     # 取消筛选
#     wb.sheets[0].api.AutoFilterMode = False

# # 筛选
# wb.sheets[0].range((1,1),(mrows,ncolumns)).api.AutoFilter(field=int(ncolumns), Criteria1="=1", False)
# EndChar=chr(ord('A')+ncolumns-1) 
# list1=CurrentSheet['A1:'+EndChar+'1'].value
# print(list1)

# list2=CurrentSheet.range[(1,1),(1,14)].value 
# print(list2)
##=====================================00.测试代码
def test(st):
    pass
    # #==================================================================获取工作表的总行数和总列数
    # info = st.used_range
    # nrows = info.last_cell.row  #行数
    # ncolumns = info.last_cell.column #列数

    # #==================================================================获取某列数据调用
    # nColData=GetColData(st,1) #指定列数,默认标题1行
    # #print(nColData)
   
    # #==================================================================获取某行数据调用
    # nRowData=GetRowData(st,1)
    # print(nRowData)

    # #==================================================================遍历数据表调用
    # CheckTable(st)
    # #==================================================================删除一行数据
    # DeleteRow(st,2)
    # #==================================================================删除一列数据
    DeleteCol(st,3)

if __name__=="__main__":
    CurPath=r'D:\整改率可用率明细20230504'   #路径
    FileList=[]
    GetFileList(CurPath, FileList)

    app=AppInit()                         #App初始化

    #打开指定工作薄
    wb = xw.Book(FileList[4])             #打开
    SheetNames=SheetNameList(wb)          #获取工作表名
    st=wb.sheets[SheetNames[0]]           #选中第一个工作表
    
    test(st)                               #测试

    wb.save()  #保存
    wb.close() #关闭
    app.quit() #退出wps表格



