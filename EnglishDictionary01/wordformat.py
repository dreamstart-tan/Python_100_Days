import requests
import json

import xlrd
import xlwt

def trans(word):
    try:
        url = 'https://fanyi.baidu.com/sug'
        Form_data = {'kw': word}
        # post方式请求网络
        response = requests.post(url,data = Form_data,)
        content = json.loads(response.content.decode())
        result = content['data'][0]['v'] # 获取翻译结果
        print(result)
        return result
    except:
        return ""

def wordclass(mean):
    classlist=["n.","vt.","vi.","adj.","adv.","prep.","conj.","addr.","pron.","pl.","int.","pl.","pref."]
    meanclass=""
    for i in classlist:
        if i in mean:
            meanclass+=i[:-1]+","
    return meanclass

book = xlrd.open_workbook(r'D:\Py100\Python_100_Days\EnglishDictionary01\2021new.xls')
names = book.sheet_names()
sheet = book.sheet_by_name('Sheet1')
row = sheet.row_values(0)
col =sheet.col_values(0)[1:]
sorcol=sheet.col_values(1)[1:]
wtbook = xlwt.Workbook(encoding = 'utf-8')
wtsheet = wtbook.add_sheet('Sheet',cell_overwrite_ok = True)

print(names)
print(row)
print(col)

wtsheet.write(0,0,"单词")
wtsheet.write(0,1,"词性")
wtsheet.write(0,2,"词义")
wtsheet.write(0,3,"首字母")
wtsheet.write(0,4,"来源")
m=1 
for i in col:
    wtsheet.write(m,0,i)
    wtsheet.write(m,1,wordclass(trans(i)))
    wtsheet.write(m,2,trans(i))
    wtsheet.write(m,3,i[0].upper())
    wtsheet.write(m,4,sorcol[m-1])
    m+=1

wtbook.save(r'D:\Py100\Python_100_Days\EnglishDictionary01\2021new+.xls')