import urllib  
def cbk(a, b, c):  
    '''''�ص����� 
    @a: �Ѿ����ص����ݿ� 
    @b: ���ݿ�Ĵ�С 
    @c: Զ���ļ��Ĵ�С 
    '''  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print '%.2f%%' % per  
  
url = 'http://www.codecademy.com/zh/tracks/python'  
local = 'files/sina.html'  
urllib.urlretrieve(url, local, cbk)  
