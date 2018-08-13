import xlwt

with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()

items = eval(content)

print(items)

file = xlwt.Workbook()

table = file.add_sheet('Test', cell_overwrite_ok=True)

for row in range(len(items)):
    for col in range(len(items[row])):
        table.write(row, col, items[row][col])


file.save('result.xls')