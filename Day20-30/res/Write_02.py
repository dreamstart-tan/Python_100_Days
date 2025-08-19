import xlwt
import random

student_names = ['关羽','张飞','赵云','马超','黄忠']
scores = [[random.randrange(50,101) for _ in range(3)] for _ in range(5)]
wb = xlwt.Workbook()
sheet = wb.add_sheet('一年级二班')
header_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5

header_style.pattern = pattern
titles = ('姓名','语文','数学','英语')
for index, title in enumerate(titles):
    sheet.write(0,index,title,header_style)
for row in range(len(scores)):
    sheet.write(row+ 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1,scores[row][col])
wb.save('考试成绩表.xls')











