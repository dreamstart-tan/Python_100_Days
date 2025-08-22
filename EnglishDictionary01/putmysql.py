import pymysql
import xlrd

book = xlrd.open_workbook(r'D:\Py100\Python_100_Days\EnglishDictionary01\2021new.xls')
sheet = book.sheet_by_name('Sheet1')
wordcol = sheet.col_values(0)[1:]
classcol = sheet.col_values(1)[1:]
meancol = sheet.col_values(2)[1:]
capitalcol = sheet.col_values(3)[1:]
sourcol = sheet.col_values(4)[1:]
conn = pymysql.connect(
    host = '127.0.0.1', # 数据库地址 本地地址
    user = 'root',  # 用户名
    passwd='hao123',  # 密码
    port = 3306,    #端口，默认3306
    db = 'dictionary', #数据库名称
    charset = 'utf8'    # 字符编码
    )


tablename = "mainword"
cur = conn.cursor() # 生成游标对象
sql1 = "select word from mainword"
cur.execute(sql1)
data = cur.fetchall()
print(data)
datalist = []
for i in data:
    datalist.append(i[0])
print(datalist)
for i in range(len(wordcol)):
    if wordcol[i] in datalist:
        print(wordcol[i] + "已存在")
        sql3 = "select wordcount from mainword where word = \"" + wordcol[i]+"\""
        cur.execute(sql3)
        data = cur.fetchall()
        print(data[0][0])
        sql4 = "UPDATE mainword SET wordcount = " + str(data[0][0]+1)+ " where word = \"" + wordcol[i]+"\""
        print(sql4)
        cur.execute(sql4)
        sql3 = "select wordcount from mainword where word = \"" + wordcol[i] + "\""
        cur.execute(sql3)
        data = cur.fetchall()
        print(data)
        conn.commit()
    else:

        # ==================插入语句================
        sql2 = "INSERT INTO " + tablename + "(word,wordclass,mean,capital,source,wordcount) VALUES "+"(\"" + wordcol[i] + "\",\""+classcol[i] + "\",\"" + meancol[i] + "\",\""+capitalcol[i]+"\",\""+sourcol[i]+"\",\"1\");"

        try:
            cur.execute(sql2) # 执行插入的sql语句
            """
              for i in data[:]:  # 打印输出所有数据
                print(i)
            conn.commit()      # 提交到数据库执行              
            """
            data = cur.fetchall() # 通过fetchall方法获得数据
            conn.commit() # 提交到数据库执行
            print(wordcol[i] + "已导入")
        except:
            print(wordcol[i] + "无法导入")
            conn.rollbakc() # 如果发生错误则回滚

conn.close() #关闭数据库连接

















