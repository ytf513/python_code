#"��ģ�鲻��Ϊcsv.py"
import csv
with open('some.csv','rb') as f:
        reader=csv.reader(f)
        for row in reader:
                print row #��ֵ����ΪList�ڴ�ӡʱ����Ϊ���룬����תΪ�ַ�������",".join(row)
