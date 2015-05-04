#"该模块不能为csv.py"
import csv
with open('some.csv','rb') as f:
        reader=csv.reader(f)
        for row in reader:
                print row #该值类型为List在打印时可能为乱码，可以转为字符串，用",".join(row)
