#"��ģ�鲻��Ϊcsv.py"
import csv
someiterable=[['alex1', '', 'male', 'shanghai'],['Amily1', '20', 'femal', 'kunshan']]
with open('some-write.csv','wb') as f:
        writer=csv.writer(f)
        writer.writerows(someiterable)
