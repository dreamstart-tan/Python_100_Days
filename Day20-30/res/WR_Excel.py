import xlrd

wb = xlrd.open_workbook(r'D:\Python_100_Days\Day20-30\res\测试电子表格.xls')
sheetnames = wb.sheet_names()
print(sheetnames)
sheet = wb.sheet_by_name(sheetnames[0])
print(sheet.nrows,sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row,col).value
        if row > 0 :
            if col == 0:
                value = xlrd.xldate_as_tuple(value,1)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            else:
                value = '{value:.2f}'
        print(value,end='\t')
    print()
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols- 1)
print(last_cell_type)
print(sheet.row_values(0))
print(sheet.row_slice(3,0,5))









