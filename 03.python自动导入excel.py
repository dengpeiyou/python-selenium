#coding:utf-8
import os,time
import openpyxl
from openpyxl import load_workbook
import pymysql

#==========================================获取指定xlsx文件全部数据(返回二维列表)
def 读取文件(FileName):
    print(f"开始从Excel表{FileName}中读取数据...")
    t1 = time.time()
    wb = load_workbook(FileName)
    ws = wb.active
    AllData=[]
    for row in wb['Sheet0'].rows:
        line = [col.value for col in row]
        AllData.append(line)

    del(AllData[0])  #删除表头
    NewData=[]
    for row in AllData: #把第一列变成整数
        row[0]=str(int(row[0])).zfill(10)
        row.insert(0,0) 
        NewData.append(tuple(row))

    wb.close()
    t2 = time.time()
    print(f"读取数据完成，用时{round(t2 -t1,3)}秒。")   
    return NewData


def 打开数据库(Host,Port,UserName,Password,DbName,CharSet='utf8'):
    conn = pymysql.connect(host=Host,
                           port=Port,
                           user=UserName,
                           passwd = Password,
                           db = DbName,
                           charset = CharSet
                           )
    cur = conn.cursor()
    return (cur,conn)

def 导入数据(conn,cur,Listdata):
    #清空老数据
    ClearData="truncate table dangtian"
    cur.execute(ClearData)
    conn.commit()

    sql="INSERT INTO `dangtian` ( `id`,`serial`,`danwei`,`user_number`,`user_name`,`address`,`assets_code`,`event_type`,`meter_id`, \
`start_time`,`end_time`,`meter_model`,`div_code`,`ter_code`,`collect_time`)  VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print("开始导出数据到mysql表...")
    t1 = time.time()
    try:
        cur.executemany(sql,Listdata)
        conn.commit()
        t2 = time.time()
        print(f"导出数据完成,共导出了{cur.rowcount}行数据，用时{round(t2 -t1,3)}秒。")            
    except Exception as e:
        print(e)
        conn.rollback()
   
 
def 读取集抄库记录数(cur):
    CountRows="select count(id) from jichao"
    cur.execute(CountRows) 
    count_wm = cur.fetchall()[0][0] #获取总【集抄】表的记录数
    print( f"原有数据库记录{count_wm}条.")
    return  count_wm

def 数据是否存在(cur,dbfilename):
    #取【当天数据】表的第一个记录查到的停电日期
    QueryDate=f"select  Date(start_time) from {dbfilename} limit 1"
    cur.execute(QueryDate)
    数据日期=cur.fetchall()[0][0]
    
    CountRows=f"select count(id) from jzcb where Date(start_time) = '{数据日期}'"
    cur.execute(CountRows) 
    count_wm = cur.fetchall()[0][0] #查询【集抄】表里有没有当天数据    
    if count_wm >0:
        return  True
    else:
        return  False

def 修改ID(conn,cur,dbfilename):
    记录数=读取集抄库记录数(cur)
    #设置一个变量为r(在原来记数的基本上增加)    
    ModifyID1=f"set @r:={记录数}"
    #使用变量r来更新列中的值，同时r递增
    ModifyID2=f"UPDATE {dbfilename} SET id=(@r:=@r+1)"
    cur.execute(ModifyID1) 
    cur.execute(ModifyID2) 
    conn.commit()
def 数据表去重(conn,cur):
    #如果去重表存在就删除
    DropTable="drop table  if exists  去重表"
    DropTable="truncate  table 去重表"
    conn.commit()
    
    #把去重的查询结果保存在新建【去重表】
    RemoveDuplicates="CREATE TABLE 去重表 (SELECT  *   FROM dangtian FORCE INDEX(index_bianhao)  Group by user_number,start_time ORDER BY serial)"
    cur.execute(RemoveDuplicates)
    conn.commit()
    
    #把【当天数据】表清空
    ClearData="truncate table dangtian"
    cur.execute(ClearData)
    conn.commit() 
    
    #把【去重表】里的内容导入【当天数据】
    AppendData="insert into dangtian (select * from 去重表)"
    cur.execute(AppendData)
    print(f"去重后剩余数据{cur.rowcount}行。")    
    conn.commit()     

    #如果去重表存在就删除
    DropTable="drop table if exists  去重表"
    cur.execute(DropTable)
    conn.commit()
def 添加当天到集抄表(conn,cur,ScrDB,DestDB):
    #把数据从ScrDB表添加到DestDB表
    s1="`id`,`serial`,`danwei`,`user_number`,`user_name`,`address`,`assets_code`,`event_type`,`meter_id`,"
    s2="`start_time`,`end_time`,`meter_model`,`div_code`,`ter_code`,`collect_time`"
    字段=s1+s2
    sql=f"INSERT INTO jzcb ({字段}) SELECT {字段} FROM dangtian WHERE not exists (select * from jzcb,dangtian where jzcb.id =dangtian.id)"
  
    
    cur.execute(sql)
    print(f"总共添加了{cur.rowcount}条记录.")
    conn.commit() 


if __name__ == '__main__':

    #1.初始化参数
    XLSFileName="d:\\2020-05-05.xlsx"
    
    Host='localhost'
    Port=3333
    UserName="root"
    Password="dyj.2379"
    DbName="jichao"

    #2.连接数据库
    cur,conn=打开数据库(Host,Port,UserName,Password,DbName)
    
    #3.读取EXCEL表    
    数据=读取文件(XLSFileName)  
    
    #4.导入EXCEL到数据表
    导入数据(conn,cur,数据)
    
    #5.数据表去重(如果用户编号和停电发生时间表都相同为一条重复记录)
    数据表去重(conn,cur)
    
    #6.检查数据是否存在
    RecordExsit=数据是否存在(cur,"dangtian")
    if not  RecordExsit:  
        #7.修改id列为自增(在【集抄】数据表之后增加)
        修改ID(conn,cur,"dangtian")
        
        #8.添加整理好的记录【当天数据】到数据表【集抄】（如果存在则不追加）
        添加当天到集抄表(conn,cur,"dangtian","jzcb")
    else:
        print("你要插入的数据已经存的，0行数据被处理。")
             
    cur.close()   #先关闭游标
    conn.close()  #再关闭数据库连接
    print("程序运行完毕！！！")
